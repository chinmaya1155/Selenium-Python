*** settings ***
Library  Selenium2Library
*** Test Cases ***
To test open browser
    [documentation]  Browser testing only
    [tags]  regression

    Open Browser  http://newtours.demoaut.com  Chrome
    Close Browser
