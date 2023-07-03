import logging
import allure
from pages.logining_page import LoginPage
from pytest import fixture, mark
from data import ui_data
from data.url_data import LOGIN_PAGE_URL
from playwright.sync_api import expect
import os


@fixture(scope='class')
def login_page(page):
    return LoginPage(page)


@allure.suite('Тесты страницы входа')
class TestLoginPage():
    """Тесты страницы входа"""
    
    @allure.description('Проверка в действительности ли url страницы соответсвует url страницы входа')
    @allure.title("Проверка правильности url страницы входа")
    def test_logining_page(self, login_page):
        logging.debug(f"Начат тест проверки страницы входа")
        logging.debug(f"Переходим на страницу входа с url:{LOGIN_PAGE_URL}")
        login_page.goto_with_allure_step()
        
        with allure.step("Проверить правильность url"):
            logging.debug("Проверяем правильность url страницы на которую перешли")
            assert login_page.page.url == LOGIN_PAGE_URL


    @mark.parametrize(
        "key, val", 
        filter(
            lambda x: (x[0].startswith('SIGNUP_') and 'DYNAMIC' not in x[0]),
            ui_data.__dict__.items()
            ),
        )
    @allure.title(f'Проверка наличия элемента на странице')
    @allure.description('Проверяем существует ли элемент на странице')
    def test_page_element(self, login_page, key, val):
        logging.debug(f"Начат тест проверки элемента {key}")
        logging.debug("Проверяем на странице входа мы ли мыб в противном случае переходим на страницу")
        login_page.goto_if_not_url_with_allure_step()
        with allure.step(f"Проверяем наличие элемента:\n{val.element_discription}"):
            logging.debug(f"Проверяем наличие элемента:\n{val.element_discription}")
            button = login_page.page.locator(val.locator)
            expect(button).to_have_count(1)
    
     
    @allure.title('Вход в аккаунт с недействительными данными')
    @allure.description('Проверяем корректонсть работы с неверными данными для входа')
    def test_wrong_password_logining (self, login_page):
        #данные элементов используемых в тесте
        logging.debug(f"Начат тест проверки входа на страницу с неверными данными")
        
        email_field = ui_data.SIGNUP_FIELD_EMAIL
        password_field = ui_data.SIGNUP_FIELD_PASSWORD
        submit_button = ui_data.SIGNUP_BUTTON_SUBMIT
        notice_field = ui_data.SIGNUP_DYNAMIC_MESSAGE_FIELD_FAIL
        
        login_page.goto_if_not_url_with_allure_step()
        login_page.field_fill_with_allure_step(email_field.name, email_field.locator, os.environ.get('OWM_WRONG_LOGIN'))
        login_page.field_fill_with_allure_step(password_field.name, password_field.locator, os.environ.get('OWM_WRONG_PASSWORD') )
        login_page.click_with_allure_step(submit_button.name, submit_button.locator)
        
        notification = login_page.locator(notice_field.locator)
        expect(notification, 'Сообщение об ошибке не найдено, либо текст ошибки не совпадает с предполагаемым').to_contain_text(notice_field.element_text)
        
        
    @allure.title('Вход в аккаунт с корректными данными')
    @allure.description('Проверяем корректонсть работы с корректными данными для входа')
    def test_correct_password_logining (self, login_page):
        #данные элементов используемых в тесте
        logging.debug(f"Начат тест проверки входа на страницу с корректными данными")
        
        email_field = ui_data.SIGNUP_FIELD_EMAIL
        password_field = ui_data.SIGNUP_FIELD_PASSWORD
        submit_button = ui_data.SIGNUP_BUTTON_SUBMIT
        notice_field = ui_data.SIGNUP_DYNAMIC_MESSAGE_FIELD_SUCCESS
        
        login_page.page.reload()
        
        login_page.goto_with_allure_step(LOGIN_PAGE_URL)
        login_page.field_fill_with_allure_step(email_field.name, email_field.locator, os.environ.get('OWM_LOGIN'))
        login_page.field_fill_with_allure_step(password_field.name, password_field.locator, os.environ.get('OWM_PASSWORD') )
        login_page.click_with_allure_step(submit_button.name, submit_button.locator)
        
        notification = login_page.locator(notice_field.locator)
        expect(notification, 'Сообщение об успешном входе не найдено, либо текст не совпадает с предполагаемым').to_contain_text(notice_field.element_text)
        