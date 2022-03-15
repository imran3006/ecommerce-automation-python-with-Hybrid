class login:
#identifying all the locators
    textbook_username_id = "Email"
    textbook_password_id = "Password"
    button_login_xpath= "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button"
    Link_logout_linktext= "Logout"


#iniatialized driver using construtor

    def __init__(self,driver):
        self.driver = driver

#action methoda

    def setUserName(self, username):
        self.driver.find_element_by_id(self.textbook_username_id).clear()
        self.driver.find_element_by_id(self.textbook_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.textbook_password_id).clear()
        self.driver.find_element_by_id(self.textbook_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_xpath(self.Link_logout_linktext).click()