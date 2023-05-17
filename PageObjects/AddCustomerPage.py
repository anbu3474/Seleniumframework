import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class AddCustomer:
    # Add customer Page
    lnkMenu_xpath = "//*[@id='nopSideBarPusher']/i"
    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddnew_xpath = "//a[@class='btn btn-primary']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    #drpselectcustomerRole = "//select[@id='SelectedCustomerRoleIds']"
    txtcustomerRoles_xpath = "//*[@id='customer-info']/div[2]/div[10]/div[2]/div/div[1]/div/div"
    lstitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    lstitemforumModerators_xpath = "//li[contains(text(),'Forum Moderators')]"
    lstitemGuests_xpath = "//li[contains(text(),'Guests')]"
    lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"
    drpmgrOfVendor_xpath = "//*[@id='VendorId']"
    rdMaleGender_id = "Gender_Male"
    rdFeMaleGender_id = "Gender_Female"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnMenu(self):
        self.driver.find_element(By.XPATH, self.lnkMenu_xpath).click()

    def clickOnCustomersMenu(self):
        self.customermenu = self.driver.find_element(By.XPATH, self.lnkCustomers_menu_xpath)
        self.driver.execute_script("arguments[0].click();", self.customermenu)

    def clickOnCustomersMenuItem(self):
        self.customermenuitem = self.driver.find_element(By.XPATH, self.lnkCustomers_menuitem_xpath)
        self.driver.execute_script("arguments[0].click();", self.customermenuitem)

    def clickOnAddnew(self):
        self.driver.find_element(By.XPATH, self.btnAddnew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.txtPassword_xpath).send_keys(password)

    def setCustomerRoles(self, role):
        self.driver.find_element(By.XPATH, self.txtcustomerRoles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemRegistered_xpath)
        elif role == 'Vendor':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemVendors_xpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemAdministrators_xpath)
        elif role == 'Forum Moderators':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemforumModerators_xpath)
        elif role == 'Guests':
            # Here user can be Registered( or) Guest, only one
            time.sleep(3)
            self.driver.find_element(By.XPATH, "//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
        elif role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemRegistered_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemVendors_xpath)
        elif role == 'ForumModerators':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemforumModerators_xpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemAdministrators_xpath)
        else:
            self.listitem = self.driver.find_element_by_xpath(self.lstitemGuests_xpath)
        time.sleep(3)
        # self.listitem.click()
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element(By.XPATH, self.drpmgrOfVendor_xpath))
        drp.select_by_visible_text(value)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()
        elif gender == 'Female':
            self.driver.find_element(By.ID, self.rdFeMaleGender_id).click()
        else:
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()

    def setFirstName(self, fname):
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.XPATH, self.txtLastName_xpath).send_keys(lname)

    def setDob(self, dob):
        self.driver.find_element(By.XPATH, self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self, comname):
        self.driver.find_element(By.XPATH, self.txtCompanyName_xpath).send_keys(comname)

    def setAdminContent(self, content):
        self.driver.find_element(By.XPATH, self.txtAdminContent_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()


