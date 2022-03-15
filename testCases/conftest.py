import pytest
from selenium import webdriver

#whenever  call the setUp method it will return the driver in test_login page/ or in every test method
@pytest.fixture()
def setUp():
    driver =webdriver.Chrome()
    return driver
