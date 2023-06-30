from playwright.sync_api import Page
import logging
import allure

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self, url: str) -> None:
        """
        Метод перехода на указанную страницу сайта/приложения,
        :param url: адрес страницы
        :type url: str
        """
        logging.debug(f'Перейти на страницу "{url}"')
        self.page.goto(url)
        
    
    def goto_with_allyre_step(self, url: str) -> None:
        """
        Метод перехода на указанную страницу сайта/приложения,
        :param url: адрес страницы
        :type url: str
        """
        with allure.step(f'Перейти на страницу "{url}"'):
            logging.debug(f'Перейти на страницу "{url}"')
            self.page.goto(url)
        
    def check_url(self, url:str) -> bool:
        """
        Метод проверки правильности текущего url
        :param url: проверяемый url страницы
        :type url: str
        
        :return: Возращает True в случае если url совпадлает, в противном случае - False
        :rtype: bool
        """
        return True if self.page.url == url else False
        
        
    def click(self, locator:str) -> None:
        """
        Базовый метод нажатия на кнопку
        :param locator: xpath-локатор кнопки
        """
        logging.debug(f'Pressed button with locator: "{locator}"')
        self.page.locator(locator).click()
        
    def click_with_allure_step(self, locator:str, element_name:str) -> None:
        """
        Метод нажатия на кнопку по xpath с allure.step
        :param locator: xpath-локатор кнопки
        :type locator: str
        :param element_name: название элемента 
        :type element_name: str
        """
        with allure.step(f'Нажать кнопку "{element_name}" с локатором: {locator}'):
            logging.debug(f'Нажать кнопку "{element_name}" с локатором "{locator}"')
            self.page.locator(locator).click()
            
    def field_fiil(self, locator: str, text:str) -> None:
        """
        Метод нажатия на кнопку по xpath с allure.step
        :param locator: xpath-локатор кнопки
        :type locator: str
        :param text: Текст для ввода в поле
        :type text: str
        """
        logging.debug(f'Ввод строки "{text}" в поле с локатором "{locator}"')
        field = self.page.locator(locator)
        field.clear()
        field.fill (text)
        
    
    def field_fill_with_allure_step(self, locator:str, text:str, element_name:str) -> None:
        """
        Метод нажатия на кнопку по xpath с allure.step
        :param locator: xpath-локатор кнопки
        :type locator: str
        :param text: Текст для ввода в поле
        :type text: str
        :param element_name: название элемента
        :type element_name: str
        """
        with allure.step(f'Очистить поле "{element_name}" с локатором {locator} и значением {text}'):
            logging.debug(f'Ввод строки "{text}" в поле {element_name} с локатором "{locator}"')
            field = self.page.locator(locator)
            field.clear()
            field.fill (text)
