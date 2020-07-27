print("test framework 2 Test execution started")
from selenium import webdriver
import pytest
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.keys import Keys

@allure.severity(allure.severity_level.NORMAL)
def test_logocheck():
    global driver
    # driver for Chrome
    driver = webdriver.Chrome(executable_path="C:/Users/chsah5/PycharmProjects/Drivers/chromedriver.exe")
    # driver for MS Edge
    #driver = webdriver.Edge(executable_path="C:/Users/chsah5/PycharmProjects/Drivers/MicrosoftWebDriver.exe")
    driver.implicitly_wait(10)
    driver.get("https://opensource-demo.orangehrmlive.com/")
    logo = driver.find_element_by_xpath("// *[ @ id = 'divLogo'] / img").is_displayed()
    if logo==True:
        assert True
    else:
        assert False

@allure.severity(allure.severity_level.CRITICAL)
def test_login():
    driver.get("https://opensource-demo.orangehrmlive.com/")
    print("URL is :" + driver.current_url)
    print("Page Title is: " + driver.title)
    driver.find_element_by_id("txtUsername").send_keys("Admin")
    driver.find_element_by_id("txtPassword").send_keys("admin123")
    driver.find_element_by_id("btnLogin").click()
    title_pg = driver.title
    if title_pg=="OrangeHRM123":
        assert True
    else:
        allure.attach(driver.get_screenshot_as_png(), name="Login Screen error",
                      attachment_type=AttachmentType.PNG)
        assert False

@allure.severity(allure.severity_level.MINOR)
def test_skipping():
    pytest.skip("SKIPPING the test intentionally")

@allure.severity(allure.severity_level.NORMAL)
def test_closing():
    driver.close()
    print("Test execution finishes")