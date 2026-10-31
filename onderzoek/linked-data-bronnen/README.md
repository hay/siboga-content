# Linked-databronnen over de Siboga-expeditie

Verkenning van 30 oktober 2026: welke linked-databronnen uit (en rond) het [NDE-datasetregister](https://datasetregister.netwerkdigitaalerfgoed.nl/) bevatten echt materiaal over de Siboga-expeditie (1899–1900)?

Elke bron heeft een eigen bestand met **steekproeven**: losse URI's die je kunt aanklikken, plus een SPARQL- of API-link die de hele lijst live ophaalt. Alles is op 30 oktober 2026 gecontroleerd.

| # | Bron | Wat er staat | Omvang | Bestand |
|---|---|---|---|---|
| 1 | UvA-bibliotheek / Allard Pierson | Expeditiefoto's (glasnegatieven) en objecten van de expeditie | 605 records | [01-uva-allard-pierson.md](01-uva-allard-pierson.md) |
| 2 | KB, nationale bibliotheek | De monografieënreeks *Siboga-Expeditie*, met auteurs | 218 rijen (reeksdelen × auteurs) | [02-kb-monografieen.md](02-kb-monografieen.md) |
| 3 | Wereldmuseum via de Colonial Collections-graaf | Objecten van Anna Weber-van Bosse, expeditiefoto's, brieven van Max Weber | 160 objecten + ruim 80 andere treffers | [03-wereldmuseum-colonial-collections.md](03-wereldmuseum-colonial-collections.md) |
| 4 | GBIF (Naturalis, NHM Londen, MNHN Parijs, …) | Specimens met datum, vindplaats en stationsnummer | 13.218 specimens met verzamelaar "Siboga Expedition" | [04-gbif-specimens.md](04-gbif-specimens.md) |
| 5 | Wikidata | De stations van de expeditie | 363 items, 255 met coördinaten | [05-wikidata-stations.md](05-wikidata-stations.md) |
| 6 | NDE Termennetwerk | Historische plaatsnamen en personen koppelen | dienst, geen dataset | [06-termennetwerk.md](06-termennetwerk.md) |
| 8 | NDE Termennetwerk | Matches voor de termen uit het Verklarend woordenboek | 47 van 79 termen goed, 16 deels | [08-termennetwerk-woordenboek.md](08-termennetwerk-woordenboek.md) |
| – | Bevraagd zonder resultaat | Rijksmuseum, RCE, RKD, en andere | – | [07-niet-gevonden.md](07-niet-gevonden.md) |

## Waarom vind je in het register zelf niets?

Zoek je in het NDE-datasetregister op "Siboga", dan vind je geen dataset. Dat klopt ook: van de 3.434 datasets heeft er geen enkele Siboga in de titel, beschrijving of trefwoorden (gecontroleerd via de SPARQL-endpoint van het register). Het materiaal zit *in* grote, algemene datasets, zoals "Beeldbank of the University of Amsterdam Library" of de "Knowledge Graph" van Colonial Collections. Je vindt het alleen door die datasets zelf te bevragen via hun SPARQL-endpoint.

Daarnaast zijn er drie valkuilen:

1. **Sibolga.** "Siboga" is ook de oude naam van de havenstad Sibolga op Sumatra. Bij het Rijksmuseum, het Wereldmuseum en Bronbeek gaat een groot deel van de treffers over die stad (rubberplantages, havengezichten, 1910–1920), niet over de expeditie.
2. **Zoeken in tekst loopt vast.** Een gewone `FILTER(CONTAINS(...))` geeft bij de grote endpoints (KB, Colonial Collections) een time-out. Die draaien op Virtuoso, en daar werkt vrije tekst alleen met `PREFIX bif: <bif:>` en `?tekst bif:contains '"siboga"'`.
3. **Naturalis staat niet in het register.** De specimens zijn wel als linked data beschikbaar (`https://data.biodiversitydata.nl/naturalis/specimen/…`), maar je vindt ze via GBIF.

## Werkwijze

1. Het register zelf bevraagd via SPARQL (`https://datasetregister.netwerkdigitaalerfgoed.nl/sparql`, 3.434 datasets): titels, beschrijvingen, trefwoorden en uitgevers gefilterd op Siboga, Indonesië, natuurhistorie, maritiem, koloniaal, personen en plaatsnamen.
2. Van de kansrijke datasets de distributies (SPARQL-endpoints, API's) opgezocht en bevraagd op "siboga", Weber, Weber-van Bosse en Tydeman.
3. Per treffer de URI's nagelopen: lossen ze op, en gaat het echt over de expeditie?

## Gegevensbestanden

In [data/](data/) staan de volledige lijsten als CSV, zoals ze op 30 oktober 2026 uit de endpoints kwamen:

- `uva-allard-pierson-siboga.csv`: 605 records (URI, inventarisnummer, titel, beschrijving, datering)
- `kb-siboga-livraisons.csv`: 133 records uit de reeks (URI, livraison, jaar, titel, auteurs, NTA-URI's, OCLC)
- `wereldmuseum-weber-van-bosse.csv`: 160 objecten (object-URI, inventarisnummer, naam, type, pagina op de collectiesite, afbeelding)
- `colonial-collections-siboga-treffers.csv`: 84 teksttreffers, gefilterd op de expeditie, Weber en Tydeman. Let op: de URI's daarin zijn soms de beschrijving of naam van een object, niet het object zelf.
