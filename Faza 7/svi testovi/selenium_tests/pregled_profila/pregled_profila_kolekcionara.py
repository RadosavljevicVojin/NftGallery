import time

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

driver.get("http://127.0.0.1:8000")

time.sleep(5)

username_input = driver.find_element(By.ID, "search-input")
username_input.send_keys("margo")

search_button = driver.find_element(By.CSS_SELECTOR, "button.search-btn")
search_button.click()

try:
    izlozbe_tab = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'exhibitions'))
    )

    try:
        portfolio_tab = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'portfolio'))
        )
        print("Test collector_profile_view failed.")
    except:
        print("Test collector_profile_view passed.")

except:
    print("Test collector_profile_view failed.")


driver.quit()


