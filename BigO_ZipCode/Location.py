from selenium.webdriver.common.by import By
import time
import pandas as pd

class Location(object):
    def __init__(self, driver):
        self.driver = driver
    def get_location(self,location):
        search_element = self.driver.find_element(By.ID,'find_address_by_zip_code-CityStateorZipode-searchMask-BOTStoreLocatorSearchMain')
        search_element.send_keys(location)
        search = self.driver.find_element(By.XPATH,"//div[@class='sc-4sha46-3 gAddBd']//button[@class='sc-1khk1ow-0 sc-1khk1ow-1 sc-746azs-2 kdKCXV']")
        search.click()
        try:
            # all_locations = self.driver.find_elements(By.XPATH, "//ul[@class='sc-2us082-0 irXysU']/li")
            change_radius = self.driver.find_element(By.XPATH, "//ul[@class = 'fa5pyj-1 cjBjZa']//a[contains(text(),'15')]")
            change_radius.click()
            time.sleep(1)
            # address
            address = self.driver.find_elements(By.XPATH, "//h2[@class='sc-2tswuk-0-h2 dxmkcl']/span[1]")
            address_list = []
            for a in address:
                address_list.append(a.text)
            # City
            city = self.driver.find_elements(By.XPATH, "//h2[@class='sc-2tswuk-0-h2 dxmkcl']/span[2]")
            city_list = []
            for a in city:
                city_list.append(a.text)
            # Phone Numbers
            mobile = self.driver.find_elements(By.XPATH, "//span[@class='sc-2tswuk-0 ddwnZa']")
            mobile_list = []
            for a in mobile:
                mobile_list.append(a.text)
            Data_list = list(zip(address_list, city_list, mobile_list))
            # print(Data_list)
            if Data_list is not None:
                Data = pd.DataFrame(Data_list, columns=('Address', 'City&ZipCode', 'Mobile'))
                # df_Database = pd.DataFrame(columns=('Address', 'City&ZipCode', 'Mobile'))
                return Data
        except:
             return