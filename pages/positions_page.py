import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage
from pages.form_page import FormPage


class PositionsPage(BasePage):
    page_head_section = (By.ID, 'page-head')
    filter_location = (By.ID, 'select2-filter-by-location-container')
    filter_department = (By.ID, 'select2-filter-by-department-container')
    location_items = (By.CSS_SELECTOR, '#select2-filter-by-location-results li')
    # location_items[1] = Istanbul, Turkey
    result_departments = (By.CSS_SELECTOR, '#jobs-list div div span')
    result_locations = (By.CSS_SELECTOR, '#jobs-list div div div')
    view_role_button = (By.XPATH, '//a[text()="View Role"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_page_load()

    def wait_page_load(self):
        self.wait.until(EC.visibility_of_element_located(self.page_head_section))
        self.wait.until(EC.visibility_of_element_located(self.filter_location))
        self.wait.until(EC.text_to_be_present_in_element(self.filter_department, "Quality Assurance"))
        # department kismi sayfa acildiktan birkac saniye sonra otomatik olarak Quality Assurance oluyor ve
        # bu eventten sonra locations kismi erisilebilir oluyor, bundan dolayi quality assurance olana kadar beklemesi
        # icin expected condition ekledim.

    def click_location_filter(self):
        self.driver.find_element(*self.filter_location).click()

    def select_istanbul_from_location_filter(self):
        self.wait.until(EC.visibility_of_all_elements_located(self.location_items))
        self.driver.find_elements(*self.location_items)[1].click()

    def scroll_until_all_jobs_visible_on_page(self):
        self.driver.execute_script("window.scrollBy(0, 700);")
        time.sleep(1)
        # secilen lokasyondaki islerin gelmesi birkac saniye surdugu icin time sleep

    def verify_filtered_results_match_with_selected_locations(self):
        # ilgili sonuç 4 adet çıkmaktadır
        # element sayısı kadar dönüp hepsi quality assurance iceriyorsa true donduren method
        # duplicate oldugunu fark ettim ama clean code'a nasil cevirecegime dair bir yontem dusunemedim
        elements = self.driver.find_elements(*self.result_locations)
        element_count = len(elements)
        job_locations = []
        completed = False
        count = 0

        for i in range(element_count):
            element = self.driver.find_elements(*self.result_locations)[i]
            job_locations.append(element.text)

        # prints the locations
        for i in range(element_count):
            print(job_locations[i])

        for i in range(element_count):
            if job_locations[i] == 'Istanbul, Turkey':
                count += 1

        if count == element_count:
            completed = True

        return completed

    def verify_filtered_results_match_with_selected_departments(self):
        # element sayısı kadar dönüp hepsi quality assurance iceriyorsa true donduren method
        # duplicate oldugunu fark ettim ama clean code'a nasil cevirecegime dair bir yontem dusunemedim
        elements = self.driver.find_elements(*self.result_departments)
        element_count = len(elements)
        department_names = []
        completed = False
        count = 0

        for i in range(element_count):
            element = self.driver.find_elements(*self.result_departments)[i]
            department_names.append(element.text)

        for i in range(element_count):
            print(department_names[i])

        for i in range(element_count):
            if department_names[i] == 'Quality Assurance':
                count += 1

        if count == element_count:
            completed = True

        return completed

    def click_view_role_btn(self):
        # yeni sekmede acildigi icin tikladiktan sonra mevcut sekmede elementleri bulup islem yapabilmek istiyorum
        main_window_handle = self.driver.current_window_handle
        self.driver.find_element(*self.view_role_button).click()
        all_window_handles = self.driver.window_handles

        # Yeni sekmenin tanımlayıcısını bul
        new_window_definer = None
        for window_definer in all_window_handles:
            if window_definer != main_window_handle:
                new_window_definer = window_definer
                break

        # Yeni sekmenin penceresine geçiş yap
        self.driver.switch_to.window(new_window_definer)
        return FormPage(self.driver)
