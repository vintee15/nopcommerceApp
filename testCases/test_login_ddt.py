import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLutilotis

class Test_002_DDT_Login:

    # these are common variables & data is hardcoded
    # baseURL = "https://admin-demo.nopcommerce.com/"
    # username= "admin@yourstore.com"
    # password="admin"

    # reading value from config file
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()


    def test_login(self, setup):
         self.logger.info(" ******* Test_002_DDT_Login ******************")
         self.logger.info(" ******* verify login test *******")
         self.driver = setup

         self.driver.get(self.baseURL)
         self.lp = LoginPage(self.driver)
         self.lp.setUserName(self.username)
         self.lp.setPassword(self.password)
         self.lp.clickLogin()
         act_title = self.driver.title
         # self.driver.close()

         if act_title== "Dashboard / nopCommerce administration":
             assert  True
             self.logger.info(" ******* login test is passed *******")
         else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            # self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.logger.info(" ******* home page title is failed*******")
            assert False







