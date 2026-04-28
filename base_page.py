import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from config.config import EXPLICIT_WAIT, SCREENSHOT_DIR


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait   = WebDriverWait(driver, EXPLICIT_WAIT)


    def wait_for_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def is_element_present(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False


    def click(self, locator):
        el = self.wait_for_clickable(locator)
        el.click()
        return el

    def type_text(self, locator, text):
        el = self.wait_for_visible(locator)
        el.clear()
        el.send_keys(text)

    def get_text(self, locator):
        return self.wait_for_visible(locator).text.strip()

    def scroll_to(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)
        time.sleep(0.4)

    def js_click(self, element):
        """Fallback click via JavaScript for stubborn elements."""
        self.driver.execute_script("arguments[0].click();", element)

   

    def take_screenshot(self, name):
        os.makedirs(SCREENSHOT_DIR, exist_ok=True)
        path = os.path.join(SCREENSHOT_DIR, f"{name}.png")
        self.driver.save_screenshot(path)
        return path
