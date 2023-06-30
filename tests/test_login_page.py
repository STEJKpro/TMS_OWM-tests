import logging
import allure

from pages.logining_page import LoginPage





class TestLoginPage():
        
    def test_logining_form(self, page):
        self.login_page = LoginPage(page)
        self.login_page.goto()
        
    
    def test_123(self,  page):
        self.login_page = LoginPage(page)
        self.login_page.goto('https://dev.by/')