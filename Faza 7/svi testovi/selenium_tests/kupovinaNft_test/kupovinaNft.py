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

username = driver.find_element(By.ID,"username")
username.send_keys("zeks")
password = driver.find_element(By.ID,"password")
password.send_keys("12345678")
driver.find_element(By.ID, "register-button").click()
driver.get("http://127.0.0.1:8000/nft/nft_review/69")

element = driver.find_element(By.ID, "kupi")

driver.execute_script("arguments[0].scrollIntoView();", element)
driver.execute_script("arguments[0].click();", element)
wait = WebDriverWait(driver, timeout=2)
alert = wait.until(lambda d : d.switch_to.alert)
text = alert.text
if(text == "Uspesno ste kupili NFT!"):
    print("passed")
else:
    print("failed")
alert.accept()

