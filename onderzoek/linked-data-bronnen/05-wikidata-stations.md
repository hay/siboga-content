# 5. Wikidata: de stations van de expeditie

**Oordeel: de spil.** Wikidata staat ook in het NDE-register, maar het belangrijkste is dat alle andere bronnen er aan elkaar te knopen zijn. De stations van de expeditie staan er al.

## Wat er staat

- **363 items** van het type *sampling station* (Q141748032), met labels als "Siboga Expedition station no. 294".
- **255** daarvan hebben coördinaten (P625).
- Verder: de expeditie, het schip Hr.Ms. Siboga (https://www.wikidata.org/wiki/Q123196833), opvarenden en wetenschappers, en taxa die naar de Siboga zijn genoemd.

## Steekproeven

| Station | Item | Coördinaten |
|---|---|---|
| 53 | https://www.wikidata.org/wiki/Q141749262 | (geen) |
| 105 | https://www.wikidata.org/wiki/Q141749067 | 6,1333 / 121,3167 |
| 274 | https://www.wikidata.org/wiki/Q141749214 | −5,47 / 134,8983 |
| 294 | https://www.wikidata.org/wiki/Q141749232 | −10,2033 / 124,455 |

Station 294 en 274 komen overeen met specimens in Parijs en Londen (zie [04-gbif-specimens.md](04-gbif-specimens.md)).

## Zelf ophalen

```sparql
SELECT ?station ?stationLabel ?coord WHERE {
  ?station wdt:P31 wd:Q141748032 .
  OPTIONAL { ?station wdt:P625 ?coord }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "nl,en". }
}
```

[Open deze query in de Wikidata Query Service (met kaart)](https://query.wikidata.org/#%23defaultView%3AMap%0ASELECT%20%3Fstation%20%3FstationLabel%20%3Fcoord%20WHERE%20%7B%0A%20%20%3Fstation%20wdt%3AP31%20wd%3AQ141748032%20.%0A%20%20OPTIONAL%20%7B%20%3Fstation%20wdt%3AP625%20%3Fcoord%20%7D%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22nl%2Cen%22.%20%7D%0A%7D)

## Koppelen aan de andere bronnen

| Bron | Wikidata-property |
|---|---|
| KB-auteurs (NTA) | P1006 (NTA-ID) |
| Soorten op GBIF | P846 (GBIF-taxon-ID); losse specimens hebben geen eigen ID-property, die kunnen als bron of via P973 ("beschreven op URL") |
| UvA-foto's | via Commons-bestanden met dezelfde inventarisnummers |
| Wereldmuseum | de handle-URI's als bron of via P973 |
