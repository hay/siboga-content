# 2. KB: de monografieënreeks met auteurs

**Oordeel: zeer bruikbaar** voor de publicaties en de wetenschappers. De KB beschrijft de reeks *Siboga-Expeditie* als linked data, met de delen (livraisons) eraan gekoppeld en de auteurs als persoons-URI uit de Nederlandse Thesaurus van Auteursnamen (NTA).

## Waar staat het

- **In het NDE-register:** *Dutch National Bibliography Complete (NBT)* en *Personen uit de Nederlandse Thesaurus van Auteursnamen (NTA)* (uitgever: KB, nationale bibliotheek).
- **SPARQL-endpoint:** `https://data.bibliotheken.nl/sparql`
- **De reeks zelf:** http://data.bibliotheken.nl/id/nbt/p850960223. *Siboga-expeditie: uitkomsten op zoologisch, botanisch, oceanographisch en geologisch gebied …*, 1902–1970, ISSN 0165-2656, OCLC 905464684.
- **Sleutel:** de delen hangen aan de reeks met `schema:isPartOf`.

## Wat er in zit

- 133 records in de reeks, waarvan 117 met een livraisonnummer. Per deel: titel, jaar, taal, aantal pagina's, OCLC-nummer en onderwerpen.
- 58 verschillende auteurs, allemaal als NTA-URI. Die zijn te koppelen aan Wikidata via property P1006 (NTA-ID).

## Steekproeven

Een URI van `data.bibliotheken.nl` opent in de linked-databrowser van de KB.

| Livraison | Jaar | Titel | Deel-URI | Auteur (NTA-URI) |
|---|---|---|---|---|
| 1 | 1901 | Die Holothurien der Siboga-Expedition | http://data.bibliotheken.nl/id/nbt/p039929612 | Carel Philip Sluiter, http://data.bibliotheken.nl/id/thes/p070147884 |
| 2 | 1901 | The genus Halimeda | http://data.bibliotheken.nl/id/nbt/p036047538 | Ethel Sarel Barton (Mrs. A. Gepp), http://data.bibliotheken.nl/id/thes/p072805706 |
| 4 | 1902 | Description of the ship and appliances used for scientific exploration | http://data.bibliotheken.nl/id/nbt/p040282279 | Gustaaf Frederik Tydeman, http://data.bibliotheken.nl/id/thes/p069164460 |
| 6 | 1902 | Die Gorgoniden der Siboga-Expedition | http://data.bibliotheken.nl/id/nbt/p04029028X | Jan Versluys (Jzn.), http://data.bibliotheken.nl/id/thes/p072800828 |
| 79 | 1916 | Meeresgrundproben der Siboga-Expedition | http://data.bibliotheken.nl/id/nbt/p036123056 | O.B. Böggild, http://data.bibliotheken.nl/id/thes/p072799161 |

Livraison 4, van kapitein Tydeman, beschrijft het schip en de instrumenten aan boord.

**Andere personen in de NTA:**

- Anna Antoinette Weber-van Bosse: http://data.bibliotheken.nl/id/thes/p072591218
- Hugo Frederik Nierstrasz: http://data.bibliotheken.nl/id/thes/p069280851

## Zelf de hele lijst ophalen

```sparql
PREFIX schema: <http://schema.org/>
SELECT ?deel ?livraison ?titel ?auteur WHERE {
  ?deel schema:isPartOf <http://data.bibliotheken.nl/id/nbt/p850960223> ; schema:name ?titel .
  OPTIONAL { ?deel schema:description ?livraison }
  OPTIONAL { ?deel schema:author ?auteur }
} LIMIT 1000
```

[Voer deze query direct uit (geeft JSON met 218 rijen; een deel met meer auteurs komt meer keer voor)](https://data.bibliotheken.nl/sparql?query=PREFIX+schema%3A+%3Chttp%3A%2F%2Fschema.org%2F%3E%0ASELECT+%3Fdeel+%3Flivraison+%3Ftitel+%3Fauteur+WHERE+%7B%0A++%3Fdeel+schema%3AisPartOf+%3Chttp%3A%2F%2Fdata.bibliotheken.nl%2Fid%2Fnbt%2Fp850960223%3E+%3B+schema%3Aname+%3Ftitel+.%0A++OPTIONAL+%7B+%3Fdeel+schema%3Adescription+%3Flivraison+%7D%0A++OPTIONAL+%7B+%3Fdeel+schema%3Aauthor+%3Fauteur+%7D%0A%7D+LIMIT+1000)

**Let op:** niet elk deel hangt met `isPartOf` aan de reeks. Zoeken op titels met "Siboga" vindt 99 unieke titels, onder meer losse herdrukken. Vrije tekst zoeken gaat alleen zo (anders time-out):

```sparql
PREFIX bif: <bif:>
SELECT ?s ?naam WHERE {
  GRAPH <http://data.bibliotheken.nl/nbt> { ?s <http://schema.org/name> ?naam . ?naam bif:contains '"siboga"' }
} LIMIT 300
```

## Kansen voor het project

- Controle en aanvulling van de bestaande lijst van livraisons.
- De auteurs koppelen aan Wikidata en aan de specimens die zij beschreven.

Volledige lijst: [data/kb-siboga-livraisons.csv](data/kb-siboga-livraisons.csv)
