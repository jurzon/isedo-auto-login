from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import sys

# --- NAČÍTANIE ÚDAJOV Z CONFIGU ---
try:
    with open('config.json', 'r', encoding='utf-8') as f:
        config = json.load(f)
        MENO = config['MENO']
        HESLO = config['HESLO']
except FileNotFoundError:
    print("Chyba: Súbor config.json chýba. Vytvorte ho podľa súboru config.example.json")
    sys.exit(1)
# ----------------------------------

def prihlas_a_priprav_objednavku():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    
    print("1. Otváram prehliadač...")
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.isedo.sk/signin")
    driver.maximize_window()

    try:
        wait = WebDriverWait(driver, 10)

        print("2. Zadávam prihlasovacie údaje...")
        wait.until(EC.element_to_be_clickable((By.ID, "UserName_I"))).send_keys(MENO)
        wait.until(EC.element_to_be_clickable((By.ID, "Password_I_CLND"))).click()
        wait.until(EC.presence_of_element_located((By.ID, "Password_I"))).send_keys(HESLO)
        wait.until(EC.element_to_be_clickable((By.ID, "SignInButton"))).click()

        print("3. Presúvam sa do sekcie 'Tvorba objednávky'...")
        menu_tvorba = wait.until(EC.element_to_be_clickable((By.ID, "applicationMenu_DXI1_T")))
        menu_tvorba.click()

        print("4. Nastavujem kurzor pre čiarový kód...")
        policko_recept = wait.until(EC.element_to_be_clickable((By.ID, "numberEdit_I")))
        policko_recept.click()

        print("Hotovo! Systém je pripravený na skenovanie alebo písanie.")

    except Exception as e:
        print(f"Chyba pri automatizácii: {e}")

if __name__ == "__main__":
    prihlas_a_priprav_objednavku()