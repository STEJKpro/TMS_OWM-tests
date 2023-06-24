import requests
from playwright.sync_api import sync_playwright
from playwright.sync_api import Page, expect
import unittest
import re
import json
import pytest
from datetime import datetime


class TestOpenWeather(unittest.TestCase):

    def get_temperature_from_website(self):
        print('Getting data from website')
        self.page.goto('https://openweathermap.org/')
        self.page.wait_for_timeout(100)
        

        search_city = self.page.locator('xpath=/html/body/main/div[2]/div[1]/div/div/div[2]/div[1]/div/input')
        search_city.fill('Minsk') 
        search_button = self.page.locator('xpath=/html/body/main/div[2]/div[1]/div/div/div[2]/div[1]/button')
        search_button.click()
        self.page.wait_for_timeout(100)
    
        city_in = self.page.locator("xpath=/html/body/main/div[2]/div[1]/div/div/div[2]/div[1]/div/ul/li[1]/span[1]")
        city_in.click()
        self.page.wait_for_timeout(1000)

        
        temp_minsk_open_weather = self.page.locator('xpath = /html/body/main/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/span').text_content()
        temp_minsk_open_weather = float(temp_minsk_open_weather.replace('°C', ''))
        self.temperature_from_website = temp_minsk_open_weather
        return temp_minsk_open_weather
    
    def test_new_city_weather (self):
        self.page.goto("https://openweathermap.org/")
        search_new_city = self.page.locator('xpath=/html/body/main/div[2]/div[1]/div/div/div[2]/div[1]/div/input')
        search_new_city.fill('New York') 
        search_button = self.page.locator('xpath=/html/body/main/div[2]/div[1]/div/div/div[2]/div[1]/button')
        search_button.click()
        self.page.wait_for_timeout(100)
        city_in = self.page.locator("xpath=/html/body/main/div[2]/div[1]/div/div/div[2]/div[1]/div/ul/li[1]/span[1]")
        city_in.click()
        self.page.wait_for_timeout(1000)

    # def test_change_measure_unit_of_wind (self):
    #     self.page.goto("https://openweathermap.org/")
    #     change_speed_button = self.page.locator ("xpath = /html/body/main/div[2]/div[1]/div/div/div[1]/div[2]/div[3]")
    #     change_speed_button.click()
    #     self.page.wait_for_timeout(100)
    #     temp_and_speed_field = self.page.locator("xpath=/html/body/main/div[2]/div[2]/div[1]/div[1]/div[2]/ul/li[1]/div")
    #     self.page.wait_for_timeout(100)
    #     expect(temp_and_speed_field).to_contain_text("mph")


    def setup_class(self) -> None:
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()
        self.temperature_from_website = self.get_temperature_from_website(self)
        print('Setup')
        print(self.temperature_from_website)

    def teardown_class(self) -> None:
        self.browser.close()
        self.playwright.stop()
        print('Close')

    @pytest.mark.order(1)
    def test_mainpage_statuscode(self) -> None:
        url = 'https://openweathermap.org/'
        response = requests.get(url,)
        assert response.status_code == 200, 'Сервер OpenweatherMap не отвечает или отвечает с ошибкой'
        assert  '<h1><span class="orange-text">OpenWeather</span></h1>' in response.text, 'На главной странице не найден блок с надписью "OpenWeather"'
    
    @pytest.mark.order(2)
    def test_wrong_password_logining (self):
        self.page.goto("https://home.openweathermap.org/users/sign_in")
        email_field = self.page.locator("xpath=/html/body/div[2]/div[3]/div[2]/div/div/form/div[1]/input")
        email_field.fill('mikhail.tumas@mail.ru')
        wrong_password_field = self.page.locator("xpath=/html/body/div[2]/div[3]/div[2]/div/div/form/div[2]/input")
        wrong_password_field.fill('Mishatumas02111')
        self.page.wait_for_timeout(100)
        sign_in = self.page.locator("xpath=/html/body/div[2]/div[3]/div[2]/div/div/form/input[3]")
        sign_in.click()
        self.page.wait_for_timeout(100)
        notice_field = self.page.locator("xpath=/html/body/div[2]/div[3]/div/div/div/div[2]")
        self.page.wait_for_timeout(100)
        expect(notice_field).to_contain_text("Invalid Email or password")


    @pytest.mark.order(3)  
    def test_sign_in_page (self):
        self.page.goto('https://openweathermap.org/')
        sign_in = self.page.locator('xpath=/html/body/nav/ul[1]/div/ul/li[11]/a')
        sign_in.click()
        expect(self.page).to_have_url('https://home.openweathermap.org/users/sign_in')

    @pytest.mark.order(4)  
    def test_logining(self):
        self.page.goto("https://home.openweathermap.org/users/sign_in")
        email_field = self.page.locator("xpath=/html/body/div[2]/div[3]/div[2]/div/div/form/div[1]/input")
        email_field.fill('mikhail.tumas@mail.ru')   
        self.page.wait_for_timeout(100)

        password_field = self.page.locator("xpath=/html/body/div[2]/div[3]/div[2]/div/div/form/div[2]/input")
        password_field.fill('Mishatumas02')
        self.page.wait_for_timeout(100)

        sign_in = self.page.locator("xpath=/html/body/div[2]/div[3]/div[2]/div/div/form/input[3]")
        sign_in.click()
        self.page.wait_for_timeout(100)

        notice_field = self.page.locator("xpath=/html/body/div[2]/div[3]/div/div/div/div[2]")
        self.page.wait_for_timeout(100)
        expect(notice_field).to_contain_text("Signed in successfully")

    # def test_change_username (self):
    #     self.page.goto('https://home.openweathermap.org/home')
    #     username_field = self.page.locator("xpath=/html/body/div[2]/div[3]/div[3]/div/div/div[2]/form[1]/div[1]/div/input")                                  
    #     username_field.clear()
    #     username_field.fill ('Michael02111')
    #     save_button = self.page.locator ('xpath=/html/body/div[2]/div[3]/div[3]/div/div/div[2]/form[1]/input[3]')                                     
    #     save_button.click()
    #     notice_field = self.page.locator("xpath=/html/body/div[2]/div[3]/div/div/div/div[2]")
    #     expect(notice_field).to_contain_text("Profile was updated successfully")

    def get_delta(self, temp_web, temp_api):
            print('web', temp_web)
            print('api', temp_api)
            delta = temp_web-temp_api
            if delta >= 0:
                return delta
            else:
                return -delta
    
    @pytest.mark.order(4)
    def test_comparison_internal_api (self):
        if self.temperature_from_website is None:
            self.temperature_from_website = self.get_temperature_from_website()

        response = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=53.902284&lon=27.561831&units=metric&mode=json&appid=47564c54c75bcf94b7a9684d4506cd89')
        data = json.loads(response.text)
        print(data)
        temperature_minsk_api = data['main']['temp']

        assert self.get_delta(temperature_minsk_api, self.temperature_from_website) <=1.5, "Температурная дельта > 1.5 °C'"

    @pytest.mark.order(5)
    def test_comparison_external_api (self):
        if self.temperature_from_website is None:
            self.temperature_from_website = self.get_temperature_from_website()

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
        print(response.url)
        temperature_minsk_api = data['current_weather']['temperature']


        assert self.get_delta(temperature_minsk_api, self.temperature_from_website) <=1.5, f"Температурные дельты c внешним сервисом расходиться > 1.5 °C (int: {self.temperature_from_website}; ext:{temperature_minsk_api})"

    @pytest.mark.order(6)
    def test_guide_page (self):
        self.page.goto('https://openweathermap.org/')
        guide = self.page.query_selector('//*[@id="desktop-menu"]/ul/li[1]/a')
        guide.click()
        expect(self.page).to_have_url('https://openweathermap.org/guide')

    def test_api_page (self):
        self.page.goto('https://openweathermap.org/')
        api_page = self.page.query_selector('//*[@id="desktop-menu"]/ul/li[2]/a')
        api_page.click()
        expect(self.page).to_have_url('https://openweathermap.org/api')


    def test_dashboard_page (self):
        self.page.goto('https://openweathermap.org/')
        dashboard_page = self.page.query_selector('//*[@id="desktop-menu"]/ul/li[3]/a')
        dashboard_page.click()
        expect(self.page).to_have_url('https://openweathermap.org/weather-dashboard')


    def test_marketplace_page (self):
        self.page.goto('https://openweathermap.org/')
        marketplace_page_button = self.page.query_selector(' //*[@id="desktop-menu"]/ul/li[4]/a')
        with self.browser.contexts[0].expect_page() as new_page_info:
            marketplace_page_button.click() 
            new_page = new_page_info.value
            expect(new_page).to_have_url('https://home.openweathermap.org/marketplace')
            new_page.close()


    def test_pricing_page (self):
        self.page.goto('https://openweathermap.org/')
        pricing_page = self.page.query_selector('//*[@id="desktop-menu"]/ul/li[5]/a')
        pricing_page.click()
        expect(self.page).to_have_url('https://openweathermap.org/price')

    def test_maps_page (self):
        self.page.goto('https://openweathermap.org/')
        maps_page = self.page.query_selector('xpath=/html/body/nav/ul[1]/div/ul/li[6]/a')
        maps_page.click()
        expect(self.page).to_have_url(
            re.compile(r"https:\/\/openweathermap\.org\/weathermap\s*"))


    def test_our_initiatives_page (self):
        self.page.goto('https://openweathermap.org/')
        our_initiatives_page = self.page.query_selector('//*[@id="desktop-menu"]/ul/li[7]/a')
        our_initiatives_page.click()
        expect(self.page).to_have_url('https://openweathermap.org/our-initiatives')


    def test_partners_page (self):
        self.page.goto('https://openweathermap.org/')
        partners_page = self.page.query_selector('//*[@id="desktop-menu"]/ul/li[8]/a')
        partners_page.click()
        expect(self.page).to_have_url('https://openweathermap.org/examples')


    def test_blog_page (self):
        self.page.goto('https://openweathermap.org/')
        blog_page_button = self.page.query_selector('//*[@id="desktop-menu"]/ul/li[9]/a')
        with self.browser.contexts[0].expect_page() as new_page_info:
            blog_page_button.click() 
            new_page = new_page_info.value
            expect(new_page).to_have_url('https://openweather.co.uk/blog/category/weather')
            new_page.close()
        self.page.wait_for_timeout(1000)

    def test_for_business_page (self):
        self.page.goto('https://openweathermap.org/')
        for_business_page_button = self.page.query_selector('xpath=/html/body/nav/ul[1]/div/ul/li[10]/a')
        with self.browser.contexts[0].expect_page() as new_page_info:
            for_business_page_button.click()
            new_page = new_page_info.value
            expect(new_page).to_have_url('https://openweather.co.uk/')
            new_page.close()

    def test_support_page_FAQ (self):

        self.page.goto('https://openweathermap.org/')
        support_page = self.page.locator('xpath =/html/body/nav/ul[1]/div/ul/li[12]/div')
        support_page.click()
        support_field = self.page.locator ('xpath=/html/body/nav/ul[1]/div/ul/li[12]/ul/li[1]/a')
        support_field.click()
        expect(self.page).to_have_url('https://openweathermap.org/faq')


    def test_support_page_start (self):   

        self.page.goto('https://openweathermap.org/')
        support_page = self.page.locator('xpath =/html/body/nav/ul[1]/div/ul/li[12]/div')
        support_page.click()
        support_field = self.page.locator ('xpath=/html/body/nav/ul[1]/div/ul/li[12]/ul/li[2]/a')
        support_field.click()
        expect(self.page).to_have_url('https://openweathermap.org/appid')


    def test_support_page_ask_questions (self):

        self.page.goto('https://openweathermap.org/')
        support_page = self.page.locator('xpath=/html/body/nav/ul[1]/div/ul/li[12]/div')
        support_page.click()
        support_field = self.page.locator ('xpath=/html/body/nav/ul[1]/div/ul/li[12]/ul/li[3]/a')
        with self.browser.contexts[0].expect_page() as new_page_info:
            support_field.click()
            new_page = new_page_info.value
            expect(new_page).to_have_url('https://home.openweathermap.org/questions')
            new_page.close()

    # def test_logout(self):
    #     # email = "mikhail.tumas@mail.ru"
    #     # password = "Mishatumas02"
    #     self.page.goto("https://openweathermap.org/") #TODO: указать страницу с которой начинается тест
    #     account_name = self.page.locator("xpath=/html/body/nav/ul[1]/div/ul/li[11]/div/div")
    #     account_name.click()
    #     logout = self.page.locator("xpath = /html/body/nav/ul[1]/div/ul/li[11]/ul/li[5]/a")
    #     logout.click()
    #     self.page.wait_for_timeout(100)
    #     sign_in_field = self.page.locator("xpath=/html/body/div[2]/div[3]/div[2]/div/div/h3")
    #     self.page.wait_for_timeout(100)
    #     expect(sign_in_field).to_contain_text("Sign In To Your Account")



