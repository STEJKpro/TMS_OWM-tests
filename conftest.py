import logging
import allure
from playwright.sync_api import sync_playwright

from pytest import fixture
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

"""
Настройка вывода логов
"""
logging.basicConfig(
    level=logging.DEBUG,
    filename="logs/mylog.log",
    encoding="utf8",
    filemode='w',
)


@fixture(scope="session")
def context():
    """Открытие браузера"""
    with sync_playwright() as playwright:
        with allure.step(f'Открыть браузер'):
            logging.debug('Открытие браузера')
            browser = playwright.chromium.launch(headless=False)
            context = browser.new_context(viewport={'width': 1920, 'height': 1080})
            
            yield context
            
        with allure.step(f'Закрыть браузер'):
            logging.debug('Закрытие браузера')

            context.close()
            browser.close()
            logging.debug('Браузер закрыт')
                   
            
@fixture(scope="class")
def page(context):
    """
    Создание новой страницы
    """
    with allure.step(f'Очистка данных сессии браузера'):
        logging.debug('Очистка данных сессии браузера')
        context.clear_cookies()
        context.storage_state().clear()
    with allure.step(f'Открыть страницу браузера'):
        logging.debug('Открытие страницы браузера')
    page = context.new_page()

    yield page
    
    with allure.step(f'Закрыть страницу браузера'):
        logging.debug('Закрытие страницы браузера')
        page.close()
