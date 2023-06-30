import logging
import allure
from playwright.sync_api import sync_playwright

from pytest import fixture


"""
Настройка вывода логов
"""
logging.basicConfig(
    level=logging.DEBUG,
    filename="logs/mylog.log",
    encoding="utf8",
)

@fixture()
def page():
    """
    Фикстура для запуска и закрытия браузера
    """
    with sync_playwright() as playwright:
        with allure.step(f'Открыть браузер'):
            logging.debug('Открытие браузера')
            browser = playwright.chromium.launch(headless=False)
            context = browser.new_context(viewport={'width': 1920, 'height': 1080})
            # context = browser.new_context()
            page = context.new_page()

            yield page

        with allure.step(f'Закрыть браузер'):
            logging.debug('Закрытие браузера')
            page.close()
            context.close()
            browser.close()
            logging.debug('Браузер закрыт')
            