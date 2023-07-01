import logging
import allure

from pages.logining_page import LoginPage
from pytest import fixture, mark

from data import ui_data
from data.url_data import LOGIN_PAGE_URL

from playwright.sync_api import expect


@fixture(scope='class')
def login_page(page):
    return LoginPage(page)


class TestLoginPage():
    def test_logining_page(self, login_page):
        login_page.goto_with_allure_step()
        assert login_page.page.url == LOGIN_PAGE_URL


    @mark.parametrize("key, val", filter(lambda x: x[0].startswith('SIGNUP_'), ui_data.__dict__.items()) )
    def test_page_element(self, login_page, key, val):
        login_page.goto_if_not_url_with_allure_step()
        with allure.step(f"Проверяем наличие элемента:\n{val.element_discription}"):
            logging.debug(f"Проверяем наличие элемента:\n{val.element_discription}")
            button = login_page.page.locator(val.locator)
            expect(button).to_have_count(1)
            pass

