from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import schedule


def scrapy_scrapers():
    driver = webdriver.Chrome()

    wait = WebDriverWait(driver, 10)
    # Open the URL
    driver.get("https://www.gebiz.gov.sg/ptn/opportunity/BOListing.xhtml?origin=opportunities")

    totalbtns = driver.find_elements(By.CLASS_NAME, 'formRepeatPagination2_NAVIGATION-BUTTON')
    # print("buttons are: ", totalbtns)
    print('\n')
    print('\n')

    for i in range(len(totalbtns)-4): 
        time.sleep(3)  # Increase this if content loads slowly

        # Re-fetch elements (after AJAX pagination)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "commandLink_TITLE-BLUE")))
       
        page_items = driver.find_elements(By.CLASS_NAME, "commandLink_TITLE-BLUE")

        # Print the updated page content

        for item in page_items:
            print(item.text, "-", item.get_attribute("href"))

        print("\n" + "-"*50 + "\n")
        
        next_button = driver.find_elements(By.CLASS_NAME, 'formRepeatPagination2_NAVIGATION-BUTTON')[-2]
        if(next_button.is_enabled):
            # print("Enabled")
        # Click the button if next button is enabled
            next_button.click()
        
        # Wait for the new content to load


    driver.quit()

schedule.every(1).minutes.do(scrapy_scrapers)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)  