from selenium.webdriver.common.by import By


class SearchResultPage:
    def __init__(self, driver):
        self.driver = driver

    valid_product_status_xpath = '//div[@class="caption"]//a'
    invalid_product_status_xpath = '//input[@id="button-search"]/following::p[1]'

    def display_status_of_product(self):
        return self.driver.find_element(By.XPATH, self.valid_product_status_xpath).is_displayed()

    def display_status_of_no_product_msg(self, expected_msg):
        return self.driver.find_element(By.XPATH, self.invalid_product_status_xpath).text.__eq__(expected_msg)
