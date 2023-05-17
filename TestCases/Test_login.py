import pytest
from selenium import webdriver
from PageObjects.Loginpage import Loginpage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info("********************* Test_001_Login ***********************")
        self.logger.info("*************** Verifying Home Page Title ******************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        if act_title=="Your store. Login":
            assert True
            self.logger.info("************** Home page title test is passed ********************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.logger.error("************** Home page title test is failed ********************")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("************** Verifying Login Test ********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=Loginpage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.logger.info("************** Login test is passed ********************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.logger.error("************** Login test is Failed ********************")
            self.driver.close()
            assert False




