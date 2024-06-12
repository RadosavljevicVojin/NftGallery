from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)


driver.get("http://127.0.0.1:8000/accounts/login")
driver.maximize_window()

username = driver.find_element(By.ID,"username")
username.send_keys("zeks")
password = driver.find_element(By.ID,"password")
password.send_keys("12345678")
driver.find_element(By.ID, "register-button").click()

element = driver.find_element(By.ID, "moj-profil")

element.click()

element = driver.find_element(By.ID, "izmeni")
element.click()
staraSifra = driver.find_element(By.ID,"stara-lozinka")
staraSifra.send_keys("12345678")
novaSifra = driver.find_element(By.ID,"nova-lozinka")
novaSifra.send_keys("12345678")
potvrdaSifra = driver.find_element(By.ID,"potvrda-lozinke")
potvrdaSifra.send_keys("12345678")
element = driver.find_element(By.ID,"azuriraj")
driver.execute_script("arguments[0].scrollIntoView();", element)
driver.execute_script("arguments[0].click();", element)
try:
    element = driver.find_element(By.ID,"poruka")
    print("passed")
except Exception as e:
    print("failed")

