from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
baseurl= "https://www.bigotires.com/store-locator"
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get(baseurl)

search_element = driver.find_element(By.ID, 'find_address_by_zip_code-CityStateorZipode-searchMask-BOTStoreLocatorSearchMain')
search_element.send_keys('Alaska')
time.sleep(3)
autocomplete = driver.find_element(By.ID, 'react-autowhatever-1--item-0')
name = autocomplete.text
autocomplete.click()
search = driver.find_element(By.XPATH, "//div[@class='sc-4sha46-3 gAddBd']//button[@class='sc-1khk1ow-0 sc-1khk1ow-1 sc-746azs-2 kdKCXV']")
search.click()
all_locations = driver.find_elements(By.XPATH,"//ul[@class='sc-2us082-0 irXysU']/li")
count = len(all_locations)
print("Number of stores in " + name + " are :" + str(count))
#adress
address = driver.find_elements(By.XPATH, "//h2[@class='sc-2tswuk-0-h2 dxmkcl']/span[1]")
address_list = []
for a in address:
    address_list.append(a.text)
#City
city = driver.find_elements(By.XPATH, "//h2[@class='sc-2tswuk-0-h2 dxmkcl']/span[2]")
city_list = []
for a in city:
    city_list.append(a.text)
# Phone Numbers
mobile = driver.find_elements(By.XPATH, "//span[@class='sc-2tswuk-0 ddwnZa']")
mobile_list = []
for a in mobile:
    mobile_list.append(a.text)
driver.close()

Data = pd.DataFrame(list(zip(address_list,city_list,mobile_list)), columns=('Address','City&ZipCode','Mobile'))
print(Data)


