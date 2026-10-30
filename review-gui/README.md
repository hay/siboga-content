# Siboga foto-review

Lokale tool om de automatische koppelingen tussen Siboga-foto's op Wikimedia Commons en expeditiestations goed te keuren of af te wijzen.

## Starten

```
python review-gui/server.py
```

Open daarna http://127.0.0.1:8765. Je hebt alleen Python 3 nodig, zonder extra pakketten. Een andere poort kies je met `python review-gui/server.py 8800`.

## Wat het doet

- **Invoer:** `../siboga_fotos_stations_koppeling.csv` (de voorgestelde koppelingen) en `../siboga_stations_1899-1900.csv` (de stationslijst).
- **Per foto:** je ziet de afbeelding en de beschrijving van Commons, met daaronder de kandidaat-stations. Bij elk station staan de remarks, de datum, de Wikidata-link en een kaartlink.
- **Beoordelen:** vink de passende station(s) aan en klik **Goedkeuren**, of klik **Afwijzen**. Ontbreekt het juiste station, voeg het dan toe met het stationnummer (bv. `47a`).
- **Opslaan:** elke keuze gaat direct naar `beslissingen.json` in deze map. Met **Exporteer CSV** schrijf je `beslissingen.csv`, met daarin de stations, hun Wikidata-ID's en het datumbereik.

## Sneltoetsen

| Toets | Actie |
|---|---|
| ← / → (of K / J) | vorige / volgende foto |
| 1–9 | kandidaat-station aan/uit |
| G | goedkeuren |
| A | afwijzen |
| U | beslissing wissen |
| ? | uitleg (ook via de knop **Help**) |
