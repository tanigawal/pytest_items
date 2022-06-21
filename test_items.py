import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


# Предположим, что у нас будет еще много тестов для Product Page :)
class TestProductPage():

    def test_add_button_is_present(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        # Если возвращаемый find_elements список не пуст, то тест прошел
        assert browser.find_elements(By.CLASS_NAME, "btn-add-to-basket") is not None, "Button is not present!"