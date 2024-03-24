import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage
from pages.qa_page import QaPage


class CareerPage(BasePage):
    page_head_section = (By.ID, 'page-head')
    our_location_section = (By.ID, 'career-our-location')
    life_at_insider_title = (By.XPATH, '//h2[text()="Life at Insider"]')  # this section does not have an id
    teams_section = (By.ID, 'career-find-our-calling')
    see_all_teams_button = (By.XPATH, '//a[text()="See all teams"]')
    quality_assurance_role = (By.XPATH, '//h3[text()="Quality Assurance"]')
    role_images = (By.CSS_SELECTOR, '.w-100')

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_page_load()

    def wait_page_load(self):
        self.wait.until(EC.visibility_of_element_located(self.page_head_section))

    def scroll_to_locations_section(self):
        self.scroll_to_element(self.driver.find_element(*self.our_location_section))
        time.sleep(1)
        self.wait.until(EC.visibility_of_element_located(self.our_location_section))

    def scroll_to_life_at_insider_section(self):
        self.scroll_to_element(self.driver.find_element(*self.life_at_insider_title))
        time.sleep(1)
        self.wait.until(EC.visibility_of_element_located(self.life_at_insider_title))

    def scroll_to_teams_section(self):
        self.scroll_to_element(self.driver.find_element(*self.teams_section))
        time.sleep(1)
        self.wait.until(EC.visibility_of_element_located(self.teams_section))

    def click_see_all_teams_button(self):
        self.driver.execute_script("window.scrollBy(0, 700);")
        time.sleep(1)
        # scroll_to_element methodunu kullandigimda cookie'leri kapatmama ragmen
        # ClickInterception error veriyordu tiklanmiyordu, bunu cozmek icin
        # elementin clickable olabilecegi kadar asagi kaydirdim ve tiklama gerceklestirdim
        # time sleep koymazsam tam scrollamadan tiklamaya calisiyor ve exception aliyorum
        self.driver.find_element(*self.see_all_teams_button).click()
        time.sleep(2)

    def click_quality_assurance_role_button_and_navigate(self):
        # 12nd img quality assurance pozisyonunun img'i. öncesinde direkt quality_assurance_role elementine scroll
        # etmeye çalıştığım için bazen element yukarıda kalıyordu ve test case fail oluyordu. Bu durum cok sık
        # yasandigi icin (1pass-1fail gibi) img'e scrollayıp sonrasında qa'ya tiklayip sayfaya yonlendim
        self.scroll_to_element(self.driver.find_elements(*self.role_images)[10])
        time.sleep(1)
        # ayni sekilde time sleep koymazsam kaydirma bitmeden tiklamaya calisiyor
        # ve exception aliyorum, bundan dolayi 1 saniyelik time sleep burda da mevcut
        self.driver.find_element(*self.quality_assurance_role).click()
        return QaPage(self.driver)
