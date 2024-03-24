import configparser
import time
import sys
sys.path.append('../pages')
sys.path.append('../base')

from pages.home_page import HomePage
from base.base_test import BaseTest

config = configparser.ConfigParser()
config.read('settings.ini')


class TestPom(BaseTest):
    driver = config.get('WebDriverSettings', 'browser').lower()

    def test_pom(self):
        try:
            home_page = HomePage(self.driver)
            current_url = home_page.get_current_url()
            self.assertEqual(current_url, config.get('AssertionSettings', 'home_url'), 'URL is wrong, '
                                                                                       'you are not on the home page')
            home_page.click_reject_cookies()
            home_page.click_company_navbar_item()

            career_page = home_page.click_career_dropdown_item()
            current_url = home_page.get_current_url()
            self.assertEqual(current_url, config.get('AssertionSettings', 'career_url'), 'URL is wrong, '
                                                                                         'you are not on the career '
                                                                                         'page')
            career_page.scroll_to_locations_section()
            self.assertTrue(career_page.is_element_present(career_page.our_location_section))
            career_page.scroll_to_life_at_insider_section()
            self.assertTrue(career_page.is_element_present(career_page.life_at_insider_title))
            career_page.scroll_to_teams_section()
            self.assertTrue(career_page.is_element_present(career_page.teams_section))
            career_page.click_see_all_teams_button()

            qa_page = career_page.click_quality_assurance_role_button_and_navigate()
            current_url = qa_page.get_current_url()
            self.assertEqual(current_url, config.get('AssertionSettings', 'qa_url'), 'URL is wrong, '
                                                                                     'you are not on the QA job '
                                                                                     'description page')

            positions_page = qa_page.click_all_qa_jobs_btn()
            positions_page.click_location_filter()
            positions_page.select_istanbul_from_location_filter()
            positions_page.scroll_until_all_jobs_visible_on_page()
            self.assertTrue(positions_page.verify_filtered_results_match_with_selected_locations())
            self.assertTrue(positions_page.verify_filtered_results_match_with_selected_departments())

            form_page = positions_page.click_view_role_btn()
            self.assertTrue(form_page.is_element_present(form_page.apply_job_button))
            self.assertTrue(form_page.is_element_present(form_page.job_headline))
            test_status = "passed"
        except Exception:
            test_status = "failed"
            raise
        finally:
            self.take_screenshot(test_status)
