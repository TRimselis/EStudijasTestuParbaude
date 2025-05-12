# RTU eStudijas Uzdevumu Termiņu Apstrādes Projekts

## Projekta uzdevums

Šī Python skripta mērķis ir automatizēti iegūt un apstrādāt RTU eStudijas platformas uzdevumu termiņus, pieslēdzoties lietotāja kontam, iegūstot attiecīgos datus un parādot tos konsolē ar norādi par katra uzdevuma atlikušajām dienām, stundām un minūtēm līdz tā izpildes termiņam.

Risinājums noderīgs studentiem, kuri vēlas ātri pārskatīt visus tuvojošos darbus un termiņus, nepieslēdzoties manuāli platformai.

---

## Izmantotās Python bibliotēkas

Projektā tiek izmantotas šādas bibliotēkas:

- `selenium`: 
  - Automātiskai tīmekļa pārlūkprogrammas vadībai (Google Chrome) un autentifikācijai RTU sistēmā.
  - Nepieciešama, jo RTU eStudijas platformai ir pieslēgšanās mehānisms ar JavaScript, kuru nevar pārvarēt ar vienkāršiem HTTP pieprasījumiem.

- `datetime`: 
  - Lai apstrādātu termiņu datumus un aprēķinātu, cik laika atlicis līdz uzdevuma termiņam.
---

## Izmantotās datu struktūras

Projekta ietvaros tika definēta un izmantota lietotāja definēta datu struktūra – **masīvs**:

```python
results = []
