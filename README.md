# Lietojumprogrammatūras automatizēšanas rīku projekta darbs
## ORTUS e-studiju vides gaidāmo notikimumu skrāpēšana
### Projekta uzdevums
Projekta uzdevums bija izveidot programmu, kas ar Selenium bibliotēkas palīdzību automātiski ierakstīsies ORTUSa profilā izmantojot lietotājvārdu un paroli, kas ir saglabātas `info.env` failā, ***kurš netiek commitots GitHub repozotorijā drošības un privātumu nolūkos.***
### Izmantotās Python bibliotēkas
1. **Selenium**- ši bibliotēka tiek izmantota, lai varētu ievadīt lietotājvārdu un paroli ORTUSa pierakstīšanās mājaslapā, tad pierakstīties un no mājaslapas HTML koda izvilkt informāciju uzdevumus un to termiņus no gaidāmo notikumu infopaneļa. Šī bibliotēka galvenokārt tiek izmantota `calendarScrape()` funkcijā;
2. **openpyxl**- šī bibliotēka tiek izmantota, lai izveidotu Excel tabulu, kurā tiks sablabāts uzdevums, termiņa datums un atlikušais laiks līdz termiņa beigām, vai ja termiņs ir beidzies, tad paziņotu to ar *Past due*. Tā arī tiks izmantota tabulas formatēšanai, lai automātiski visi šūnu izmēri būtu atbilstoši un visa informācija būtu saredzama bez vajadzības manuāli visu mainīt. Bibliotēka galvenokārt tiek izmantota `tableGen()` funkcijā;
3. **datetime**- šī bibliotēka tiek izmantota, lai datumus un laikus, kas tika izvilkti no ORTUs pārveidotu '%d.%m.%Y %H:%M' formātā, gan lai tie būtu uzskatāmāki, gan lai pēc tam Excel tabulā varētu veikt iepriekš minētos datuma aprēķinus atlikušā laika aprēķināšanai. Šī bibliotēka galvenokārt tiek izmantota `eventTime()` funkcijā;
4. **dotenv**- šī bibliotēka tiek izmantota, lai piekļūtu pie un pēc vajadzības izmainītu mainīgos, kuri mūsu gadījumā ir ORTUS lietotājvārds un parole, kas atrodas `info.env()` failā. Šī bibliotēka tiek izmantota `calendarScrape()` un `updateKeys()` funkcijās;
5. **getpass**- šī bibliotēka tiek izmantota, lai konsolē noslēptu ORTUS paroles ievadi, ja ir nepieciešamība to nomainīt. Šī bilbiotēka tiek izmantota `updateKeys()` funkcijā;
6. **time**- šī bibliotēka tiek izmatota, lai programma veiktu dažas īsas pauzes **Selenium** automātiskās programmas laikā, lai programmā nerastos kļūdas no tā, ka programma strādā ātrāk nekā tīmeklis spēj ielādēties. Šī bibliotēka tiek izmantota `calendarScrape()` funkcijā;
7. **os**- šī bibliotēka tiek izmantota, lai piekļūtu un mainītu vides mainīgos, kas atrodas pašā programmā. Šī bibliotēka tiek izmantota `calendarScrape()` un `updateKeys()` funkcijās.
### Programmatūras izmantošanas metodes
Programma tiek izmantota, lai varētu uzzināt visus gaidāmos uzdevumus, projektus, testus utt. un to termiņus bez vajadzības pašam katru reizi manuāli ierakstīties ORTUSā, kas var aizņemt kādu laiku. Tā kā programma ir pilnīgā automātiska, tad lielāko daļu gadījumu pašam manuāli ievadīt neko nevajag. Viena lieta, kas lietotājām manuāli ir jāizveido `info.env` fails, kurā atrodas šādi mainīgie:
```
USER='ORTUS lietotājvārds'
PASS='ORUTS parole'
```