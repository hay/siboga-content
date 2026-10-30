"""Lokale server voor het beoordelen van foto-stationkoppelingen van de Siboga-expeditie.

Start:  python review-gui/server.py   en open http://127.0.0.1:8765
Leest:  ../siboga_fotos_stations_koppeling.csv en ../siboga_stations_1899-1900.csv
Schrijft: beslissingen.json (na elke keuze) en beslissingen.csv (via 'Exporteer CSV').
"""
import csv
import datetime
import io
import json
import os
import sys
import threading
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
KOPPELING = os.path.join(REPO, "siboga_fotos_stations_koppeling.csv")
STATIONS = os.path.join(REPO, "siboga_stations_1899-1900.csv")
DECISIONS = os.path.join(HERE, "beslissingen.json")
EXPORT = os.path.join(HERE, "beslissingen.csv")
PORT = int(os.environ.get("PORT", sys.argv[1] if len(sys.argv) > 1 else 8765))

lock = threading.Lock()


def read_csv(path):
    with open(path, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def load_decisions():
    if not os.path.exists(DECISIONS):
        return {}
    with open(DECISIONS, encoding="utf-8") as f:
        return json.load(f)


def save_decisions(data):
    tmp = DECISIONS + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    os.replace(tmp, DECISIONS)


def stations_by_number():
    return {s["station"]: s for s in read_csv(STATIONS)}


def export_csv(decisions):
    st = stations_by_number()
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(["bestand", "commons_url", "status", "stations", "wikidata", "datum_vanaf", "datum_tot", "opmerking", "tijd"])
    for bestand, d in sorted(decisions.items()):
        nums = d.get("stations", [])
        dates = sorted({x for n in nums if n in st for x in (st[n]["start_date"], st[n]["end_date"]) if x})
        w.writerow([bestand, "https://commons.wikimedia.org/wiki/" + bestand.replace(" ", "_"), d["status"],
                    "; ".join(nums), "; ".join(st[n]["wikidata_uri"].rsplit("/", 1)[-1] for n in nums if n in st),
                    dates[0] if dates else "", dates[-1] if dates else "", d.get("opmerking", ""), d.get("tijd", "")])
    text = buf.getvalue()
    with open(EXPORT, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return text


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=HERE, **kwargs)

    def log_message(self, fmt, *args):
        if "/api/" in str(args[0] if args else ""):
            super().log_message(fmt, *args)

    def send_body(self, body):
        # in stukken schrijven: grote antwoorden in één keer raakten op Windows soms half kwijt
        for i in range(0, len(body), 32768):
            self.wfile.write(body[i:i + 32768])
        self.wfile.flush()

    def send_json(self, obj, status=200):
        body = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("Connection", "close")
        self.end_headers()
        self.send_body(body)

    def do_GET(self):
        if self.path == "/api/data":
            with lock:
                decisions = load_decisions()
            stations = {n: {k: s[k] for k in ("station", "wikidata_uri", "start_date", "end_date", "latitude", "longitude", "remarks", "operations")}
                        for n, s in stations_by_number().items()}
            return self.send_json({"photos": read_csv(KOPPELING), "stations": stations, "decisions": decisions})
        if self.path == "/api/export":
            with lock:
                text = export_csv(load_decisions())
            body = text.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/csv; charset=utf-8")
            self.send_header("Content-Disposition", 'attachment; filename="beslissingen.csv"')
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Connection", "close")
            self.end_headers()
            self.send_body(body)
            return
        if self.path == "/favicon.ico":
            self.send_response(204)
            self.end_headers()
            return
        if self.path in ("/beslissingen.json", "/server.py") or self.path.startswith("/beslissingen"):
            return self.send_error(404)
        return super().do_GET()

    def do_POST(self):
        if self.path != "/api/decision":
            return self.send_error(404)
        try:
            payload = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))).decode("utf-8"))
            bestand = payload["bestand"]
            status = payload.get("status")
            if status not in (None, "goedgekeurd", "afgewezen"):
                raise ValueError("onbekende status")
            if status == "goedgekeurd" and not payload.get("stations"):
                raise ValueError("goedkeuren kan alleen met minstens één station")
        except (ValueError, KeyError, json.JSONDecodeError) as e:
            return self.send_json({"error": str(e)}, 400)
        with lock:
            decisions = load_decisions()
            if status is None:
                decisions.pop(bestand, None)
            else:
                decisions[bestand] = {"status": status, "stations": [str(s) for s in payload.get("stations", [])],
                                      "opmerking": payload.get("opmerking", "").strip(),
                                      "tijd": datetime.datetime.now().isoformat(timespec="seconds")}
            save_decisions(decisions)
        return self.send_json({"ok": True, "decision": decisions.get(bestand)})


if __name__ == "__main__":
    for path in (KOPPELING, STATIONS):
        if not os.path.exists(path):
            sys.exit(f"Niet gevonden: {path}")
    server = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    print(f"Foto-review draait op http://127.0.0.1:{PORT}  (Ctrl+C om te stoppen)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
