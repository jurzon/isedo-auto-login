@echo off
echo Startujem ISEDO Robota...

:: Tento prikaz zabezpeci, ze skript sa spusti v spravnej zlozke
cd /d "%~dp0"

:: Aktivacia virtualneho prostredia a spustenie skriptu
call .venv\Scripts\activate
python isedo_login.py

:: Ak by sa okno hned zavrelo (napr. kvoli chybe), toto ho podrzi otvorene
pause