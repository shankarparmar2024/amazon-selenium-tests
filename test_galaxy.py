"""
Test Case 2 — Search for a Samsung Galaxy S25 Ultra, add to cart, print price.
"""
import pytest
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage
from config.config import SEARCH_QUERIES
from utils import logger


class TestGalaxyCart:

    def test_search_galaxy_add_to_cart(self, driver):
        query = SEARCH_QUERIES["galaxy"]
        logger.info(f"Test Case 2 started  →  query: '{query}'")

        HomePage(driver).open()
        logger.info("Amazon home page loaded.")

        HomePage(driver).search(query)
        logger.info(f"Search submitted: '{query}'")

        results = SearchResultsPage(driver)
        results.wait_for_results()
        results.click_first_non_sponsored_result()
        logger.info("Navigated to product page.")

        product = ProductPage(driver)
        title   = product.get_product_title()
        price   = product.get_price()

        logger.price(title, price)
    
        before = product.get_cart_count()
        added  = product.add_to_cart()
        product.take_screenshot("tc2_galaxy_cart")

        assert added, (
            "Could not add Galaxy S25 Ultra to cart — Add to Cart button not found. "
            "Amazon may be showing a carrier selection or region-locked page."
        )

        after = product.get_cart_count()
        logger.success(f"Galaxy added to cart  |  Cart: {before}→{after}  |  Price: {price}")
        assert after > before, f"Cart count did not go up. Before={before} After={after}"