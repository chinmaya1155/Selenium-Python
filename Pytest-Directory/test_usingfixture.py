print("test framework 2 Test execution started")
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest
@pytest.fixture()
def test_setup():
    global driver
    # driver for Chrome
    driver = webdriver.Chrome(executable_path="C:/Users/chsah5/PycharmProjects/Drivers/chromedriver.exe")
    # driver for MS Edge
    #driver = webdriver.Edge(executable_path="C:/Users/chsah5/PycharmProjects/Drivers/MicrosoftWebDriver.exe")
    driver.implicitly_wait(10)
    yield
    driver.close()
    print("Test execution finishes")
def test_readdata(test_setup):
    driver.get("https://www.google.com/")
    print("URL is :" + driver.current_url)
    print("Page Title is: " + driver.title)
    pgtitle = driver.title
    assert pgtitle == 'Google'