from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

baseurl= "https://www.lesschwab.com/can-i-get-my-oil-changed-at-les-schwab"
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get(baseurl)
Result = pd.DataFrame(columns=('Address', 'City&ZipCode', 'Mobile'))
for i in range(1,99):
    a = str('(//small//a[@title = "Store Details"])' + str([i]))
    WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.CSS_SELECTOR, "span.taLnk.ulBlueLinks")))
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, a))))
    time.sleep(1)
    # address
    address = driver.find_elements(By.XPATH,"//div[@class = 'storeDetails storeDetails--full grid-x']//address//span[1]")
    address_list = []
    for a in address:
        address_list.append(a.text)
    # City
    city = driver.find_elements(By.XPATH,"//div[@class = 'storeDetails storeDetails--full grid-x']//address//span[2]")
    city_list = []
    for a in city:
        city_list.append(a.text)
    # Phone Numbers
    mobile = driver.find_elements(By.XPATH, "//ul[@class = 'storeDetails__contact']//li[1]")
    mobile_list = []
    for a in mobile:
        mobile_list.append(a.text)
    Data_list = list(zip(address_list, city_list, mobile_list))
    if Data_list is not None:
        Data = pd.DataFrame(Data_list, columns=('Address', 'City&ZipCode', 'Mobile'))
    Result = Result.append(Data,ignore_index=True)
    print(Result)
    driver.get(baseurl)
    # driver.execute_script("window.history.go(-1)")

Result.to_excel('Lesschwab_Stores.xlsx',sheet_name='Stores_Data')
driver.close()
