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


    username_input = driver.find_element(By.ID, 'username')
    password_input = driver.find_element(By.ID, 'password')
    login_button = driver.find_element(By.CSS_SELECTOR, '.login-button')

    username_input.send_keys('zeks')
    password_input.send_keys('12345678')
    time.sleep(1)
    login_button.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href*="create_exhibition"]'))
    )

    create_exhibition_link = driver.find_element(By.CSS_SELECTOR, 'a[href*="create_exhibition"]')
    create_exhibition_link.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'ime'))
    )

    # Popuni informacije o izložbi
    ime_input = driver.find_element(By.ID, 'ime')
    opis_input = driver.find_element(By.ID, 'opis')

    ime_input.send_keys('Ime1')
    opis_input.send_keys('Opis1')
    time.sleep(1)

    driver.execute_script("window.scrollBy(0, 600);")

    time.sleep(2)

    slike = driver.find_elements(By.CLASS_NAME, "nfts")
    for i in range(3):
        slike[i].click()
        time.sleep(1)

    time.sleep(1)
    # Kreiraj izložbu
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(4)

    kreiraj_izlozbu_button = driver.find_element(By.ID, 'btn1')
    kreiraj_izlozbu_button.click()

    # Sačekaj da se prikaže alert o uspešnom kreiranju izložbe
    time.sleep(3)

    # Provera da li je izložba uspešno kreirana
    try:
        alert = driver.switch_to.alert
        assert alert.text == 'Izložba je uspešno kreirana sa selektovanim slikama!'
        alert.accept()
        print('Test create exhibition: passed')
    except Exception as e:
        print('Test create exhibition: failed')

finally:
    time.sleep(2)
    logout_link = driver.find_element(By.CSS_SELECTOR, 'a[href*="logout"]')
    logout_link.click()

    driver.quit()