import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage


class ProductPage(BasePage):

    PRICE_SELECTORS = [
        (By.CSS_SELECTOR, "#corePriceDisplay_desktop_feature_div .a-offscreen"),
        (By.CSS_SELECTOR, "#corePriceDisplay_desktop_feature_div .a-price-whole"),
        (By.CSS_SELECTOR, ".apexPriceToPay .a-offscreen"),
        (By.CSS_SELECTOR, ".apexPriceToPay span[aria-hidden='true']"),
        (By.CSS_SELECTOR, "#corePrice_desktop .a-offscreen"),
        (By.CSS_SELECTOR, ".priceToPay .a-offscreen"),
        (By.CSS_SELECTOR, ".priceToPay span[aria-hidden='true']"),
        (By.CSS_SELECTOR, "#price_inside_buybox"),
        (By.CSS_SELECTOR, "#priceblock_ourprice"),
        (By.CSS_SELECTOR, "#priceblock_dealprice"),
        (By.CSS_SELECTOR, ".a-price .a-offscreen"),
        (By.CSS_SELECTOR, "#buyNewSection .a-price .a-offscreen"),
        (By.CSS_SELECTOR, "#newBuyBoxPrice"),
        (By.XPATH,        "//span[contains(@class,'a-price')]//span[@class='a-offscreen']"),
        (By.XPATH,        "//div[@id='corePriceDisplay_desktop_feature_div']//span[contains(@class,'a-offscreen')]"),
    ]
    ADD_TO_CART_SELECTORS = [
        (By.ID,           "add-to-cart-button"),
        (By.NAME,         "submit.add-to-cart"),
        (By.CSS_SELECTOR, "input[name='submit.add-to-cart']"),
        (By.CSS_SELECTOR, "input#add-to-cart-button"),
        (By.XPATH,        "//input[@id='add-to-cart-button']"),
        (By.XPATH,        "//input[contains(@value,'Add to Cart')]"),
        (By.XPATH,        "//button[normalize-space()='Add to Cart']"),
        (By.XPATH,        "//button[contains(text(),'Add to Cart')]"),
        (By.XPATH,        "//button[contains(text(),'Add to cart')]"),
        (By.XPATH,        "//input[contains(@value,'Add to cart')]"),
    ]

    BUYING_OPTIONS_SELECTORS = [
        (By.XPATH,        "//a[contains(translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'buying options')]"),
        (By.XPATH,        "//span[contains(translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'buying options')]//ancestor::a"),
        (By.CSS_SELECTOR, "a[href*='buying-options']"),
        (By.CSS_SELECTOR, "a[href*='offer-listing']"),
        (By.XPATH,        "//a[contains(@href,'offer-listing')]"),
        (By.XPATH,        "//a[contains(@href,'buying-options')]"),
    ]

    VARIANT_SELECTORS = [
        (By.CSS_SELECTOR, "#variation_color_name ul li:not(.a-button-disabled)"),
        (By.CSS_SELECTOR, "#variation_size_name ul li:not(.a-button-disabled)"),
        (By.CSS_SELECTOR, "#variation_style_name ul li:not(.a-button-disabled)"),
        (By.CSS_SELECTOR, "#variation_storage_size_name ul li:not(.a-button-disabled)"),
        (By.CSS_SELECTOR, ".a-button-toggle:not(.a-button-selected):not(.a-button-disabled)"),
        (By.XPATH,        "//div[@id='twister']//li[not(contains(@class,'disabled'))]"),
    ]

    CART_COUNT    = (By.ID, "nav-cart-count")
    PRODUCT_TITLE = (By.ID, "productTitle")



    def get_price(self) -> str:
        time.sleep(1)
        for locator in self.PRICE_SELECTORS:
            try:
                for el in self.driver.find_elements(*locator):
                    text = (el.get_attribute("textContent") or el.text or "").strip()
                    if text and ("$" in text or "₹" in text or "MRP" in text):
                        return text
            except Exception:
                continue
        return "Price not available"

    def get_product_title(self) -> str:
        try:
            return self.driver.find_element(*self.PRODUCT_TITLE).text.strip()
        except NoSuchElementException:
            return self.driver.title.strip()

    def get_cart_count(self) -> int:
        try:
            text = self.driver.find_element(*self.CART_COUNT).text.strip()
            return int(text) if text.isdigit() else 0
        except Exception:
            return 0

    def _find_button(self, selectors):
        for locator in selectors:
            try:
                for el in self.driver.find_elements(*locator):
                    if el.is_displayed() and el.is_enabled():
                        return el
            except Exception:
                continue
        return None

    def _click(self, el):
        self.scroll_to(el)
        time.sleep(0.3)
        try:
            el.click()
        except Exception:
            self.js_click(el)

    def _select_variants(self):
        for _ in range(4):
            picked = False
            for locator in self.VARIANT_SELECTORS:
                try:
                    for opt in self.driver.find_elements(*locator):
                        classes = opt.get_attribute("class") or ""
                        if "selected" in classes or "a-button-selected" in classes:
                            continue
                        self._click(opt)
                        time.sleep(0.8)
                        picked = True
                        break
                except Exception:
                    continue
            if not picked:
                break
        time.sleep(1)

    def _try_add_to_cart_direct(self) -> bool:
        btn = self._find_button(self.ADD_TO_CART_SELECTORS)
        if btn:
            self._click(btn)
            time.sleep(2)
            return True
        return False

    def _try_buying_options_flow(self) -> bool:
        """
        Handles the 'See All Buying Options' flow that Amazon shows
        for phones — clicks through to the offers listing page and
        adds the first available new offer to the cart.
        """
        btn = self._find_button(self.BUYING_OPTIONS_SELECTORS)
        if not btn:
            return False

        from utils import logger
        logger.info("Found 'See All Buying Options' — navigating to offers page...")

        self._click(btn)
        time.sleep(3)

        
        atc = self._find_button(self.ADD_TO_CART_SELECTORS)
        if atc:
            self._click(atc)
            time.sleep(2)
            return True

        
        offer_atc_selectors = [
            (By.XPATH, "(//input[@name='submit.addToCart'])[1]"),
            (By.XPATH, "(//input[contains(@value,'Add to Cart')])[1]"),
            (By.XPATH, "(//button[contains(text(),'Add to Cart')])[1]"),
            (By.CSS_SELECTOR, "input[name='submit.addToCart']"),
        ]
        atc = self._find_button(offer_atc_selectors)
        if atc:
            self._click(atc)
            time.sleep(2)
            return True

        return False

    

    def add_to_cart(self) -> bool:
        time.sleep(2)

       
        if self._try_add_to_cart_direct():
            return True

        
        self._select_variants()
        if self._try_add_to_cart_direct():
            return True

        
        if self._try_buying_options_flow():
            return True

        
        self.driver.execute_script("window.scrollTo(0, 600)")
        time.sleep(1)
        if self._try_add_to_cart_direct():
            return True

        return False