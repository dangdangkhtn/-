# Simple test script template

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time


# illustrator V0.2
# change: add param "sec" to control the duration of illustration
def illustrator(web_driver, element, sec):
    illus_style = "color:SeaShell;background: #D96459;outline-style: dashed;"
    old_style = element.get_attribute("style")
    web_driver.execute_script("arguments[0].setAttribute('style', arguments[1])", element, illus_style)
    time.sleep(sec)
    web_driver.execute_script("arguments[0].setAttribute('style', arguments[1])", element, old_style)

# Init -----------------------------------------------------------------------------------------------------
driver = webdriver.Firefox()
driver.maximize_window()
initPage = "http://truonghocdang.weebly.com"

# ----------------------------------------------------------------------------------------------------------
driver.get(initPage)