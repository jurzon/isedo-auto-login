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
        
        # Meno - kliknúť a potom písať
        user_field = wait.until(EC.element_to_be_clickable((By.ID, "UserName_I")))
        user_field.click() # Pridané kliknutie pre istotu
        user_field.clear()
        user_field.send_keys(MENO)
        
        # Heslo - DevExpress trik s kliknutím na atrapu
        wait.until(EC.element_to_be_clickable((By.ID, "Password_I_CLND"))).click()
        
        # Vloženie hesla do skutočného poľa
        pass_field = wait.until(EC.presence_of_element_located((By.ID, "Password_I")))
        pass_field.click() # Pridané kliknutie
        pass_field.send_keys(HESLO)
        
        # Klik na prihlásiť
        time.sleep(1) # Malá pauza pred kliknutím na odoslanie
        wait.until(EC.element_to_be_clickable((By.ID, "SignInButton"))).click()

        # KROK 2: Prechod na "Tvorba objednávky"
        # Dôležité: Čakáme, kým sa objaví menu po prihlásení
        print("Čakám na hlavné menu...")
        menu_tvorba = wait.until(EC.element_to_be_clickable((By.ID, "applicationMenu_DXI1_T")))
        menu_tvorba.click()

        # KROK 3: Aktivácia políčka pre recept
        time.sleep(2) #
        
        print("Aktivujem políčko pre recept...")
        policko_recept = wait.until(EC.element_to_be_clickable((By.ID, "numberEdit_I")))
        policko_recept.click()
        policko_recept.clear() # Pridané: vymaže políčko pred skenovaním

        print("HOTOVO! Môžete skenovať.")

    except Exception as e:
        print(f"Chyba: {e}")
        # Prehliadač nezavrieme, nech vidíte, kde robot skončil
        input("Stlačte Enter pre zatvorenie...")
        driver.quit()

if __name__ == "__main__":
    prihlas_a_priprav_objednavku()