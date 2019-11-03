from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common import keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

from bin.ClassesLib import *

driver = webdriver.Chrome('bin\\chromedriver.exe')


class ListCount(object):
    select: Select

    def __init__(self, select_):
        self.select = select_

    def __call__(self, d):
        try:

            return len(self.select.options) > 1
        except StaleElementReferenceException as e:
            print(str(e))
            return False


def login():
    try:
        driver.get("http://cabinet.yi.uz")
        driver.find_element_by_id("loginform-username").send_keys("margilon_sh")
        driver.find_element_by_id("loginform-password").send_keys("NazoratM2018")
        driver.find_element_by_id("loginform-password").submit()
    except NoSuchElementException:
        print("     !!! Internet tarmog'iga ulanishni ilojini topa olmadim !!!      ")


def __fill_from(youth: Youth):
    driver.find_element_by_id("members-firstname").send_keys(youth.name)
    driver.find_element_by_id("members-lastname").send_keys(youth.lastName)
    driver.find_element_by_id('members-surname').send_keys(youth.surname)
    driver.implicitly_wait(200)
    driver.set_script_timeout(100)

    __select("members-gender", youth.gender)

    driver.find_element_by_id("members-birthday").send_keys(youth.birthday)

    driver.implicitly_wait(200)
    driver.set_script_timeout(100)
    __select("members-crime", "0")

    __select("members-type_document", youth.document_type, True)

    driver.find_element_by_id("members-series").send_keys(youth.series)
    driver.find_element_by_id("members-number").send_keys(youth.number)

    __select("members-region_id", youth.region, True)

    driver.implicitly_wait(200)
    __select("members-district_id", youth.tuman, True)
    __select("members-gathering_id", youth.mahalla, True)

    driver.find_element_by_id("members-address").send_keys(youth.address)

    driver.find_element_by_id("members-phone").send_keys(str(youth.phone))


def addPupil(pupil: Pupil):
    pupil.check()
    if not pupil.success:
        error = open(ERROR_FILE_PATH, "a")
        error.write(pupil.json())
        error.close()
        return

    try:
        driver.get("http://cabinet.yi.uz/members/create")

        __fill_from(pupil)

        __select("members-type_member", pupil.pupil_type)

        __select("members-org_region_id", pupil.school_region, True)
        __select("members-org_district_id", pupil.school_tuman, True)
        __select("member-organization_id", pupil.school_id, True)
        __select("members-course", pupil.course)

        driver.find_element_by_id("members-phone").submit()

        driver.get("http://cabinet.yi.uz")
    except NoSuchElementException:
        print("     !!! Internet tarmog'iga ulanishni ilojini topa olmadim !!!      ")

    file = open("success.txt", 'a')
    file.write(pupil.json() + "\n")
    file.close()


def addTeenager(teenage: Teenager):
    teenage.check()
    if not teenage.success:
        error = open(ERROR_FILE_PATH, "a")
        error.write(teenage.json())
        error.close()
        return

    try:
        driver.get("http://cabinet.yi.uz/members/create")

        __fill_from(teenage)

        __select("members-type_member", teenage.status)
        driver.find_element_by_id("members-type_members").send_keys(keys.Keys.TAB).send_keys(teenage.info)

        driver.find_element_by_id("members-phone").submit()

        driver.get("http://cabinet.yi.uz")
    except NoSuchElementException:
        print("     !!! Internet tarmog'iga ulanishni ilojini topa olmadim !!!      ")

    file = open("success.txt", 'a')
    file.write(teenage.json() + "\n")
    file.close()


def close():
    driver.close()


def __select(element_id, value, wait: bool = False):
    if wait:
        WebDriverWait(driver, 10).until(
            ListCount(Select(driver.find_element_by_id(element_id)))
        )
    Select(driver.find_element_by_id(element_id)).select_by_value(value)
