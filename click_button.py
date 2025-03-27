from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def click_claim_button():
    # Run Chrome in headless mode (no visible browser)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # Change the path to match your environment if you run locally
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # 1) Go to your site
        driver.get("https://magichour.ai")  # <-- Replace with the actual URL

        # 2) Wait if necessary for the page to load (adjust time as needed)
        time.sleep(5)

        # 3) Locate the "Claim" button by text and click it
        claim_button = driver.find_element(
            By.XPATH, "//button[normalize-space(text())='Claim']"
        )
        claim_button.click()

        # 4) Possibly wait a bit so any subsequent server action completes
        time.sleep(3)

    finally:
        driver.quit()

if __name__ == "__main__":
    click_claim_button()
