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

    username_field.send_keys("Nepostojece_ime")  # Zameni sa korisničkim imenom za test
    time.sleep(1)
    password_field.send_keys("losa_lozinka")  # Zameni sa šifrom za test
    time.sleep(1)

    # Klik na dugme za prijavu
    submit_button = driver.find_element(By.ID, "register-button")
    submit_button.click()

    try:
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'messages')))
        error_message = driver.find_element(By.CLASS_NAME, 'messages').text
        print("Test login unsuccessfully: passed")
    except Exception as e:
        print("Test login unsuccessfully: failed")
finally:
    driver.quit()