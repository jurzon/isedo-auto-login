# Auto-Login Robot pre ISEDO (Lekárne)

Tento Python skript slúži na automatické prihlásenie do informačného systému ISEDO a okamžité nastavenie kurzora do políčka pre skenovanie e-receptov. Rieši problém s neustálym odhlasovaním a šetrí čas pri každodennej práci v lekárni.

## 🚀 Inštalácia

1. Stiahnite si tento repozitár do počítača.
2. Vytvorte si virtuálne prostredie a nainštalujte knižnicu Selenium:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   pip install selenium

3. Premenujte súbor config.example.json na config.json.

4. Otvorte config.json v textovom editore a vložte do neho svoje prihlasovacie meno a heslo pre portál ISEDO.

## Používanie
Pre Windows používateľov:
Stačí dvakrát kliknúť na súbor spusti_isedo.bat. Pre maximálne pohodlie si z tohto súboru môžete vytvoriť odkaz na Pracovnú plochu.

Po spustení sa automaticky otvorí prehliadač Google Chrome, prebehne prihlásenie a systém vás presmeruje priamo do sekcie "Tvorba objednávky", kde nastaví kurzor, aby ste mohli okamžite zadat cislo receptu.

