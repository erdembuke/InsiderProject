from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object): #facade class

    def __init__(self, driver, explicit_wait=30):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, explicit_wait)

    def is_element_present(self, locator):
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_current_url(self):
        return self.driver.current_url
