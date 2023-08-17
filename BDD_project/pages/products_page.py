from base_page import BasePage


class ProductsPage(BasePage):
    def check_current_url(self):
        expected_url = "https://www.saucedemo.com/inventory.html"
        actual_url = self.browser.current_url
        assert expected_url == actual_url
