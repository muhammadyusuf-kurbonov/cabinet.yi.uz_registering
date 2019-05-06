import selenium.webdriver
import selenium.webdriver.support.ui
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.select import Select


class listCount(object):
    select: Select

    def __init__(self, select_):
        self.select = select_

    def __call__(self, driver):
        try:

            return len(self.select.options) > 1
        except StaleElementReferenceException:
            return False


driver = selenium.webdriver.Chrome()

Select(driver.find_element_by_id("members-region_id")).select_by_value('12')
driver.implicitly_wait(200)
select = Select(driver.find_element_by_id("members-district_id"))
selenium.webdriver.support.ui.WebDriverWait(driver, 10).until(
    listCount(select)
)
for tuman in select.options:
    select._setSelected(tuman)
    mahalla = Select(driver.find_element_by_id("members-gathering_id"))
    selenium.webdriver.support.ui.WebDriverWait(driver, 10).until(
        listCount(mahalla)
    )
    for m in mahalla.options:

        print(m)