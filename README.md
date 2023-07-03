# Информация о проекте
## Описание:
Тестовый фреймворк для автоматизированного тестирования **OpenWeatherMap**
## Требовани:
#### Для полноценного использования проекта должны быть устнаовлены:  
- [Python](https://www.python.org/)(Протестировано на версии 3.11.3)  
- [Allure](https://docs.qameta.io/allure/)  
- Прочие модули и библиотеки из [requirements.txt](/requirements.txt)  
## Установка:
 ```
 git clone https://github.com/Michael02111/OpenWeatherMap-tests.git
 pip install -r requirements.txt
 ```
 Перед запуском создайте файл .env в корневой дирректории проекта.  
 И внесите актуальные данные. Пример файла переменных окружения: [.env_examle](/.env_examlpe)

 ## Запуск
 ``` pytest ```  
 или  
 ``` pytest --alluredir=<path-to-allure-report-dir>``` для использования с allure  
 для генерации web отчета:  
 ``` allure serve <path-to-allure-report-dir>```