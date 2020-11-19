from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
desired_cap = {
 'browserName': 'iPhone',
 'device': 'iPhone 11',
 'realMobile': 'true',
 'os_version': '14.0',
 'name': 'BStack-[Python] Sample Test', # test name
 'build': 'BStack Build Number 1' # CI/CD job or build name
}
driver = webdriver.Remote(
    command_executor='https://divyanksingh1:CNnn3B4jqfsEFKbcJYyp@hub-cloud.browserstack.com/wd/hub',
    desired_capabilities=desired_cap)
driver.get("https://www.google.com")
if not "Google" in driver.title:
    raise Exception("Unable to load google page!")
elem = driver.find_element_by_name("q")
elem.send_keys("BrowserStack")
elem.submit()
print(driver.title)
driver.quit() 
