import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:

    # these are common variables & data is hardcoded
    # baseURL = "https://admin-demo.nopcommerce.com/"
    # username= "admin@yourstore.com"
    # password="admin"

    # reading value from config file
    baseURL = ReadConfig.getApplicationURL()
    username= ReadConfig.getUsername()
    password=ReadConfig.getPassword()

    logger = LogGen.loggen()



    def test_homePageTitle(self, setup):
        # inside this method create driver

        self.logger.info(" ******* Test_001_Login *******")
        self.logger.info(" ******* verifying home page title *******")
        self.driver=setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        # if act_title != "nopCommerce demo store. Login":
        #     self.driver.save_screenshot(".\\Screenshots\\test_homePageTitle.png")
        # self.logger.info(" ******* home page title is failed *******")
        # assert act_title == "nopCommerce demo store. Login1", f"Expected title did not match. Got: {act_title}"
        # self.logger.info(" ******* home page title is passed *******")
        # self.driver.close()

        if act_title == "nopCommerce demo store. Login121122":
            self.logger.info(" ******* home page title is passed *******")
            assert True

        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.logger.info(" ******* home page title is failed *******")

            assert False

    def test_login(self, setup):
         self.driver = setup
         self.logger.info(" ******* verify login test *******")
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







