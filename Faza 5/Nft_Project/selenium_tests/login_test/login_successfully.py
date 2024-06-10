import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Podešavanje WebDriver-a

chrome_driver_path = "C:\\Program Files\\chromedriver-win64\\chromedriver.exe"

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ChromeService(chrome_driver_path),options=options)

try:

    driver.get("http://localhost:8000/")
    driver.maximize_window()

    login_button = driver.find_element(By.ID, "prijavi-se")
    login_button.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )

    # Popunjavanje forme za prijavu
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")

    username_field.send_keys("zeks")  # Zameni sa korisničkim imenom za test
    time.sleep(1)
    password_field.send_keys("12345678")  # Zameni sa šifrom za test
    time.sleep(1)

    # Klik na dugme za prijavu
    submit_button = driver.find_element(By.ID, "register-button")
    submit_button.click()

    # Čekanje da se učita početna stranica nakon prijave
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "moj-profil"))
    )

    # Provera da li je korisnik ulogovan tako što ćemo potražiti dugme "Moj profil"
    try:
        profile_button = driver.find_element(By.ID, "moj-profil")

        time.sleep(1)

        # Klik na dugme "Odjavi se"
        logout_button = driver.find_element(By.ID, "odjavi-se")
        logout_button.click()

        time.sleep(1)

        # Čekanje da se učita početna stranica nakon odjave
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "prijavi-se"))
        )
        print("Test login successfully: passed")
    except:
        print("Test login successfully: failed")
finally:
    # Zatvaranje WebDriver-a
    driver.quit()