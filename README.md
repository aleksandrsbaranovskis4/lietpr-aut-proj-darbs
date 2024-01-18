# Lietojumprogrammatūras automatizēšanas rīku projekta darbs
## ORTUS e-studiju vides gaidāmo notikimumu skrāpēšana
### Projekta uzdevums
Projekta uzdevums bija izveidot programmu, kas ar Selenium bibliotēkas palīdzību automātiski ierakstīsies ORTUSa profilā izmantojot lietotājvārdu un paroli, kas ir saglabātas `info.env` failā, ***kurš netiek commitots GitHub repozotorijā drošības un privātumu nolūkos.***
### Izmantotās Python bibliotēkas
1. **Selenium**- ši bibliotēka tiek izmantota, lai varētu ievadīt lietotājvārdu un paroli ORTUSa pierakstīšanās mājaslapā, tad pierakstīties un no mājaslapas HTML koda izvilkt informāciju uzdevumus un to termiņus no gaidāmo notikumu infopaneļa. Šī bibliotēka galvenokārt tiek izmantota `calnderScrape()` funkcijā;
2. **openpyxl**- šī bibliotēka tiek izmantota, lai
