from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
from Location import Location
import itertools
from joblib import Parallel, delayed

baseurl= "https://www.bigotires.com/store-locator"
#intiliase driver
driver = webdriver.Chrome()
driver.implicitly_wait(1)
driver.get(baseurl)
# Read Us_ZipCodes file
data = pd.read_excel('Zipcode.xlsx')

send_location = data['Zip_Codes']

# Created an object for class Location
getlocation = Location(driver)

# Created a empty DataFrame
df_Database = pd.DataFrame(columns=('Address', 'City&ZipCode', 'Mobile'))
# Empty list of error_states
# error_cities_list=[]
list_cycle = itertools.cycle(send_location)
# Loop to traverse all the zip_Codes in the get_location function
for a in range(len(send_location)):
    data = getlocation.get_location(next(list_cycle))
    df_Database = df_Database.append(data , ignore_index=True)
    df_Database.drop_duplicates('Address', keep='first',inplace=True)
    print(df_Database)
    driver.get(baseurl)

# export to excel
writer = pd.ExcelWriter('BigO_Stores_ZipCodes.xlsx', engine='xlsxwriter')
df_Database.to_excel(writer,sheet_name='Stores_Data')
writer.save()
driver.quit()

