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
MAIN_BUTTON_MARKETPLACE_LINK = ButtonElement('Button to MARKETPLACE page', 'xpath=/html/body/nav/ul[1]/div/ul/li[4]/a', 'API', href='https://home.openweathermap.org/marketplace')
MAIN_BUTTON_PRICE_LINK = ButtonElement('Button to Price page', 'xpath=/html/body/nav/ul[1]/div/ul/li[5]/a', 'Price', href='https://openweathermap.org/price')
MAIN_BUTTON_OUR_INITIATIVES_LINK = ButtonElement('Button to our initiatives page', 'xpath=/html/body/nav/ul[1]/div/ul/li[7]/a', 'Our Initiatives', href='https://openweathermap.org/our-initiatives')
MAIN_BUTTON_PARTNERS_LINK = ButtonElement('Button to partners page', 'xpath=/html/body/nav/ul[1]/div/ul/li[8]/a', 'Partners', href='https://openweathermap.org/examples')
MAIN_BUTTON_BLOG_LINK = ButtonElement('Button to blog page', 'xpath=/html/body/nav/ul[1]/div/ul/li[9]/a', 'Blog', href='https://openweather.co.uk/blog/category/weather')
MAIN_BUTTON_FOR_BUSINESS_LINK = ButtonElement('Button to for business page', 'xpath=/html/body/nav/ul[1]/div/ul/li[10]/a', 'For Business', href='https://openweather.co.uk/')
MAIN_DYNAMIC_BUTTON_FAQ_LINK = ButtonElement('Button to FAQ page', 'xpath=/html/body/nav/ul[1]/div/ul/li[12]/ul/li[1]/a', 'FAQ', href='https://openweathermap.org/faq')
MAIN_DYNAMIC_BUTTON_HOW_TO_START_LINK = ButtonElement('Button to How to start page', 'xpath=/html/body/nav/ul[1]/div/ul/li[12]/ul/li[2]/a', 'FAQ', href='https://openweathermap.org/appid')
MAIN_DYNAMIC_BUTTON_ASK_A_QUESTION_LINK = ButtonElement('Button to How to start page', 'xpath=/html/body/nav/ul[1]/div/ul/li[12]/ul/li[3]/a', 'Ask a question', href='https://home.openweathermap.org/questions')

MAIN_FIELD_SEARCH_CITY = FieldElement('Строка выбора города', 'xpath=/html/body/main/div[2]/div[1]/div/div/div[2]/div[1]/div/input', placeholder='Search city')
MAIN_BUTTON_SEARCH = FieldElement('Кнопка поиска города', 'xpath=/html/body/main/div[2]/div[1]/div/div/div[2]/div[1]/button', 'Search')
MAIN_DYNAMIC_1ST_CITY_SEARCH_RESULT = BaseElement('Превый элемент в результатах поиска города', 'xpath=/html/body/main/div[2]/div[1]/div/div/div[2]/div[1]/div/ul/li[1]/span[1]')
MAIN_TEXT_CURRENT_TEMPERATURE = BaseElement('Текущая температура', 'xpath = /html/body/main/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/span')

