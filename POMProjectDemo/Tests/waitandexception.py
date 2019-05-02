# Example to describe explicit and implicit waits , AJAX CALLS and handling common selenium exceptions
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

# Create a new chromedriver instance
# Go to www.google.com
driver = webdriver.Chrome(executable_path='C:/Users/Allah/Desktop/Pythan/Projects/FirstSeleniumTest/Drivers/chromedriver.exe')
driver.get("http://www.google.com")
driver.implicitly_wait(5)
try:
    # Wait as long as required, or maximum of 5 sec for element to appear
    # If successful, retrieves the element
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.NAME, "q")))
    #
    print("load search bar at www.google.com")

    # Type "selenium"
    element.send_keys("selenium")

    # Type Enter
    element.send_keys(Keys.ENTER)

except H:
    print("Failed to load search bar at www.google.com")
except TimeoutException:
    print("The object not found. Time Exceeded to locate the Web Element")
finally:
    driver.quit()

