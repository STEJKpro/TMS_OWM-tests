import logging
import allure
from pages.main_page import MainPage
from pytest import fixture, mark
from data import ui_data
from data.url_data import BASE_URL
from playwright.sync_api import expect
import os

@fixture(scope='class')
def main_page(page):
    return MainPage(page)

@allure.suite('Тесты главной страницы')
class TestMainPage():
    """Тесты главной страницы"""
    
    @allure.description('Проверка в действительности ли url страницы соответсвует url главной страницы')
    @allure.title("Проверка правильности url главной страницы")
    def test_logining_page(self, main_page):
        logging.debug(f"Начат тест проверки главной страницы")
        logging.debug(f"Переходим на страницу входа с url:{BASE_URL}")
        main_page.goto_with_allure_step()
        
        with allure.step("Проверить правильность url"):
            logging.debug("Проверяем правильность url страницы на которую перешли")
            assert main_page.page.url == BASE_URL


    
    @mark.parametrize(
        "key, val", 
        filter(
            lambda x: (x[0].startswith('MAIN_') and 'DYNAMIC' not in x[0]),
            ui_data.__dict__.items()
            ),
        )
    @allure.title(f'Проверка наличия элемента на странице')
    @allure.description('Проверяем существует ли элемент на странице')
    def test_page_element(self, main_page, key, val):
        logging.debug(f"Начат тест проверки элемента {key}")
        logging.debug("Проверяем на главной мы ли мы странице, в противном случае переходим на страницу")
        main_page.goto_if_not_url_with_allure_step()
        with allure.step(f"Проверяем наличие элемента:\n{val.element_discription}"):
            logging.debug(f"Проверяем наличие элемента:\n{val.element_discription}")
            button = main_page.page.locator(val.locator)
            expect(button).to_have_count(1)
    
    @mark.parametrize(
        "key, val", 
        filter(
            lambda x: (x[0].startswith('MAIN_') and 'DYNAMIC' not in x[0] and 'LINK' in x[0]),
            ui_data.__dict__.items()
            ),
        )
    @allure.title(f'Проверка наличия элемента на странице')
    @allure.description('Проверяем существует ли элемент на странице')
    def test_page_links(self, main_page, context, key, val):
        logging.debug(f"Начат тест проверки перехода на страницe по кнопке {key}")
        with allure.step(f"Проверяем правильность url страницы на которую перешли url Фактический:{main_page.page.url} url предполагаемый:{val.href}"):   
            with context.expect_page() as new_page_info:
                main_page.click_with_allure_step(val.name, val.locator, modifiers=["Shift"])
                new_page = new_page_info.value
                expect(new_page).to_have_url(val.href)
                new_page.close()
