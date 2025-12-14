# Дипломный проект тестирования API Petstore
> [Petstore Swagger](https://petstore.swagger.io/#/)

![This is an image](/resources/images/readme/petstore.png)

### Список проверок:
- [x] Проверка методов для пользователя
  - Создание пользователя
  - Получение существующего пользователя
  - Обновление пользователя
  - Удаление пользователя
  - Получение несуществующего пользователя
- [x] Проверка методов для питомца
  - Создание питомца
  - Получение существующего питомца
  - Обновление питомца
  - Удаление питомца
  - Получение несуществующего питомца
----
### Используемые технологии
<p  align="center">
   <code><img width="5%" title="Python" src="/resources/images/readme/python.png"></code>
   <code><img width="5%" title="PyCharm" src="/resources/images/readme/pycharm.png"></code>
   <code><img width="5%" title="Pytest" src="/resources/images/readme/pytest.png"></code>
   <code><img width="5%" title="Jenkins" src="/resources/images/readme/jenkins.png"></code>
   <code><img width="5%" title="Allure Report" src="/resources/images/readme/allure_report.png"></code>
   <code><img width="5%" title="Allure TestOps" src="/resources/images/readme/allure_testops.png"></code>
   <code><img width="5%" title="Telegram" src="/resources/images/readme/tg.png"></code>
</p>

----
### Локальный запуск

1. Склонировать репозиторий
2. Установить зависимости командой `pip install -r requirements.txt`
3. Открыть проект в PyCharm, установить интерпретатор
4. Создать `.env` файл, пример файла - `.env.example`
5. Запустить тесты в командной строке `pytest .`:

----
### Удаленный запуск в Jenkins

> <a target="_blank" href="https://jenkins.autotests.cloud/job/iawitm_petstore_api_test_project/">_**Ссылка на сборку в Jenkins**_</a>

1. Открыть проект
2. Выбрать пункт `Build with Parameters`
3. Указать комментарий для отчета в Telegram
3. Нажать кнопку `Build`

![This is an image](/resources/images/readme/jenkins_build.png)

----

### Allure отчет

#### Пример формирования отчета:

![This is an image](/resources/images/readme/allure_overview.png)

----
### Интеграция с Allure TestOps

#### Пример генерации тест-кейсов на основе автотестов
![This is an image](/resources/images/readme/case_legend.png)
![This is an image](/resources/images/readme/testops_cases_api.png)

----
### Оповещение о результатах прогона тестов в Telegram
#### Пример уведомления в Telegram
![This is an image](/resources/images/readme/tg_notification.png)