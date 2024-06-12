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


username_input = driver.find_element(By.ID, "search-input")
username_input.send_keys("LeaderOfHorde")

search_button = driver.find_element(By.CSS_SELECTOR, "button.search-btn")
search_button.click()
time.sleep(3)
try:
    portfolio_tab = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'portfolio'))
    )

    driver.execute_script("arguments[0].onclick()", portfolio_tab)

    try:
        ukupna_vrednost_header = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//header[contains(text(), 'Ukupna vrednost portfolia:')]"))
        )
        print("Test portfolio_view passed.")
    except Exception as e:
        print("Test portfolio_view failed.")
except Exception as e:
    print("Test portfolio_view failed.")


driver.quit()


