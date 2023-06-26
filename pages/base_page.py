from playwright.sync_api import Page
import logging
import allure

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self, url: str):
        """
        Метод перехода на указанную страницу сайта/приложения,
        :param url: адрес страницы
        """
        logging.debug('Перейти на страницу "{url}"')
        self.page.goto(url)
        
    
    def goto_with_allyre_step(self, url: str):
        """
        Метод перехода на указанную страницу сайта/приложения,
        :param url: адрес страницы
        """
        with allure.step('Перейти на страницу "{url}"'):
            logging.debug('Перейти на страницу "{url}"')
            self.page.goto(url)
        
    def click(self, locator):
        """
        Базовый метод нажатия на кнопку
        :param locator: xpath-локатор кнопки
        """
        logging.debug(f'Pressed button with locator: "{locator}"')
        self.page.locator(locator).click()
        
    def click_with_allure_step(self, locator, element_name):
        """
        Метод нажатия на кнопку по xpath с allure.step
        :param locator: xpath-локатор кнопки
        :element_name: название элемента 
        """
        with allure.step(f'Нажать кнопку "{element_name}" с локатором: {locator}'):
            logging.debug(f'Нажать кнопку "{element_name}" с локатором "{locator}"')
            self.page.locator(locator).click()