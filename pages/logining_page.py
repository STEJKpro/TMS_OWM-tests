from data.url_data import BASE_URL, LOGIN_PAGE_URL
from pages.base_page import BasePage



class LoginPage (BasePage):
    """
    
    """
    def goto_with_allure_step(self, url:str = LOGIN_PAGE_URL) -> None:
        """
        По умолчанию переход на страницу входа
        При необходимости в качестве параметра можно передать требуемый 

        Args:
            url (str, optional): Адрес страницы для перехода. Defaults to BASE_URL+LOGIN_PAGE_URL.
        """
        return super().goto_with_allure_step(url)
    
    def goto(self, url:str = LOGIN_PAGE_URL) -> None:
        """
        По умолчанию переход на страницу входа
        При необходимости в качестве параметра можно передать требуемый 

        Args:
            url (str, optional): Адрес страницы для перехода. Defaults to BASE_URL+LOGIN_PAGE_URL.
        """
        return super().goto(url)
    
    def goto_if_not_url_with_allure_step(self, url:str=LOGIN_PAGE_URL):
        """Метод для проверки соответствует ли url желаемому и перехода, в случае несоответствия
        По умолчанию проверяет соответствует ли url странице входа
        """
        return super().goto_if_not_url_with_allure_step(url)