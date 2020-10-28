import selenium.webdriver.support.ui
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.select import Select

import Pupil

driver = webdriver.Chrome()


class listCount(object):
    select: Select

    def __init__(self, select_):
        self.select = select_

    def __call__(self, driver):
        try:

            return len(self.select.options) > 1
        except StaleElementReferenceException as e:
            print(str(e))
            return False


def login():
    driver.get("http://cabinet.yi.uz")
    driver.find_element_by_id("loginform-username").send_keys("margilon_sh")
    driver.find_element_by_id("loginform-password").send_keys("NazoratM2018")
    driver.find_element_by_id("loginform-password").submit()


def add(pupil: Pupil):
    pupil.check()
    if not pupil.success:
        return

    driver.get("http://cabinet.yi.uz/members/create")
    driver.find_element_by_id("members-firstname").send_keys(pupil.name)
    driver.find_element_by_id("members-lastname").send_keys(pupil.lastName)
    driver.find_element_by_id('members-surname').send_keys(pupil.surname)
    driver.implicitly_wait(200)
    driver.set_script_timeout(100)
    Select(driver.find_element_by_id("members-gender")).select_by_value(pupil.gender)
    driver.find_element_by_id("members-birthday").send_keys(pupil.birthday)

    Select(driver.find_element_by_id("members-type_member")).select_by_value(pupil.pupil_type)

    selenium.webdriver.support.ui.WebDriverWait(driver, 10).until(
        listCount(Select(driver.find_element_by_id("members-org_region_id")))
        , "No district")
    Select(driver.find_element_by_id("members-org_region_id")).select_by_value(pupil.school_region)
    selenium.webdriver.support.ui.WebDriverWait(driver, 10).until(
        listCount(Select(driver.find_element_by_id("members-org_district_id")))
        , "No district")
    Select(driver.find_element_by_id("members-org_district_id")).select_by_value(pupil.school_tuman)
    selenium.webdriver.support.ui.WebDriverWait(driver, 10).until(
        listCount(Select(driver.find_element_by_id("members-organization_id")))
    )
    Select(driver.find_element_by_id("members-organization_id")).select_by_value(pupil.school_id)
    Select(driver.find_element_by_id("members-course")).select_by_value(pupil.course)
    driver.implicitly_wait(200)
    driver.set_script_timeout(100)
    Select(driver.find_element_by_id("members-crime")).select_by_value('0')

    selenium.webdriver.support.ui.WebDriverWait(driver, 10).until(
        listCount(Select(driver.find_element_by_id("members-type_document")))
    )
    Select(driver.find_element_by_id("members-type_document")).select_by_value(pupil.document_type)
    driver.find_element_by_id("members-series").send_keys(pupil.series)
    driver.find_element_by_id("members-number").send_keys(pupil.number)
    selenium.webdriver.support.ui.WebDriverWait(driver, 10).until(
        listCount(Select(driver.find_element_by_id("members-region_id")))
    )
    Select(driver.find_element_by_id("members-region_id")).select_by_value(pupil.region)
    driver.implicitly_wait(200)
    selenium.webdriver.support.ui.WebDriverWait(driver, 10).until(
        listCount(Select(driver.find_element_by_id("members-district_id")))
    )
    Select(driver.find_element_by_id("members-district_id")).select_by_value(pupil.tuman)
    selenium.webdriver.support.ui.WebDriverWait(driver, 15).until(
        listCount(Select(driver.find_element_by_id("members-gathering_id")))
    )
    Select(driver.find_element_by_id("members-gathering_id")).select_by_value(pupil.mahalla)
    driver.find_element_by_id("members-address").send_keys(pupil.address)

    driver.find_element_by_id("members-phone").send_keys(str(pupil.phone))
    driver.find_element_by_id("members-phone").submit()

    driver.get("http://cabinet.yi.uz")

    print("success $(pupil.name)" + pupil.name)


def close():
    driver.close()
