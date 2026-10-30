# 7. Bevraagd zonder (bruikbaar) resultaat

Deze bronnen uit het NDE-register zijn wel bevraagd, maar leverden niets over de expeditie op. Zo hoeft niemand ze opnieuw te proberen.

| Bron (dataset in het register) | Endpoint | Resultaat |
|---|---|---|
| Rijksmuseum (*Indisch erfgoed*, *maritiem digitaal*, *Entire Public Domain Set*) | `https://data.rijksmuseum.nl/search/collection?title=siboga` | 4 treffers, allemaal foto's van de stad Sibolga op Sumatra. Wel een brief aan Max en Anna Weber, via de Colonial Collections-graaf (zie [03](03-wereldmuseum-colonial-collections.md)). |
| RCE, *Colonial Objects* | `https://api.linkeddata.cultureelerfgoed.nl/datasets/rce/colonialobjects/services/colonialobjects/sparql` | Niets. |
| Wereldmuseum, *NMVW Collection Archives* (los endpoint) | `https://api.colonialcollections.nl/datasets/nmvw/collection-archives/sparql` | Niets op "siboga". De archiefstukken staan wel in de grote Colonial Collections-graaf. |
| Wereldmuseum, *Thesaurus* | `https://api.colonialcollections.nl/datasets/nmvw/thesaurus/services/thesaurus/sparql` | Geen term "Siboga"; wel plaatsnamen (zie [06](06-termennetwerk.md)). |
| RKD Knowledge Graph | `https://api.rkd.triply.cc/datasets/rkd/RKD-Knowledge-Graph/services/SPARQL/sparql` | Geen Siboga. Wel "Weber-van Bosse" als verzamelaar: https://data.rkd.nl/collectors/22981. Misschien bruikbaar voor de illustratoren van de monografieën; niet verder uitgezocht. |
| Teylers Museum | `https://sparql.ldmax.nl/Q474563` | Niets. |
| Maritiem Museum Rotterdam | `https://sparql.ldmax.nl/Q2755458` | Niets. |
| AdamNet Heritage | `https://api.druid.datalegend.net/datasets/AdamNet/Heritage/services/Heritage/sparql` | Endpoint geeft "Not found or unauthorized". |
| Het Scheepvaartmuseum | – | Staat alleen met een WO2-dataset in het register. |

## Niet getest, maar mogelijk de moeite waard

- **Moluks Historisch Museum** (*Beeldbank*, *Objecten*, *Verhalen*; dumps in Turtle en CSV): Ambon, Banda, Kei- en Aroe-eilanden.
- **Open Archieven / Nationaal Archief** (persoonsvermeldingen): voor de Europese bemanning (Verhey, Loyer, Gorter, Nieuwenhuyzen).
- **GLOBALISE** (*Geographical Indices*, thesauri): historische plaatsnamen in de archipel, wel uit de VOC-tijd.
- **Universiteitsmuseum Utrecht** (JSON-LD-dump): natuurhistorische collectie, misschien Siboga-materiaal.
