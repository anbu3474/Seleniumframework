import time
import pytest
from PageObjects.Loginpage import Loginpage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from Utilities import ExcelUtils


class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("*************** Test_002_DDT_Login ***********************")
        self.logger.info("*************** Verifying Login DDT Test ********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Loginpage(self.driver)

        self.rows = ExcelUtils.getRowCount(self.path, 'Sheet1')
        print("Number of Rows in the Excel : ", self.rows)
        list_status = []  # Empty list variable
        for r in range(2, self.rows+1):
            self.user = ExcelUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = ExcelUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = ExcelUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                   self.logger.info("*************** Login test is Passed ********************")
                   self.lp.clickLogout()
                   list_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("*************** Login test is Failed ********************")
                    self.lp.clickLogout()
                    list_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("*************** Login test is Failed ********************")
                    list_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("*************** Login test is Passed ********************")
                    list_status.append("Pass")

        if "Fail" not in list_status:
            self.logger.info("*************** Login DDT test Passed *****************")
            self.driver.close()
            assert True
        else:
            self.logger.info("*************** Login DDT test Failed *****************")
            self.driver.close()
            assert False

        self.logger.info("*************** End of Login DDT Test *******************")
        self.logger.info("*************** Completed Test_002_DDT_Login **************")
