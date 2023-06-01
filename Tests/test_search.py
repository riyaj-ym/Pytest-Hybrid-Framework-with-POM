from pytest import mark

from Pages.SearchPage import SearchPage


@mark.usefixtures("setup")
class TestSearch:
    url = "https://tutorialsninja.com/demo/"

    def test_search_with_valid_product(self):
        self.driver.get(self.url)
        search_page = SearchPage(self.driver)
        search_page.enter_product_into_search_field("Hp")
        search_result_page = search_page.click_on_search_button()
        assert search_result_page.display_status_of_product()

    def test_search_with_invalid_product(self):
        self.driver.get(self.url)
        search_page = SearchPage(self.driver)
        search_page.enter_product_into_search_field("Honda")
        search_result_page = search_page.click_on_search_button()
        expected_msg = "There is no product that matches the search criteria."
        assert search_result_page.display_status_of_no_product_msg(expected_msg)

    def test_search_with_no_product(self):
        self.driver.get(self.url)
        search_page = SearchPage(self.driver)
        search_page.enter_product_into_search_field("")
        search_result_page = search_page.click_on_search_button()
        expected_msg = "There is no product that matches the search criteria."
        assert search_result_page.display_status_of_no_product_msg(expected_msg)
