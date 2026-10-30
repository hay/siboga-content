# 4. Specimens via GBIF (Naturalis, NHM Londen, MNHN Parijs en anderen)

**Oordeel: zeer bruikbaar.** Dit is de grootste bron, maar hij staat **niet in het NDE-register**: Naturalis publiceert zijn specimens via GBIF en via een eigen linked-data-URI per specimen.

## Waar staat het

- **GBIF-API:** `https://api.gbif.org/v1/occurrence/search` (JSON, geen sleutel nodig)
- **Naturalis-URI per specimen:** `https://data.biodiversitydata.nl/naturalis/specimen/<registratienummer>`. In GBIF staat die in het veld `occurrenceID`.
- **Sleutel:** het veld `recordedBy` (verzamelaar) is "Siboga Expedition".

## Hoeveel

| Zoekopdracht | Aantal | API-link |
|---|---|---|
| Verzamelaar "Siboga Expedition" | 13.218 | https://api.gbif.org/v1/occurrence/search?recordedBy=Siboga%20Expedition&limit=0 |
| Vrije tekst "siboga" | 22.423 | https://api.gbif.org/v1/occurrence/search?q=siboga&limit=0&facet=institutionCode |
| Verzamelaar Anna Weber-van Bosse | 7 | https://api.gbif.org/v1/occurrence/search?q=siboga&recordedBy=Anna%20Antoinette%20Weber-van%20Bosse |

**Let op:** het hogere getal bij vrije tekst bevat ook soorten die naar de expeditie zijn genoemd (*sibogae*), maar die later elders zijn verzameld. Bijvoorbeeld *Zygophylax sibogae*, verzameld in 1977. Voor de expeditie zelf is de zoekopdracht op verzamelaar betrouwbaarder.

Bij vrije tekst komt het meeste van Naturalis (Cnidaria 4.121, Porifera 3.286, Crustacea 2.342, Echinodermata 1.911, Bryozoa 1.512, Tunicata 1.264, Botany 533, Mollusca 530) en van het Natural History Museum in Londen (4.464).

## Steekproeven

De GBIF-pagina's (`www.gbif.org/occurrence/…`) zijn gewone webpagina's; de API-link geeft hetzelfde record als JSON.

| Instelling | Registratienummer | Soort | Vindplaats en datum | Links |
|---|---|---|---|---|
| Naturalis | ZMA.CRUS.D.241114 | *Munida* sp. | bij de Kei-eilanden, 1899-12-10 | https://data.biodiversitydata.nl/naturalis/specimen/ZMA.CRUS.D.241114 · https://www.gbif.org/occurrence/2434502468 |
| Naturalis | ZMA.CRUS.D.240937 | *Synalpheus* sp. | Pulu Kaniungan ketjil, 1899-06-21 | https://data.biodiversitydata.nl/naturalis/specimen/ZMA.CRUS.D.240937 · https://www.gbif.org/occurrence/2434526098 |
| Naturalis | RMNH.COEL.5910 | *Acabaria ramulosa* | "St. 105, Siboga Exp." | https://data.biodiversitydata.nl/naturalis/specimen/RMNH.COEL.5910 · https://www.gbif.org/occurrence/3079322463 |
| Naturalis | ZMA.ECH.E.5272 | *Heterocentrotus mamillatus*, de lanszee-egel uit de Naturalis-topstukken | – | https://data.biodiversitydata.nl/naturalis/specimen/ZMA.ECH.E.5272 · https://www.gbif.org/occurrence/2432710356 |
| NHM Londen | 2001.9.10.12-14 | *Hippopodina feegeensis* | "Siboga Stn 77, Borneo Bank", 1899-06-10, −3,225 / 117,3 | https://www.gbif.org/occurrence/1055537527 |
| NHM Londen | 2002.7.10.3 | *Rhynchozoon bifurcum* | "Siboga Stn 274", 1899-12-26, −5,4672 / 134,8858 | https://www.gbif.org/occurrence/1057078675 |
| MNHN Parijs | 2023-2850 | *Diadema setosum* | Baai van Nangamessi, Sumba, station 53, 1899-04-21/22 | https://www.gbif.org/occurrence/4092146428 |
| MNHN Parijs | 2023-3330 | *Laganum decagonale* | station 294, 1900-01-23, −10,2033 / 124,455 | https://www.gbif.org/occurrence/4138991301 |
| Herbarium Trondheim | TRH 3315 | *Lithothamnion australe* subsp. *minutulum* | Pulu Tongkil, Sulu-archipel, 1899-07-05; verzameld door **Anna Weber-van Bosse** | https://www.gbif.org/occurrence/1041884321 |

## De koppeling met de stations werkt

Specimens met een stationsnummer vallen samen met de stations op Wikidata (zie [05-wikidata-stations.md](05-wikidata-stations.md)):

- MNHN 2023-3330, station 294: −10,203333 / 124,455. Wikidata-station 294 (https://www.wikidata.org/wiki/Q141749232): −10,2033 / 124,455. **Dezelfde plek.**
- NHM 2002.7.10.3, station 274: −5,4672 / 134,8858. Wikidata-station 274 (https://www.wikidata.org/wiki/Q141749214): −5,47 / 134,8983. Op ruim een kilometer na dezelfde plek.

Je kunt specimens dus aan een station hangen, en zo op de kaart zetten.

## Kansen voor het project

- Per station laten zien wat er is opgehaald, met links naar de specimens in Leiden, Londen en Parijs.
- De algen die Anna Weber-van Bosse zelf verzamelde, als apart verhaal.
