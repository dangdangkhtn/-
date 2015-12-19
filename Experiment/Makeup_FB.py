from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time


# illustrator V0.1
def illustrator(web_driver, element):
    illus_style = "color:SeaShell;background: #D96459;outline-style: dashed;"
    old_style = element.get_attribute("style");
    web_driver.execute_script("arguments[0].setAttribute('style', arguments[1])", element, illus_style)
    time.sleep(0.2)
    web_driver.execute_script("arguments[0].setAttribute('style', arguments[1])", element, old_style)

# Init -----------------------------------------------------------------------------------------------------
driver = webdriver.Firefox()
driver.maximize_window()

# ----------------------------------------------------------------------------------------------------------

driver.get("https://www.facebook.com")
emailFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("email"))
emailFieldElement.clear()
illustrator(driver, emailFieldElement)
emailFieldElement.send_keys("dangdanghpe@gmail.com")



loginButtonElement = \
    WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("loginbutton"))
illustrator(driver, loginButtonElement)
loginButtonElement.click()

# ----------------------------------------------------------------------------------------------------------
