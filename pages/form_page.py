from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage


class FormPage(BasePage):
    apply_job_button = (By.CSS_SELECTOR, '.postings-btn-wrapper a')
    job_headline = (By.CSS_SELECTOR, 'div[class="posting-headline"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_page_load()

    def wait_page_load(self):
        self.wait.until(EC.visibility_of_element_located(self.apply_job_button))
        self.wait.until(EC.visibility_of_element_located(self.job_headline))
