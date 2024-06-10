import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

print("Starting script execution...")

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)


print("Navigating to http://127.0.0.1:8000")
driver.get("http://127.0.0.1:8000")

time.sleep(5)

username_input = driver.find_element(By.ID, "search-input")
username_input.send_keys("LeaderOfHorde")

search_button = driver.find_element(By.CSS_SELECTOR, "button.search-btn")
search_button.click()

# Wait for the page to load after the search
time.sleep(5)

# Print page source for debugging
print(driver.page_source)

try:
    username_input = driver.find_element(By.ID, "search-input")
    print("Found username input field.")
    username_input.send_keys("LeaderOfHorde")
    print("Entered username.")
except Exception as e:
    print(f"Failed to find or interact with username input field: {e}")
    driver.quit()
    exit()

try:
    search_button = driver.find_element(By.CSS_SELECTOR, "button.search-btn")
    print("Found search button.")
    search_button.click()
    print("Clicked search button.")
except Exception as e:
    print(f"Failed to find or click search button: {e}")
    driver.quit()
    exit()

# Wait for the page to load after the search
time.sleep(5)

try:
    portfolio_tab = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'portfolio'))
    )
    print("Found portfolio tab.")
    portfolio_tab.click()
    print("Clicked portfolio tab.")
except Exception as e:
    print(f"Test portfolio_view failed: Could not find or click portfolio tab. Error: {e}")
    driver.quit()
    exit()

try:
    ukupna_vrednost_header = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//header[contains(text(), 'Ukupna vrednost portfolia:')]"))
    )
    print("Test portfolio_view passed: Found header 'Ukupna vrednost portfolia:'.")
except Exception as e:
    print(f"Test portfolio_view failed: Could not find header 'Ukupna vrednost portfolia:'. Error: {e}")

# Zatvaranje drivera
driver.quit()
