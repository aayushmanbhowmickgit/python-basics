from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Letter to be typed automatically
a=str(input("Enter a text to be typed automatically: "))
# Open Chrome
driver = webdriver.Chrome()
driver.get("https://www.google.com")
time.sleep(2)

# Open a text box using Google's search box as an example
search_box = driver.find_element(By.NAME, "q")

# Automatically type the letter
search_box.send_keys(a)

time.sleep(5)
driver.quit()
