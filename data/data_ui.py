

"""   
Константы, для сайта OpenWeatherMap.com
Константа состоит из: названия метки поля ввода или названия кнопки; локатора поля ввода или кнопки

Синтаксис для констант:
СТРАНИЦА_ТИП_НАЗВАНИЕ
"""

### Константы элементов страницы выхода
SIGNUP_CHECKBOX_REMEMBER_ME = ('Remember me', "xpath=/html/body/div[2]/div[3]/div[2]/div/div/form/div[3]/div/label") #"remember me" (button)
SIGNUP_BUTTON_RECOWER_PASSWORD = ('Click here to recover.', 'xpath=/html/body/div[2]/div[3]/div[2]/div/div/div/div[1]/a') # Lost your password? Click here to recover. (button)
SIGNUP_BUTTON_CREATE_ACCOUNT = ('Create an Account.', 'xpath=/html/body/div[2]/div[3]/div[2]/div/div/p/a') # Not registered? Create an Account. (button)
SIGNUP_BUTTON_SUBMIT = ('Submit', 'xpath=/html/body/div[2]/div[3]/div[2]/div/div/form/input[3]') #submit (button)
SIGNUP_FIELD_EMAIL = ('Email', 'xpath = /html/body/div[2]/div[3]/div[2]/div/div/form/div[1]/input') #Enter email (field)
SIGNUP_FIELD_PASSWORD = ('Password', 'xpath = /html/body/div[2]/div[3]/div[2]/div/div/form/div[2]/input') #Password (field)

