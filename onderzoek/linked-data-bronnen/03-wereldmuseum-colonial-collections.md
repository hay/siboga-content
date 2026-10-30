# 3. Wereldmuseum (via de Colonial Collections Knowledge Graph)

**Oordeel: bruikbaar, met wat zoekwerk.** De Colonial Collections Knowledge Graph bundelt de collecties van onder meer het Wereldmuseum (NMVW, voorheen Tropenmuseum), Bronbeek en het Rijksmuseum. Er zitten drie soorten Siboga-materiaal in:

1. **160 objecten met Anna Weber-van Bosse als vroegere eigenaar**: een etnografische collectie (reeks TM-1596) en foto's van plaatsen die de expeditie aandeed.
2. **Expeditiefoto's** die in de beschrijving "Siboga-expeditie" noemen.
3. **Brieven van Max Weber** over de schenking van zijn etnografische collectie.

## Waar staat het

- **In het NDE-register:** *Knowledge Graph* (uitgever: Colonial Collections Consortium).
- **SPARQL-endpoint:** `https://api.colonialcollections.nl/datasets/data-hub/knowledge-graph/services/kg/sparql` (Virtuoso)
- **Datamodel:** Linked Art / CIDOC-CRM. Een object (`crm:E22_Human-Made_Object`) heeft een naam en inventarisnummer via `crm:P1_is_identified_by`, een beschrijving via `crm:P67i_is_referred_to_by` en een verwerving via `crm:P24i_changed_ownership_through`.
- **URI-patroon:** `https://n2t.net/ark:/27023/…` opent in de browser van Colonial Collections. Elk Wereldmuseum-object heeft ook een handle (`https://hdl.handle.net/20.500.11840/…`) die naar de collectiesite van het Wereldmuseum gaat, met foto.

## A. De collectie van Anna Weber-van Bosse

Anna Weber-van Bosse heeft een eigen persoons-URI in de graaf:
https://n2t.net/ark:/27023/ebaeba84ef5afa5b0957afdaf2b2e3dc ("Dr. A.A. (Anne Antoinette) Weber-Van Bosse"). Bij 160 objecten is zij de partij van wie de eigendom overging. 149 daarvan hebben een afbeelding.

| Inventarisnummer | Naam | Pagina op collectie.wereldmuseum.nl | Object-URI |
|---|---|---|---|
| WM-903056 | Voorouderbeeld op een graf, eiland Damar | https://hdl.handle.net/20.500.11840/1151007 | https://n2t.net/ark:/27023/4162a3f242154b269a73afba673b0e50 |
| WM-903038 | Huis op Salajer | https://hdl.handle.net/20.500.11840/1151698 | https://n2t.net/ark:/27023/c9d4a7673fcf7f80ac8433a72b7cdc8d |
| TM-1596-29 | Kalkhouder met deksel, gemaakt van een kalebas | https://hdl.handle.net/20.500.11840/57874 | https://n2t.net/ark:/27023/ca94123776376e6c9acc9e669eff800a |
| TM-1596-77 | Schild | https://hdl.handle.net/20.500.11840/57957 | https://n2t.net/ark:/27023/0c3f830da168c9e2f048b240e231084b |
| TM-1596-91 | Dwarsfluit van bamboe met zes vingergaten | https://hdl.handle.net/20.500.11840/57985 | https://n2t.net/ark:/27023/f2efede0f36a486646870af235685b30 |
| TM-1596-1 | Houten watervat | https://hdl.handle.net/20.500.11840/57844 | https://n2t.net/ark:/27023/3c1105cffbf7b3488e618aaecfd28c3b |

Andere foto's in deze groep: Kampong Bara op Boeroe (WM-902272), twee mannen van de Aroe-eilanden (WM-902752), de noordoostpunt van Timor (WM-902766), een staatsieprauw van Hoog-Kei (WM-903057). Dat zijn allemaal plekken op de route van de Siboga.

**Voorzichtig met conclusies:** de data zegt dat Anna Weber-van Bosse vroegere eigenaar was. Of alle TM-1596-objecten tijdens de expeditie verzameld zijn, staat er niet bij. Dat moet je per object op de collectiesite nalopen.

