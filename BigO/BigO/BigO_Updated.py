from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
from Location import Location

baseurl= "https://www.bigotires.com/store-locator"
#intiliase driver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get(baseurl)
# Read Us_States file
data = pd.read_excel('Us_States.xlsx')
send_location = data.values.tolist()
# Created an object for class Location
getlocation = Location(driver)
# Created a empty DataFrame
df_Database = pd.DataFrame(columns=('Address', 'City&ZipCode', 'Mobile'))
# Empty list of error_states
error_cities_list=[]
# Loop to traverse all the states in the get_location function
for a in send_location:
    data = getlocation.get_location(a)
    if data is not None:
        frames = [df_Database, data]
        df_Database = pd.concat(frames, ignore_index= True)
    else:
        error_cities_list.append(a)
    driver.get(baseurl)
# export to excel
writer = pd.ExcelWriter('BigO_Stores.xlsx', engine='xlsxwriter')
df_error_cities = pd.DataFrame(error_cities_list, columns=['States Which Results Error'])
df_Database.to_excel(writer,sheet_name='Stores_Data')
df_error_cities.to_excel(writer,sheet_name='Error_States')
writer.save()
driver.quit()


