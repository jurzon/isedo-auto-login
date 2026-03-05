from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import sys
import time

# --- NAČÍTANIE ÚDAJOV Z CONFIGU ---
try:
    with open('config.json', 'r', encoding='utf-8') as f:
        config = json.load(f)
        MENO = config['MENO']
        HESLO = config['HESLO']
except FileNotFoundError:
    print("CHYBA: Súbor config.json neexistuje. Vytvorte ho!")
    sys.exit(1)

def prihlas_a_priprav_objednavku():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    
    print("Spúšťam prehliadač...")
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.isedo.sk/signin")
    driver.maximize_window()

    try:
        wait = WebDriverWait(driver, 15) # Predĺžený čas na 15s

        # KROK 1: Prihlásenie
        print("Prihlasujem sa...")
        wait.until(EC.element_to_be_clickable((By.ID, "UserName_I"))).send_keys(MENO)
        
        # Kliknutie na atrapu hesla aby sa zobrazil input
        wait.until(EC.element_to_be_clickable((By.ID, "Password_I_CLND"))).click()
        
        # Vloženie hesla
        wait.until(EC.presence_of_element_located((By.ID, "Password_I"))).send_keys(HESLO)
        
        # Klik na prihlásiť
        wait.until(EC.element_to_be_clickable((By.ID, "SignInButton"))).click()

        # KROK 2: Prechod na "Tvorba objednávky"
        # Dôležité: Čakáme, kým sa objaví menu po prihlásení
        print("Čakám na hlavné menu...")
        menu_tvorba = wait.until(EC.element_to_be_clickable((By.ID, "applicationMenu_DXI1_T")))
        menu_tvorba.click()

        # KROK 3: Nastavenie kurzora
        # Dáme stránke 2 sekundy pauzu, nech sa prekreslí (ochrana proti session error)
        time.sleep(2) 
        
        print("Aktivujem políčko pre recept...")
        policko_recept = wait.until(EC.element_to_be_clickable((By.ID, "numberEdit_I")))
        policko_recept.click()

        print("HOTOVO! Môžete skenovať.")

    except Exception as e:
        print(f"Chyba: {e}")
        # Prehliadač nezavrieme, nech vidíte, kde robot skončil
        input("Stlačte Enter pre zatvorenie...")
        driver.quit()

if __name__ == "__main__":
    prihlas_a_priprav_objednavku()