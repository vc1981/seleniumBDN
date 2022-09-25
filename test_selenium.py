import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

@pytest.mark.usefixtures("setup")
class TestSelenium:
    def test_01(self):
        self.driver.get("https://www.selenium.dev/selenium/web/web-form.html")
        self.driver.implicitly_wait(5)

        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(5)

        self.driver.execute_script("window.scrollTo(0,0)")
        time.sleep(5)

        my_text = WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((By.NAME, "my-text"))
        )
        my_text.send_keys("Happy Testing")
        time.sleep(5)

        my_password = WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((By.NAME, "my-password"))
        )
        my_password.send_keys("very_secret_password")

        my_textarea = WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((By.NAME, "my-textarea"))
        )
        my_textarea.send_keys("Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean et est a dui semper facilisis. Pellentesque placerat elit a nunc. Nullam tortor odio, rutrum quis, egestas ut, posuere sed, felis. Vestibulum placerat feugiat nisl. Suspendisse lacinia, odio non feugiat vestibulum, sem erat blandit metus, ac nonummy magna odio pharetra felis. Vivamus vehicula velit non metus faucibus auctor. Nam sed augue. Donec orci. Cras eget diam et dolor dapibus sollicitudin. In lacinia, tellus vitae laoreet ultrices, lectus ligula dictum dui, eget condimentum velit dui vitae ante. Nulla nonummy augue nec pede. Pellentesque ut nulla. Donec at libero. Pellentesque at nisl ac nisi fermentum viverra. Praesent odio. Phasellus tincidunt diam ut ipsum. Donec eget est.")
        time.sleep(5)

        select_element = self.driver.find_element(By.NAME, "my-select")
        select_object = Select(select_element)
        select_object.select_by_visible_text('Two')
        time.sleep(5)

        my_datalist = WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((By.NAME, "my-datalist"))
        )
        action = ActionChains(self.driver).move_to_element(my_datalist)
        action.perform()
        time.sleep(5)
        action.click(on_element=my_datalist)
        action.perform()
        time.sleep(5)

        my_datalist.send_keys("Los Angeles")
        time.sleep(5)

        my_date = WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((By.NAME, "my-date"))
        )
        my_date.click()
        time.sleep(5)
        my_date.send_keys("09/30/2022")
        time.sleep(5)

        submit_button = self.driver.find_element(by=By.CSS_SELECTOR, value="button")
        submit_button.click()
        message = self.driver.find_element(by=By.ID, value="message")
        value = message.text
        assert value == "Received!"



        # self.driver.execute_script("arguments[0].scrollIntoView(true);", element);



