# scroll down Ver 1 use script "element.scrollIntoView()", it's work well but not natural and slightly difficult -
# - to follow
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
initPage = "http://jqueryui.com/draggable/#default"

# ----------------------------------------------------------------------------------------------------------

driver.get(initPage)
element = \
    WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(".//*[@id='mCSB_3_container']/p[3]"))
driver.execute_script("arguments[0].scrollIntoView();", element)
illustrator(driver, element, 0.5)
print(element.text)
