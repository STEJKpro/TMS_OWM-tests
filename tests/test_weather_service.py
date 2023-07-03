import json
import logging

import allure
import requests
from playwright.sync_api import expect
from pytest import fixture, mark

from data import ui_data
from data.url_data import BASE_URL
from pages.main_page import MainPage


@fixture(scope='class')
def main_page(page):
    return MainPage(page)

@fixture(scope='class')
def website_temperature(main_page):
        logging.debug('получение текущей температуры с сайта')
        search_field = ui_data.MAIN_FIELD_SEARCH_CITY
        search_button =ui_data.MAIN_BUTTON_SEARCH
        search_result_element = ui_data.MAIN_DYNAMIC_1ST_CITY_SEARCH_RESULT
        temperature_element = ui_data.MAIN_TEXT_CURRENT_TEMPERATURE
        
        main_page.goto_with_allure_step(BASE_URL)
        main_page.field_fill_with_allure_step(search_field.name, search_field.locator, 'Minsk' )
        main_page.click_with_allure_step(search_button.name, search_button.locator)
        main_page.click_with_allure_step(search_result_element.name, search_result_element.locator)
        
        temp_minsk_open_weather = main_page.get_element_text(temperature_element.locator)
        temp_minsk_open_weather = float(temp_minsk_open_weather.replace('°C', ''))
        return temp_minsk_open_weather
    
    
@allure.suite('Тесты правильности прогноза погоды')
class TestWeatherАorecast():
    """
    Тесты правильности прогноза погоды
    """
    
    def get_delta(self, temp_web, temp_api):
        """Метод приведения дельты к положительному числу"""
        delta = temp_web-temp_api
        if delta >= 0:
            return delta
        else:
            return -delta

    @allure.description('Температурные расхождения должны составят не более 1.5 градусов')
    @allure.title("Тест соответствия температуры сайта с температурой OWM Api")  
    def test_comparison_internal_api (self, website_temperature):
        with allure.step("Получаем прогноз от внутреннего api"):
            response = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=53.902284&lon=27.561831&units=metric&mode=json&appid=47564c54c75bcf94b7a9684d4506cd89')
            data = json.loads(response.text)
            temperature_minsk_api = data['main']['temp']

        assert self.get_delta(temperature_minsk_api, website_temperature) <=1.5, "Температурная дельта > 1.5 °C'"


    @allure.description('Температурные расхождения должны составят не более 1.5 градусов')
    @allure.title("Тест соответствия температуры сайта с температурой api.open-meteo.com/")  
    def test_comparison_external_api (self, website_temperature):
        
        with allure.step("Получаем прогноз погоды от внешнего сервиса"):
            logging.debug("Получаем прогноз погоды от внешнего сервиса")
            response = requests.get(url='https://api.open-meteo.com/v1/forecast',
                        params= {
                            'latitude' : 53.902284,
                            'longitude':27.561831,
                            'models': 'best_match',
                            'timezone': 'Europe/Moscow',
                            'current_weather': True,
                            'hourly' : 'temperature_2m',
                        }
                        )
            data = json.loads(response.text)
            temperature_minsk_api = data['current_weather']['temperature']


        assert self.get_delta(temperature_minsk_api, website_temperature) <=1.5, f"Температурные дельты c внешним сервисом расходиться > 1.5 °C (int: {website_temperature}; ext:{temperature_minsk_api})"

        
    