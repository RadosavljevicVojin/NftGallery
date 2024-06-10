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


    # Otvori stranicu za prijavljivanje
    driver.get("http://localhost:8000/")
    driver.maximize_window()

    login_button = driver.find_element(By.ID, "prijavi-se")
    login_button.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )

    # Popunjavanje forme za prijavu
    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.CSS_SELECTOR, '.login-button')

    username_input.send_keys('admin')
    password_input.send_keys('123')
    login_button.click()

    # Sačekaj da se stranica učita
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "search-input"))
    )

    # Pretraga korisnika
    search_input = driver.find_element(By.ID, 'search-input')
    search_button = driver.find_element(By.CSS_SELECTOR, '.search-btn')

    search_input.send_keys('tmptmp')
    time.sleep(1)
    search_button.click()

    # Sačekaj da se profil korisnika učita
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#deleteForm button'))
    )

    # Klikni na dugme za brisanje korisnika
    delete_button = driver.find_element(By.CSS_SELECTOR, '#deleteForm button')
    delete_button.click()
    time.sleep(1)

    # Potvrdi brisanje korisnika u alertu
    alert = driver.switch_to.alert
    alert.accept()

    # Sačekaj da se prikaže alert o uspešnom brisanju
    time.sleep(2)

    # Provera da li je korisnik uspešno obrisan
    try:
        alert = driver.switch_to.alert
        assert alert.text == 'Uspešno ste obrisali korisnika'
        alert.accept()
        print("Test delete user: passed")
    except Exception as e:
        print("Test delete user: failed")

finally:# Logout
    logout_link = driver.find_element(By.CSS_SELECTOR, 'a[href*="logout"]')
    logout_link.click()
    time.sleep(2)

    # Zatvori pretraživač
    driver.quit()