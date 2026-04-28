import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from pages.base_page import BasePage


class SearchResultsPage(BasePage):

    RESULTS_CONTAINER = (By.CSS_SELECTOR, '[data-component-type="s-search-result"]')
    SPONSORED_LABEL   = (By.CSS_SELECTOR, ".s-label-popover-default, .puis-sponsored-label-text")

    # Multiple fallback selectors — Amazon keeps changing these
    RESULT_LINK_SELECTORS = [
        "h2 a.a-link-normal",
        "h2 a",
        "a.a-link-normal.s-underline-text",
        "a.a-link-normal.s-no-outline",
        "a.a-link-normal[href*='/dp/']",
        ".s-title-instructions-style a",
        "a[href*='/dp/']",
    ]

    def wait_for_results(self):
        self.wait_for_element(self.RESULTS_CONTAINER)
        time.sleep(2)
        return self

    def _get_all_results(self):
        return self.driver.find_elements(*self.RESULTS_CONTAINER)

    def _is_sponsored(self, card):
        try:
            card.find_element(*self.SPONSORED_LABEL)
            return True
        except NoSuchElementException:
            return False

    def _find_link_in_card(self, card):
        for selector in self.RESULT_LINK_SELECTORS:
            try:
                link = card.find_element(By.CSS_SELECTOR, selector)
                if link and link.get_attribute("href"):
                    return link
            except NoSuchElementException:
                continue
        return None

    def click_first_non_sponsored_result(self):
        results = self._get_all_results()

        for card in results:
            if self._is_sponsored(card):
                continue
            link = self._find_link_in_card(card)
            if link:
                self.scroll_to(link)
                time.sleep(0.3)
                try:
                    link.click()
                except Exception:
                    self.js_click(link)
                return self

        # Fallback — try every card including sponsored ones
        for card in results:
            link = self._find_link_in_card(card)
            if link:
                self.scroll_to(link)
                time.sleep(0.3)
                try:
                    link.click()
                except Exception:
                    self.js_click(link)
                return self

        raise Exception(
            "Could not find any clickable product link on the search results page. "
            "Amazon may have changed their page structure."
        )