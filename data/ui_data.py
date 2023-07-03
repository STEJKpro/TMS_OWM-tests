from elements.page_elements import ButtonElement, FieldElement, CheckBoxElement, BaseElement

"""   
Константы, для сайта OpenWeatherMap.com

Синтаксис для названия констант:
СТРАНИЦА_ТИП_НАЗВАНИЕ

Элементы с пометкой DYNAMIC - Это поля, которые отображаются при какихх-то условиях и по умолчанию на странице не доступны
"""

# ###Элементы страницы выхода
SIGNUP_CHECKBOX_REMEMBER_ME = CheckBoxElement('Remember me checkbox', "xpath=/html/body/div[2]/div[3]/div[2]/div/div/form/div[3]/div/label", 'Remember me')
SIGNUP_BUTTON_RECOVER_PASSWORD = ButtonElement('Submit button', 'xpath=/html/body/div[2]/div[3]/div[2]/div/div/div/div[1]/a', 'Submit')
SIGNUP_BUTTON_CREATE_ACCOUNT = ButtonElement('Create new accaunt button', 'xpath=/html/body/div[2]/div[3]/div[2]/div/div/p/a', 'Create an Account.' )
SIGNUP_BUTTON_SUBMIT = ButtonElement('Submit loggining form button', 'xpath=/html/body/div[2]/div[3]/div[2]/div/div/form/input[3]', 'Submit' )
SIGNUP_FIELD_EMAIL = FieldElement('Account email field', 'xpath = /html/body/div[2]/div[3]/div[2]/div/div/form/div[1]/input', placeholder='Enter email')
SIGNUP_FIELD_PASSWORD = FieldElement('Account password field', 'xpath = /html/body/div[2]/div[3]/div[2]/div/div/form/div[2]/input', placeholder='Password' )

SIGNUP_DYNAMIC_MESSAGE_FIELD_FAIL = BaseElement('Logining Error field', 'xpath=/html/body/div[2]/div[3]/div/div/div/div[2]', element_text = 'Invalid Email or password')
SIGNUP_DYNAMIC_MESSAGE_FIELD_SUCCESS = BaseElement('Logining Error field', 'xpath=/html/body/div[2]/div[3]/div/div/div/div[2]', element_text = 'Signed in successfully')

# ###Элементы главной страницы
MAIN_BUTTON_GUIDE_LINK = ButtonElement('Button to guid page', 'xpath=/html/body/nav/ul[1]/div/ul/li[1]/a', 'Guide', href='https://openweathermap.org/guide')
MAIN_BUTTON_API_LINK = ButtonElement('Button to API page', 'xpath=/html/body/nav/ul[1]/div/ul/li[2]/a', 'API', href='https://openweathermap.org/api')
MAIN_BUTTON_DASHBOARD_LINK = ButtonElement('Button to DASHBOARD page', 'xpath=/html/body/nav/ul[1]/div/ul/li[3]/a', 'API', href='https://openweathermap.org/weather-dashboard')
MAIN_BUTTON_MARKETPLACE_LINK = ButtonElement('Button to MARKETPLACE page', 'xpath=/html/body/nav/ul[1]/div/ul/li[4]/a', 'API', href='https://openweathermap.org/weather-dashboard')
MAIN_BUTTON_PRICE_LINK = ButtonElement('Button to Price page', 'xpath=/html/body/nav/ul[1]/div/ul/li[5]/a', 'Price', href='https://openweathermap.org/weather-dashboard')
MAIN_BUTTON_OUR_INITIATIVES_LINK = ButtonElement('Button to our initiatives page', '/html/body/nav/ul[1]/div/ul/li[7]/a', 'Our Initiatives', href='https://openweathermap.org/our-initiatives')
