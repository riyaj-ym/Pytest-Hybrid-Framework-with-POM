from selenium.webdriver.common.by import By

from Pages.SearchResultPage import SearchResultPage


class SearchPage:
    def __init__(self, driver):
        self.driver = driver

    search_field_name = "search"
    search_button_css = "button.btn-default"

    def enter_product_into_search_field(self, product):
        search_field = self.driver.find_element(By.NAME, self.search_field_name)
        search_field.click()
        search_field.clear()
        search_field.send_keys(product)

    def click_on_search_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.search_button_css).click()
        return SearchResultPage(self.driver)
