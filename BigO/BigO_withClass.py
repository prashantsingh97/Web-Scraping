from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
from Location import Location
baseurl= "https://www.bigotires.com/store-locator"
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get(baseurl)
send_location = ['San Diego','Alaska']
getlocation = Location(driver)
for a in send_location:
    data = getlocation.get_location(a)
    if data is not None:
        print(data)
        driver.execute_script("window.location.href = 'https://www.bigotires.com/store-locator;'")
driver.quit()


