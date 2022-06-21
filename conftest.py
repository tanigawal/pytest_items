import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Добавляем параметры browser_name и language в командную строку
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome", help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="ru", help="Choose default language")

@pytest.fixture(scope="function")
def browser(request):
    # Сохраняем в переменную выбранный браузер
    browser_name = request.config.getoption("browser_name")
    browser = None
    # Сохраняем в переменную выбранный язык
    user_language = request.config.getoption("language")

    #Если выбран Chrome, создаем его экземпляр с использованием выбранного языка
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    #Если выбран Firefox, создаем его экземпляр с использованием выбранного языка
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    #Иначе ругаемся :)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
