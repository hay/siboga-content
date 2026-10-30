# 1. UvA-bibliotheek / Allard Pierson: 605 records

**Oordeel: zeer bruikbaar.** De collectie "Siboga-expeditie: glasnegatieven" uit de Artis Bibliotheek staat volledig als linked data online, met plaatsnamen, beschrijvingen en namen van opvarenden.

## Waar staat het

- **In het NDE-register:** de datasets *Beeldbank of the University of Amsterdam Library*, *Afbeeldingen van de Bibliotheek UvA* en *Other objects of the University of Amsterdam Library* (uitgever: University of Amsterdam Library). Ze delen één catalogus-endpoint.
- **SPARQL-endpoint:** `https://api.lod.uba.uva.nl/datasets/UB-UVA/Catalogue/sparql`
- **Sleutel:** elk record heeft `dc:subject "Siboga-expeditie"`.
- **URI-patroon:** `https://pid.uba.uva.nl/ark:/88238/b…`. De PID verwijst door naar de catalogus van de UvA, waar het beeld bij staat.

## Wat er in zit

- **Foto's van de reis** met de plaats in de titel: Baai van Bima, Straat Molo, Badjo op Flores, Kupang, Lamakera op Solor, Makassar, de Kutei-rivier, Sulu, Menado, Siau, Ternate, Waigeo en meer. De fotoreeks heeft inventarisnummers 300.000–300.455; daarnaast zijn er foto's onder andere nummers (301.xxx).
- **Het werk aan boord:** dreggen, korren, het laboratorium, de longroom.
- **Opvarenden met naam:** in titels en beschrijvingen (Loyer, Verhey, Nierstrasz, Huysmans, Versluys, Max en Anna Weber).
- **Objecten van de expeditie:** de fotokist, een koffer met parasol, een apothekerskistje.
- **Publicaties:** twee exemplaren van *Liste des algues du Siboga*.
- 361 van de 605 records hebben een uitgebreide beschrijving (`dct:abstract`). Als datering staat er meestal 1899-03-07 tot 1900-02-26.

## Steekproeven

Klik op de PID. Je komt dan op de UvA-catalogus met de foto.

| Inv.nr. | Titel | PID | Beschrijving in de data |
|---|---|---|---|
| 300.427 | de bemanning en de wetenschappelijke staf van de Siboga | https://pid.uba.uva.nl/ark:/88238/b1990032310050205131 | "In het midden Anna Weber-van Bosse met op haar schoot de scheepskat Titi, aan haar rechterkant Max Weber en vlak voor haar Baboe, de persoonlijke bediende van Anna. Linksonder met een pijp de tekenaar van de expeditie, J.W. Huysmans." |
| 300.428 | … met de radja van Misool | https://pid.uba.uva.nl/ark:/88238/b1990032310060205131 | |
| 300.002 | laboratorium aan boord van de Siboga | https://pid.uba.uva.nl/ark:/88238/b1990032250290205131 | "v.l.n.r. H.F. Nierstrasz, J.W. Huysmans, Prof. Max Weber en Dr. J. Versluys" |
| 300.003 | uitzetten van de dreg | https://pid.uba.uva.nl/ark:/88238/b1990032250310205131 | "De dreg is voorzien van een paar dikke zwabbers, die over de grond slepende, fijne dieren in hun lange vezels kunnen vasthouden." |
| 300.005 | bovenkomen van de kor | https://pid.uba.uva.nl/ark:/88238/b1990032250370205131 | |
| 300.011 | de heren Loyer en Verhey op het dek van de Siboga | https://pid.uba.uva.nl/ark:/88238/b1990032251970205131 | Noemt de vier Europese onderofficieren: Verhey, Loyer, Gorter en hofmeester Nieuwenhuyzen |
| 300.020 | Baai van Bima met de Siboga | https://pid.uba.uva.nl/ark:/88238/b1990032252210205131 | |
| 300.021 | Straat Tydeman | https://pid.uba.uva.nl/ark:/88238/b1990032252230205131 | Citaat uit *Een jaar aan boord van H.M. Siboga* over de naamgeving van Straat Tydeman |
| 300.073 | Menado | https://pid.uba.uva.nl/ark:/88238/b1990032253620205131 | "Drie schepen, waaronder de Siboga, liggen voor anker op de rede van Menado (Noord-Celebes)." |
| 050.109 | fotokist Siboga expeditie | https://pid.uba.uva.nl/ark:/88238/b1990031935880205131 | "Op het deksel staat: Siboga expeditie 1899 - 1900." |
| 050.055 | apothekerskistje | https://pid.uba.uva.nl/ark:/88238/b1990031935340205131 | |

**Controle met Commons:** de groepsfoto's 300.425 en 300.428 staan al op Wikimedia Commons als `UvA-BC 300.425 …` en `UvA-BC 300.428 …`. Deze vault heeft er ook records voor. De inventarisnummers in de linked data zijn dezelfde, dus je kunt Commons-bestanden en UvA-records één op één koppelen.

## Zelf de hele lijst ophalen

```sparql
PREFIX dc: <http://purl.org/dc/elements/1.1/>
PREFIX dct: <http://purl.org/dc/terms/>
SELECT ?record ?titel ?beschrijving WHERE {
  ?record dc:subject "Siboga-expeditie" ; dc:title ?titel .
  OPTIONAL { ?record dct:abstract ?beschrijving }
} LIMIT 1000
```

[Voer deze query direct uit (geeft JSON met 605 rijen)](https://api.lod.uba.uva.nl/datasets/UB-UVA/Catalogue/sparql?query=PREFIX+dc%3A+%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Felements%2F1.1%2F%3E%0APREFIX+dct%3A+%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Fterms%2F%3E%0ASELECT+%3Frecord+%3Ftitel+%3Fbeschrijving+WHERE+%7B%0A++%3Frecord+dc%3Asubject+%22Siboga-expeditie%22+%3B+dc%3Atitle+%3Ftitel+.%0A++OPTIONAL+%7B+%3Frecord+dct%3Aabstract+%3Fbeschrijving+%7D%0A%7D+LIMIT+1000)

Alle velden van één record bekijken: vervang de URI in `SELECT ?p ?o WHERE { <https://pid.uba.uva.nl/ark:/88238/b1990032253620205131> ?p ?o }`.

## Kansen voor het project

- Plaatsnamen uit de titels koppelen aan de reisroute van Anna Weber en aan de stations op Wikidata.
- Foto's van het dreggen en korren gebruiken voor een woordenlijst met scheepstermen.
- Ontbrekende foto's naar Commons uploaden, met de PID als bron.

Volledige lijst: [data/uva-allard-pierson-siboga.csv](data/uva-allard-pierson-siboga.csv)
