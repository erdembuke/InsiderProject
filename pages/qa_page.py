from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage
from pages.positions_page import PositionsPage


class QaPage(BasePage):
    see_jobs_button = (By.XPATH, '//a[text()="See all QA jobs"]')
    qa_title = (By.CSS_SELECTOR, '#page-head h1')

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_page_load()

    def wait_page_load(self):
        self.wait.until(EC.visibility_of_element_located(self.see_jobs_button))
        self.wait.until(EC.visibility_of_element_located(self.qa_title))

    def click_all_qa_jobs_btn(self):
        self.driver.find_element(*self.see_jobs_button).click()
        return PositionsPage(self.driver)
