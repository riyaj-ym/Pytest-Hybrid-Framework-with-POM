from pytest import fixture
from selenium import webdriver


@fixture
def setup(request):
    browser = request.config.getoption("--browser")
    driver = None
    if browser.__eq__("chrome"):
        from selenium.webdriver.chrome.service import Service
        from webdriver_manager.chrome import ChromeDriverManager
        service_object = Service(ChromeDriverManager().install())
        option = webdriver.ChromeOptions()
        option.add_experimental_option("detach", True)
        driver = webdriver.Chrome(service=service_object, options=option)

    elif browser.__eq__("edge"):
        from selenium.webdriver.edge.service import Service
        from webdriver_manager.microsoft import EdgeChromiumDriverManager
        service_object = Service(EdgeChromiumDriverManager().install())
        option = webdriver.EdgeOptions()
        option.add_experimental_option("detach", True)
        driver = webdriver.Edge(service=service_object, options=option)
    request.cls.driver = driver
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")
