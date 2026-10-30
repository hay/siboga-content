# 6. NDE Termennetwerk: plaatsnamen en personen koppelen

**Oordeel: handig hulpmiddel.** Het Termennetwerk is geen dataset maar een zoekdienst van NDE. Je zoekt één term tegelijk in veel terminologiebronnen. Dat helpt om de historische plaatsnamen uit de foto's en het reisverslag aan URI's te koppelen.

## Waar staat het

- **GraphQL-API:** `https://termennetwerk-api.netwerkdigitaalerfgoed.nl/graphql` (POST, JSON)
- Bruikbare bronnen voor ons:
  - Thesaurus Wereldmuseum: `https://data.colonialcollections.nl/nmvw/thesaurus` (plaatsen en volken in Indonesië)
  - GeoNames wereldwijd: `https://www.geonames.org`
  - Nederlandse Thesaurus van Auteursnamen: `http://data.bibliotheken.nl/id/dataset/persons`
  - RKDartists: `https://data.rkd.nl/rkdartists` (voor illustratoren)
  - Wikidata: `https://www.wikidata.org#entities-all`

## Steekproef: "Bima"

Bima komt voor in de UvA-foto's (Baai van Bima, paleis van de sultan van Bima).

```bash
curl -s https://termennetwerk-api.netwerkdigitaalerfgoed.nl/graphql \
  -H 'Content-Type: application/json' \
  -d '{"query":"{ terms(sources: [\"https://data.colonialcollections.nl/nmvw/thesaurus\", \"https://www.geonames.org\"], query: \"Bima\") { source { name } result { ... on Terms { terms { uri prefLabel scopeNote } } } } }"}'
```

Resultaat (eerste treffers):

| Bron | URI | Label |
|---|---|---|
| Thesaurus Wereldmuseum | https://hdl.handle.net/20.500.11840/termmaster10077521 | Bima |
| Thesaurus Wereldmuseum | https://hdl.handle.net/20.500.11840/termmaster10062403 | Bima (regentschap) |
| Thesaurus Wereldmuseum | https://hdl.handle.net/20.500.11840/termmaster10062408 | Bima (stadsgemeente) |
| GeoNames | https://sws.geonames.org/218880/ | Bima (plaats) |
| GeoNames | https://sws.geonames.org/218877/ | Bima (water) |

Een term "Siboga" bestaat in deze thesauri niet; zoeken op "Siboga" in de Cultuurhistorische Thesaurus geeft niets.

## Kansen voor het project

- De plaatsnamen uit de UvA-titels (Bima, Kupang, Solor, Menado, …) in één keer reconciliëren.
- Dezelfde Wereldmuseum-termen gebruiken als de objecten in de Colonial Collections-graaf, zodat foto's en objecten op plaats te koppelen zijn.