Query voor de hele lijst:

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX la: <https://linked.art/ns/terms/>
SELECT ?object (SAMPLE(?naam) AS ?naam) (SAMPLE(?pagina) AS ?pagina) WHERE {
  ?object crm:P24i_changed_ownership_through ?verwerving .
  ?verwerving crm:P23_transferred_title_from <https://n2t.net/ark:/27023/ebaeba84ef5afa5b0957afdaf2b2e3dc> .
  OPTIONAL { ?object crm:P1_is_identified_by/crm:P190_has_symbolic_content ?naam }
  OPTIONAL { ?object crm:P129i_is_subject_of/la:digitally_carried_by/la:access_point ?pagina }
} GROUP BY ?object
```

[Voer deze query direct uit (geeft JSON met 160 objecten)](https://api.colonialcollections.nl/datasets/data-hub/knowledge-graph/services/kg/sparql?query=PREFIX+crm%3A+%3Chttp%3A%2F%2Fwww.cidoc-crm.org%2Fcidoc-crm%2F%3E%0APREFIX+la%3A+%3Chttps%3A%2F%2Flinked.art%2Fns%2Fterms%2F%3E%0ASELECT+%3Fobject+%28SAMPLE%28%3Fnaam%29+AS+%3Fnaam%29+%28SAMPLE%28%3Fpagina%29+AS+%3Fpagina%29+WHERE+%7B%0A++%3Fobject+crm%3AP24i_changed_ownership_through+%3Fverwerving+.%0A++%3Fverwerving+crm%3AP23_transferred_title_from+%3Chttps%3A%2F%2Fn2t.net%2Fark%3A%2F27023%2Febaeba84ef5afa5b0957afdaf2b2e3dc%3E+.%0A++OPTIONAL+%7B+%3Fobject+crm%3AP1_is_identified_by%2Fcrm%3AP190_has_symbolic_content+%3Fnaam+%7D%0A++OPTIONAL+%7B+%3Fobject+crm%3AP129i_is_subject_of%2Fla%3Adigitally_carried_by%2Fla%3Aaccess_point+%3Fpagina+%7D%0A%7D+GROUP+BY+%3Fobject)

## B. Expeditiefoto's en brieven

| Inventarisnummer | Wat | Object-URI |
|---|---|---|
| TM-10018523 | Runderen bij een steiger op een van de Banda-eilanden. Beschrijving: "Deze foto is gemaakt tijdens de Siboga Expeditie van 1899-1900, … onder leiding van prof. dr. M.W.C. Weber (zoöloog) en zijn vrouw dr. A.A. Weber van Bosse." Pagina: https://hdl.handle.net/20.500.11840/299629 | https://n2t.net/ark:/27023/c5aed58d2d05fa99da0d199e742a3393 |
| TM-10006545 | Zeilvis, 2,68 m lang, gevangen aan boord van H.M. Siboga te Banda | https://n2t.net/ark:/27023/56c4d4d2200a9031310af112b0eda9df |
| TM-10005840 | Mannen van de Aroe-eilanden aan boord van de H.M. Siboga | https://n2t.net/ark:/27023/e3219e7bb66f591165fac41c01d808ab |
| TM-10014615 | Opnemingen per stoomsloep tijdens de Siboga-expeditie | https://n2t.net/ark:/27023/5366db5f7a601f9e1ecfd12fe86e6b33 |
| TM-60048273 | Bijeenkomst van het bestuur van de Maatschappij ter Bevordering van het Natuurkundig Onderzoek der Nederlandsche Koloniën met de leden van de Siboga-expeditie | https://n2t.net/ark:/27023/c7de3f271f064c62a561fd2c31472bcd |
| TM-60056241 | Kalkalgen (Lithothamnium), verzameld tijdens de Siboga-expeditie, op de jubileumtentoonstelling van het Koloniaal Instituut (1923) | https://n2t.net/ark:/27023/287a46fc8ed0a0c54ceec13df3433555 |
| NL-LdnRMV-A1-15-430/431 | Brief van Max Weber aan Serrurier: hij schenkt zijn etnografische voorwerpen uit Flores, Luwu en Zuid-Celebes aan het Rijks Ethnographisch Museum | https://n2t.net/ark:/27023/196c0571528021bd1dd62d37c6f8864d |
| NL-LdnRMV-A1-15-432 | Brief van Max Weber aan Serrurier: hij vraagt zijn naam en die van zijn vrouw niet in de Staatscourant te vermelden | https://n2t.net/ark:/27023/a4729b2d7b4d0f8ec0e562235e7eae92 |
| BI-1950-17-138 (Rijksmuseum) | Brief aan Max Wilhelm Carl Weber en Anne Antoinette Weber-van Bosse | https://n2t.net/ark:/27023/916f65c616d3c4d50606bae13f117939 |

Ook interessant: de foto van Banda (TM-10018523) is verworven van de **Maatschappij ter Bevordering van het Natuurkundig Onderzoek der Nederlandsche Koloniën**, de opdrachtgever van de expeditie (https://n2t.net/ark:/27023/4fccdbdbcbd9899a486b2afbaebbe6e2). Van die Maatschappij komen 2.771 objecten. Die zijn niet allemaal van de Siboga, want de Maatschappij financierde ook andere expedities.

Vrije-tekstzoekopdracht naar alle 147 vermeldingen van "siboga" (de helft gaat over de stad Sibolga):

```sparql
PREFIX bif: <bif:>
SELECT ?s ?tekst ?graaf WHERE {
  GRAPH ?graaf { ?s ?p ?tekst . ?tekst bif:contains '"siboga"' }
} LIMIT 500
```

[Voer deze query direct uit](https://api.colonialcollections.nl/datasets/data-hub/knowledge-graph/services/kg/sparql?query=PREFIX+bif%3A+%3Cbif%3A%3E%0ASELECT+%3Fs+%3Ftekst+%3Fgraaf+WHERE+%7B%0A++GRAPH+%3Fgraaf+%7B+%3Fs+%3Fp+%3Ftekst+.+%3Ftekst+bif%3Acontains+%27%22siboga%22%27+%7D%0A%7D+LIMIT+500)

## Kansen voor het project

- Het herkomstverhaal van de verzamelde objecten: wat namen de Webers mee, en van wie?
- Foto's van dezelfde plekken naast de UvA-foto's leggen (bijvoorbeeld Banda, Salajer, Aroe).

Volledige lijsten: [data/wereldmuseum-weber-van-bosse.csv](data/wereldmuseum-weber-van-bosse.csv) en [data/colonial-collections-siboga-treffers.csv](data/colonial-collections-siboga-treffers.csv)
