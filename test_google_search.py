import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from parameterized import parameterized

testing_list = ['Donkeys', 'Elephants', 'Dogs', 'Rats', 'Chickens']

@pytest.mark.usefixtures("setup")
class TestSelenium:
    def test_01(self):
        self.driver.get("https://www.google.com/")
        self.driver.save_screenshot("shot.png")
        assert self.driver.title == "Google"
        accept_cookie = WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((By.ID, "L2AGLb"))
        ).click()


    @parameterized.expand(testing_list)
    def test_02_search_for(self, search_text):
        self.driver.get("https://www.google.com")
        search_field = WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((By.NAME, "q"))
        )
        search_field.send_keys(search_text)
        search_field.send_keys("\n")

        time.sleep(10)