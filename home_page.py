import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.config import AMAZON_URL


class HomePage(BasePage):

    SEARCH_BOX    = (By.ID, "twotabsearchtextbox")
    SEARCH_BUTTON = (By.ID, "nav-search-submit-button")

    POPUPS = [
        (By.CSS_SELECTOR, '[data-action="a-modal-close"]'),
        (By.CSS_SELECTOR, ".a-popover-closebutton"),
        (By.XPATH,        "//button[contains(text(),'Dismiss')]"),
        (By.XPATH,        "//button[contains(text(),'Continue')]"),
        (By.ID,           "attach-close_sideSheet-link"),
    ]

    def open(self):
        self.driver.get(AMAZON_URL)
        time.sleep(2)
        self._dismiss_popups()
        return self

    def _dismiss_popups(self):
        for locator in self.POPUPS:
            try:
                el = self.driver.find_element(*locator)
                if el.is_displayed():
                    el.click()
                    time.sleep(0.5)
            except Exception:
                continue

    def search(self, query: str):
        self.type_text(self.SEARCH_BOX, query)
        time.sleep(0.3)
        self.click(self.SEARCH_BUTTON)
        return self