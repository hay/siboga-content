# 8. Termennetwerk: termen uit het Verklarend woordenboek

Verkenning van 31 oktober 2026: welke termen uit [[Verklarend woordenboek]] hebben een match in het [Termennetwerk](https://termennetwerk.netwerkdigitaalerfgoed.nl/) van het NDE?

**Uitkomst:** van de 79 termen hebben er 47 een goede match, 16 alleen een bredere of verwante term en 16 geen match. Vooral scheepsterminologie (stoomspil, rolstopper, veeraccumulator, waterschepper, korboom) en marinerangen (stoker, hoofdmachinist, korporaal-hofmeester) ontbreken. De koloniale termen zitten bijna allemaal in de Indisch Erfgoed Thesaurus.

## Werkwijze

- Gezocht via de GraphQL-API (`https://termennetwerk-api.netwerkdigitaalerfgoed.nl/graphql`), zie [[06-termennetwerk]].
- Bronnen: Cultuurhistorische Thesaurus (CHT, RCE), Art & Architecture Thesaurus (AAT), Indisch Erfgoed Thesaurus (IED), Thesaurus Wereldmuseum, GTAA onderwerpen (Beeld & Geluid) en Wikidata.
- CHT en AAT gebruiken meervoudsvormen; waar het enkelvoud niets gaf, is ook het meervoud of een synoniem gezocht.
- **Match** betekent: *ja* = zelfde begrip; *deels* = bredere of verwante term, of omschrijving niet gecontroleerd; *nee* = niets bruikbaars. Het oordeel is gebaseerd op het label en de eerste 90 tekens van de omschrijving (scopeNote), niet op de volledige omschrijving.
- Wikidata-treffers op straatnamen en achternamen (Ankerplaats, Kajuit, Sloep, Fuik …) zijn weggelaten.

## Het schip en de scheepvaart

| Term | Match | Beste treffers | Opmerking |
|---|---|---|---|
| Ankerplaats | deels | ankerplaatsen (ruimten aan de waterkant) (AAT) <http://vocab.getty.edu/aat/300007927> | AAT bedoelt open waterplaatsen aan de kant; zie ook *rede* |
| rede | ja | reden (ankerplaats) (CHT) <https://data.cultureelerfgoed.nl/term/id/cht/4be53c95-9347-4246-a51c-fe6e996bb12b> |  |
| Dok | ja | droogdokken (CHT) <https://data.cultureelerfgoed.nl/term/id/cht/492dc21e-48c8-402d-97cc-0cf085f65cb5><br>droogdokken (AAT) <http://vocab.getty.edu/aat/300120748> | AAT *dokken* (300120801) is breder |
| Donkere kamer | ja | donkere kamers (AAT) <http://vocab.getty.edu/aat/300004512> |  |
| Hr.Ms. | nee | – |  |
| Kajuit | ja | kajuiten (CHT) <https://data.cultureelerfgoed.nl/term/id/cht/7ac78f97-2264-44b0-a4f3-afb427e0e2a5> | CHT: werk- en eetruimte voor officieren; AAT *cabines* (300248156) is breder |
| Kampanje | ja | kampanjes (CHT) <https://data.cultureelerfgoed.nl/term/id/cht/a1eeb86c-da32-4551-a3d1-9c3865996531> |  |
| Kanonneerboot | ja | kanonneerboten (CHT) <https://data.cultureelerfgoed.nl/term/id/cht/001e5a82-1f45-4241-a94f-d449bc600a1d><br>kanonneerboten (AAT) <http://vocab.getty.edu/aat/300232845><br>kanonneerboot (Wikidata) <http://www.wikidata.org/entity/Q214196> |  |
| Kolen laden | ja | bunkeren (Wikidata) <http://www.wikidata.org/entity/Q1009603> | alleen in Wikidata |
| Marinevaartuig | ja | marineschepen (CHT) <https://data.cultureelerfgoed.nl/term/id/cht/4b64c746-06bc-4db7-a7eb-7bbe788599f5><br>marineschepen (AAT) <http://vocab.getty.edu/aat/300232810> |  |
| Monsterrol | deels | monsterrollen (CHT) <https://data.cultureelerfgoed.nl/term/id/cht/646086e4-486b-44e8-8cf5-27e3ce18f91b><br>monsterrol (Wikidata) <http://www.wikidata.org/entity/Q65789047> | CHT en AAT (300027828) beschrijven lijsten van troepen, geen scheepsbemanning |
| Sloep | deels | sloepen (GTAA) <http://data.beeldengeluid.nl/gtaa/26737><br>sloepen (Wereldmuseum) <https://hdl.handle.net/20.500.11840/termmaster10068319> | AAT *sloepen* (300212979) is een zeilschip, andere betekenis; omschrijving GTAA/Wereldmuseum niet gecontroleerd |
| roeisloep | nee | – |  |
| stoomsloep | nee | – |  |
| vlet | deels | vletten (Wikidata) <http://www.wikidata.org/entity/Q2145154> | Wikidata: begrip uit de binnenvaart |
| Stoomspil | deels | kaapstanders (waterbouw) (CHT) <https://data.cultureelerfgoed.nl/term/id/cht/44e3f082-329c-49c3-a1fa-546da9a28b9b><br>lieren (hefwerktuigen) (AAT) <http://vocab.getty.edu/aat/300022367> | alleen bredere termen; geen stoomspil of stoomlier |
| Tros | ja | trossen (CHT) <https://data.cultureelerfgoed.nl/term/id/cht/60434021-b296-4fb1-85ca-ec88951ae9fe> |  |
| staaltros | deels | kabels (CHT) <https://data.cultureelerfgoed.nl/term/id/cht/85074203-7473-4702-87c7-b622d6f867fa><br>kabels (objectgenres) (AAT) <http://vocab.getty.edu/aat/300014618> | bredere term |
| Wacht houden | nee | – |  |
| Zeemijl | ja | zeemijlen (CHT) <https://data.cultureelerfgoed.nl/term/id/cht/a3c241e7-0e7f-4c43-a88e-49163b91417c><br>zeemijl (Wikidata) <http://www.wikidata.org/entity/Q93318> |  |
| Zeestraat | ja | zeestraten (CHT) <https://data.cultureelerfgoed.nl/term/id/cht/cd3fad9d-4ca6-4137-a5fa-fcb03bdded5f> |  |

## De mensen aan boord

| Term | Match | Beste treffers | Opmerking |
|---|---|---|---|
| Bemanning | ja | bemanning (CHT) <https://data.cultureelerfgoed.nl/term/id/cht/f5da69b1-5658-41ea-ad8e-55a242554d30> |  |
| Chef d'équipage / schipper | deels | bootsman (Wikidata) <http://www.wikidata.org/entity/Q303486> | AAT *kapiteins* (300136377) is de koopvaardij-schipper: andere betekenis |
| Commandant | ja | commandant (Wikidata) <http://www.wikidata.org/entity/Q11247470> | alleen in Wikidata |
| Hofmeester | ja | hofmeester (Wikidata) <http://www.wikidata.org/entity/Q67201364> | Wikidata: voormalige positie bij de Nederlandse marine |
| korporaal-hofmeester, korporaal-stoker | nee | – | CHT heeft alleen korporaal bij landmacht en luchtmacht |
| Lichtmatroos | ja | lichtmatroos (Wikidata) <http://www.wikidata.org/entity/Q2685095> |  |
| Machinist | ja | scheepswerktuigkundige (Wikidata) <http://www.wikidata.org/entity/Q2177743> | AAT *machinisten* (300025271) en *scheepswerktuigkundigen* (300025083) gaan over bouwers en ontwerpers |
| hoofdmachinist | nee | – |  |
| Matroos | ja | matrozen (CHT) <https://data.cultureelerfgoed.nl/term/id/cht/e6f116bb-12ba-4590-9ee2-1f60c86f67b0><br>matrozen (AAT) <http://vocab.getty.edu/aat/300386642> |  |
| Navigateur | ja | navigators (AAT) <http://vocab.getty.edu/aat/300236294> | CHT *stuurlieden* is verwant |
| Officier | ja | officieren (AAT) <http://vocab.getty.edu/aat/300236210> | algemene term, niet specifiek marine |
| Privébediende | deels | bedienden (AAT) <http://vocab.getty.edu/aat/300025874> | bredere term |
| Scheepsarts | ja | scheepsarts (Wikidata) <http://www.wikidata.org/entity/Q325855> |  |
| Sergeant-kok | deels | koks (AAT) <http://vocab.getty.edu/aat/300248012><br>scheepskok (Wikidata) <http://www.wikidata.org/entity/Q133828630> | geen rang; IED *Kokki* is een kok in een Indisch huishouden |
| Stoker | nee | – | AAT en Wikidata hebben alleen stokers in metaalgieterijen en bij het spoor |

## Onderzoek op zee

| Term | Match | Beste treffers | Opmerking |
|---|---|---|---|
| Diepzee | ja | diepzee (Wikidata) <http://www.wikidata.org/entity/Q1070117> |  |
| Dreg | deels | dreggen (Wereldmuseum) <https://hdl.handle.net/20.500.11840/termmaster10070917> | omschrijving niet gecontroleerd; CHT *dregankers* is een anker, andere betekenis |
| Dynamometer | ja | dynamometers (AAT) <http://vocab.getty.edu/aat/300423894><br>dynamometer (Wikidata) <http://www.wikidata.org/entity/Q11223329> |  |
| Fuik | ja | fuiken (CHT) <https://data.cultureelerfgoed.nl/term/id/cht/b30e8521-d639-4dc2-ba21-cc82528e6cc6><br>fuiken (AAT) <http://vocab.getty.edu/aat/300263216> |  |
| diepzeefuik | nee | – |  |
| Hydrografie | ja | hydrografie (CHT) <https://data.cultureelerfgoed.nl/term/id/cht/f5940ec6-98be-4bb1-bcf9-4c0c7c2863e8><br>hydrografie (AAT) <http://vocab.getty.edu/aat/300054549> |  |
| hydrograaf | ja | hydrograven (CHT) <https://data.cultureelerfgoed.nl/term/id/cht/1b1400ca-bd35-46d3-a439-d04b34047f0c><br>hydrografen (AAT) <http://vocab.getty.edu/aat/300025805> |  |
| In kaart brengen / opnemen | deels | cartografie (CHT) <https://data.cultureelerfgoed.nl/term/id/cht/3cf2fa3e-555e-4887-9278-5d2f7a862d77><br>cartografie (AAT) <http://vocab.getty.edu/aat/300053163> | vakgebied, geen handeling |
| Kor | deels | korren (CHT) <https://data.cultureelerfgoed.nl/term/id/cht/85590fc6-a38b-42f8-80dc-13de56200856><br>boomkorren (CHT) <https://data.cultureelerfgoed.nl/term/id/cht/02d17c8f-805d-4d06-a75a-d2683a1a3453><br>sleepnetten (CHT) <https://data.cultureelerfgoed.nl/term/id/cht/aeb98d12-b7ff-4716-88ae-76dd59b556f9> | CHT *korren*: kustdialect voor sleepnet; *boomkorren* gaat over motorvissersschepen |
| korboom | nee | – |  |
| Laadboom | ja | laadbomen (CHT) <https://data.cultureelerfgoed.nl/term/id/cht/4b3e7ac9-48ee-4c36-b104-ee91db1e5a74><br>laadboom (Wikidata) <http://www.wikidata.org/entity/Q63209165> |  |
| Leefnet | ja | leefnetten (CHT) <https://data.cultureelerfgoed.nl/term/id/cht/bff8dad2-77a4-405a-8b85-f646fac89c47> |  |
| Loden / peillood | ja | dieploden (CHT) <https://data.cultureelerfgoed.nl/term/id/cht/ce18ad60-7c69-425e-99a2-fd726cb66c5d><br>peilloden (CHT) <https://data.cultureelerfgoed.nl/term/id/cht/df9dfe8e-a8fa-4746-9cf9-d4704005e6d9><br>dieplood (Wikidata) <http://www.wikidata.org/entity/Q1382947> | match op het voorwerp; het werkwoord *loden* zelf niet gevonden |
| lodingdraad, lodingtoestel | nee | – |  |
| Onderzeese rug | ja | onderzeese rug (Wikidata) <http://www.wikidata.org/entity/Q390395> |  |
| Plankton | ja | plankton (GTAA) <http://data.beeldengeluid.nl/gtaa/28948><br>plankton (Wikidata) <http://www.wikidata.org/entity/Q25367> | CHT heeft alleen fyto- en zoöplankton |
| Rif | ja | riffen (AAT) <http://vocab.getty.edu/aat/300008808><br>koraalriffen (AAT) <http://vocab.getty.edu/aat/300387631><br>koraalrif (Wikidata) <http://www.wikidata.org/entity/Q11292> |  |
| Rolstopper | nee | – |  |
| Station | nee | – | alleen treinstations en dergelijke |
| Veeraccumulator | nee | – |  |
| Waterschepper | nee | – |  |
| Zwenkboom | deels | zwaaiboom (Wikidata) <http://www.wikidata.org/entity/Q2256930> | het woordenboek linkt zelf naar Zwaaiboom; of dat hetzelfde is, niet gecontroleerd |

## Biologie en collecties

| Term | Match | Beste treffers | Opmerking |
|---|---|---|---|
| Algen | ja | algen (AAT) <http://vocab.getty.edu/aat/300265695><br>algen (GTAA) <http://data.beeldengeluid.nl/gtaa/25343> |  |
| algoloog | ja | algenkundige (Wikidata) <http://www.wikidata.org/entity/Q12358881> | Wikidata heeft ook *fycologie* (Q188391) |
| Conserveren | deels | conserveren (materiaalbeheer) (AAT) <http://vocab.getty.edu/aat/300266154> | algemene term, niet specifiek natuurhistorisch |
| conservator | ja | conservators (CHT) <https://data.cultureelerfgoed.nl/term/id/cht/0971b9a5-4ca0-4f6d-b092-b7ee713d0e30><br>conservatoren (AAT) <http://vocab.getty.edu/aat/300025633> |  |
| det. | ja | determinatie (Wikidata) <http://www.wikidata.org/entity/Q2039217> |  |
| Geslacht | ja | geslacht (Wikidata) <http://www.wikidata.org/entity/Q34740> | AAT *geslachten* betekent families |
| Herbarium | ja | herbaria (documents) (AAT) <http://vocab.getty.edu/aat/300440768><br>herbarium (Wikidata) <http://www.wikidata.org/entity/Q181916> |  |
| leg. | nee | – | niet gezocht als afkorting |
| Siboga-reeks | deels | Siboga expeditie (Wikidata) <http://www.wikidata.org/entity/Q47059163> | Wikidata: 'Nederlandse publicatie'; nagaan of dit het reeks-item is |
| Soort | ja | soorten (CHT) <https://data.cultureelerfgoed.nl/term/id/cht/bc2ebab8-8160-44b4-9213-f0643207ae93><br>soort (Wikidata) <http://www.wikidata.org/entity/Q7432> |  |
| Specimen | ja | exemplaren (CHT) <https://data.cultureelerfgoed.nl/term/id/cht/5e745056-7911-444f-8e50-e4dcc71ee98f><br>specimens (AAT) <http://vocab.getty.edu/aat/300235576> | CHT: voorwerp in een natuurhistorische collectie |
| typespecimen | deels | holotype (Wikidata) <http://www.wikidata.org/entity/Q1061403> | smaller begrip |
| Wallace-lijn | ja | Wallacelijn (IED) <https://data.indischherinneringscentrum.nl/ied/113340><br>Wallacelijn (Wikidata) <http://www.wikidata.org/entity/Q210746> |  |
| Zoöloog | ja | zoölogen (AAT) <http://vocab.getty.edu/aat/300025792><br>zoöloog (Wikidata) <http://www.wikidata.org/entity/Q350979> |  |

## De koloniale tijd

| Term | Match | Beste treffers | Opmerking |
|---|---|---|---|
| Baboe | ja | Baboe (IED) <https://data.indischherinneringscentrum.nl/ied/110798> |  |
| Gamelan | ja | Gamelan (IED) <https://data.indischherinneringscentrum.nl/ied/110869><br>gamelans (AAT) <http://vocab.getty.edu/aat/300205068><br>gamelans (Wereldmuseum) <https://hdl.handle.net/20.500.11840/termmaster10068843> |  |
| Kolonie | ja | koloniën (CHT) <https://data.cultureelerfgoed.nl/term/id/cht/77ad3e7d-b770-4b2e-8090-36153f38546e><br>koloniën (AAT) <http://vocab.getty.edu/aat/300235115> |  |
| Moesson | ja | Moesson (IED) <https://data.indischherinneringscentrum.nl/ied/111849><br>moessons (AAT) <http://vocab.getty.edu/aat/300054742> |  |
| Pasanggrahan | ja | Pasanggrahan (IED) <https://data.indischherinneringscentrum.nl/ied/113658> |  |
| Radja | nee | – | IED *Radja* is een schip |
| Wajang | ja | Wayang (IED) <https://data.indischherinneringscentrum.nl/ied/104009><br>wajang (Wikidata) <http://www.wikidata.org/entity/Q1078316> | AAT *Wajang* (300107244) is een stijl |
