from elements.page_elements import ButtonElement, FieldElement, CheckBoxElement

"""   
Константы, для сайта OpenWeatherMap.com

Синтаксис для названия констант:
СТРАНИЦА_ТИП_НАЗВАНИЕ
"""

# ###Элементы страницы выхода
SIGNUP_CHECKBOX_REMEMBER_ME = CheckBoxElement('Remember me checkbox', "xpath=/html/body/div[2]/div[3]/div[2]/div/div/form/div[3]/div/label", 'Remember me')
SIGNUP_BUTTON_RECOWER_PASSWORD = ButtonElement('Submit button', 'xpath=/html/body/div[2]/div[3]/div[2]/div/div/div/div[1]/a', 'Submit')
SIGNUP_BUTTON_CREATE_ACCOUNT = ButtonElement('Create new accaunt button', 'xpath=/html/body/div[2]/div[3]/div[2]/div/div/p/a', 'Create an Account.' )
SIGNUP_BUTTON_SUBMIT = ButtonElement('Submit loggining form button', 'xpath=/html/body/div[2]/div[3]/div[2]/div/div/form/input[3]', 'Submit' )
SIGNUP_FIELD_EMAIL = FieldElement('Account email field', 'xpath = /html/body/div[2]/div[3]/div[2]/div/div/form/div[1]/input', placeholder='Enter email')
SIGNUP_FIELD_PASSWORD = FieldElement('Account password field', 'xpath = /html/body/div[2]/div[3]/div[2]/div/div/form/div[2]/input', placeholder='Password' )