class TestCheckForm():
    def goto_if_not_url(self, url):
        if self.page.url != url: self.page.goto(url)

    def setup_class(self) -> None:
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()
        print('Setup')

    def teardown_class(self) -> None:
        self.browser.close()
        self.playwright.stop()
        print('Close')

#Проверка элементов формы входа в аккаунт
    @pytest.mark.order(1)
    def test_logining_form(self):
        self.page.goto("https://home.openweathermap.org/users/sign_in")
        self.page.wait_for_timeout(100)

            ####ПРОВЕРКА НАЛИЧИЯ КНОПКИ REMEMBER ME
    def test_remember_user(self):
        self.goto_if_not_url("https://home.openweathermap.org/users/sign_in")
        buttton_remember_me = self.page.locator("xpath=/html/body/div[2]/div[3]/div[2]/div/div/form/div[3]/div/label")
        expect(buttton_remember_me).to_contain_text("Remember me")

    #####ПРОВЕРКА НАЛИЧИЯ ССЫЛКИ "ЗАБЫЛИ ПАРОЛЬ" НА ВХОДЕ
    def test_recover_user(self):
        print('Тест forgot')
        lost_password = self.page.locator("xpath=/html/body/div[2]/div[3]/div[2]/div/div/div/div[1]/a")
        expect(lost_password).to_contain_text("Click here to recover.")

    #####ПРОВЕРКА НАЛИЧИЯ ССЫЛКИ "СОЗДАТЬ АККАУНТ" НА ВХОДЕ
    def test_create_account_link_on_sign_page(self):
        create_account = self.page.locator("xpath=/html/body/div[2]/div[3]/div[2]/div/div/p/a")
        expect(create_account).to_contain_text("Create an Account.")

    ####проверка наличия кнопки submit
    def test_submit_button_on_sign_page(self):
        submit_button = self.page.locator("xpath=/html/body/div[2]/div[3]/div[2]/div/div/form/input[3]")
        expect(submit_button, 'В форме авторизации отсутсвует кнопка "Submit"').to_have_count(1)

    def test_email_field(self):
            email_field = self.page.locator('xpath = /html/body/div[2]/div[3]/div[2]/div/div/form/div[1]/input')
            expect(email_field).to_have_attribute('placeholder','Enter email')

    def test_password_field(self):
            password_field = self.page.locator('xpath = /html/body/div[2]/div[3]/div[2]/div/div/form/div[2]/input')
            expect(password_field).to_have_attribute("placeholder", "Password")

