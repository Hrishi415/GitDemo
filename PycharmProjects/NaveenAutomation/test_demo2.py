import pytest
import time

from selenium import webdriver


def test_FB():
    driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
    driver.get("https://www.facebook.com/")


def test_Gmail():
    driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
    driver.get("https://www.google.com/gmail/")

