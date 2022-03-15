import pytest
from selenium import webdriver
from pageObject.loginPage import login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseUrl= ReadConfig.getApplicationURL()
    username= ReadConfig.getUserEmail()
    password= ReadConfig.getPassword()
#call the loggen method under LogGen class.It will return the logger object .
    logger= LogGen.loggen()

#test_method1
    def test_homePageLogin(self,setUp):

        self.logger.info("***********Test_001_Login********** ")
        self.logger.info("*********** Verifying Home Page Title********** ")

        self.driver = setUp                        # here for muliple driver calling in different methods is time consuming. what we did is to create a fixture method in conftest.py in where we declare a setup method and call them in driver calling everytime
        self.driver.get(self.baseUrl)              #access class variable uding self keyword
        actual_title= self.driver.title

#verification
        if actual_title == "Your store. Loginn":
            assert True
            self.driver.close()
            self.logger.info("***********  Home Page Title passed ********** ")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageLogin.png") # screenshot of failure
            self.driver.close()
            self.logger.error("***********  Home Page Title is failed ********** ")
            assert False


#test_method2
    def test_Login(self,setUp):

        self.logger.info("***********  Verifying Login test ********** ")

        self.driver = setUp
        self.driver.get(self.baseUrl)
        self.ll= login(self.driver)   #creating object of class login to invoke the action methods.
        self.ll.setUserName(self.username)  # here we use self keyword cause every variable is under this class
        self.ll.setPassword(self.password)
        self.ll.clickLogin()
        actual_title = self.driver.title

# verification
        if actual_title == "Dashboard / nopCommerce administration111":
            assert True
            self.logger.info("***********  Login test is passed ********** ")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Login.png")  # screenshot of failure
            self.driver.close()
            self.logger.error("***********  Login test  is failed ********** ")
            assert False






