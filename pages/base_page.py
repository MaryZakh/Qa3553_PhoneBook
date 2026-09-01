import time

from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self,driver):
        self.driver = driver

    def find(self, locator, timeout=5):
        deadline = time.time() + timeout
        last_error = None

        while time.time() < deadline:
            try:
                return self.driver.find_element(*locator)
            except (NoSuchElementException, StaleElementReferenceException) as exc:
                last_error = exc
                time.sleep(0.2)

        raise last_error

    def click(self, locator):
        element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))
        element.click()

    def fill(self, locator, value):
        element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(value)

    def get_alert_text(self):
        alert = WebDriverWait(self.driver,timeout=5).until(
            EC.alert_is_present()
        )

        return alert.text

    def accept_alert(self):
        self.driver.switch_to.alert.accept()