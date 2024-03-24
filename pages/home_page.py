import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage
from pages.career_page import CareerPage


class HomePage(BasePage):
    reject_cookie_btn = (By.ID, 'wt-cli-reject-btn')
    header_locator = (By.ID, 'announce')
    navbar_dropdown = (By.ID, 'navbarNavDropdown')
    navbar_items = (By.ID, 'navbarDropdownMenuLink')  # we will select 5th (index = 4)
    careers_dropdownSub = (By.XPATH, '//a[text()="Careers"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_page_load()

    def wait_page_load(self):
        self.wait.until(EC.visibility_of_element_located(self.header_locator))
        self.wait.until(EC.visibility_of_element_located(self.navbar_dropdown))
        time.sleep(2)

    def click_reject_cookies(self):
        self.driver.find_element(*self.reject_cookie_btn).click()

    def click_company_navbar_item(self):
        self.driver.find_elements(*self.navbar_items)[4].click()

    def click_career_dropdown_item(self):
        self.wait.until(EC.visibility_of_element_located(self.careers_dropdownSub))
        self.driver.find_element(*self.careers_dropdownSub).click()
        return CareerPage(self.driver)
