from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
baseurl= "https://www.bigotires.com/store-locator"
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get(baseurl)
# data = pd.read_excel('/Users/Prashant/Downloads/Us_States.xlsx')
send_location = ['KY']

search_element = driver.find_element(By.ID, 'find_address_by_zip_code-CityStateorZipode-searchMask-BOTStoreLocatorSearchMain')
search_element.send_keys(send_location)
time.sleep(3)
autocomplete = driver.find_element(By.ID, 'react-autowhatever-1--item-0')
name = autocomplete.text
autocomplete.click()
search = driver.find_element(By.XPATH, "//div[@class='sc-4sha46-3 gAddBd']//button[@class='sc-1khk1ow-0 sc-1khk1ow-1 sc-746azs-2 kdKCXV']")
search.click()
try:
    error = driver.find_element(By.XPATH, "//span[@class='sc-2tswuk-0 sc-746azs-6 kaDmc']")
except:
    change_radius = driver.find_element(By.XPATH, "//ul[@class = 'fa5pyj-1 cjBjZa']//a[contains(text(),'100')]")
    change_radius.click()
    time.sleep(2)
    all_locations = driver.find_elements(By.XPATH,"//ul[@class='sc-2us082-0 irXysU']/li")
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
    print("No Stores in the City/State/Zipcode " + str(send_location))
    Data_list = list(zip(address_list,city_list,mobile_list))
    Data = pd.DataFrame(Data_list, columns=('Address','City&ZipCode','Mobile'))
    print(Data)
driver.close()