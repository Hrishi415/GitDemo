import pytest
from selenium import webdriver


@pytest.fixture(scope='class')
def test_chrome_driver(request):
    driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
    request.cls.driver = driver
    yield
    driver.close()


@pytest.mark.usefixtures("test_chrome_driver")
class test_Base_class:
    pass


class test_Child_class(test_Base_class):
    def test_google_title(self):
        self.driver.get("http://www.google.com")
        assert self.test_google_title == "Google"

