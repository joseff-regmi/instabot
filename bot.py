from selenium import webdriver
import os 
import time
from config import us, pw


class InstagramBot():

    def __init__(self, username, password):

        self.driver = webdriver.Edge('msedgedriver.exe')

        
        self.driver.get("https://www.instagram.com/accounts/login/")
        
        time.sleep(3)

        self.driver.find_element_by_xpath("//input[@name=\'username\']").send_keys(username)


        self.driver.find_element_by_xpath("//input[@name=\'password\']").send_keys(password)


        self.driver.find_element_by_xpath("//button[@Type=\'submit\']").click()

        


if __name__ == "__main__":
    ig_bot = InstagramBot(us, pw)
