import pytest
from selenium import webdriver

@pytest.fixture(params=["Chrome"], scope="class")
def test_driver(request):
    if request.param =="Chrome":
        driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
        request.cls.driver = driver
        yield
        driver.close()

@pytest.mark.usefixtures("test_driver"
                         )

class BaseTest:
    pass

class Test_Google(BaseTest):
    def test_google_title(self):
        self.driver.get("http://www.google.com")
        assert self.driver.title == "Google2"