## Дипломный проект. Задание 2: API-тесты

### Автотесты для проверки бэк-энда, которая помогает заказать бургер в Stellar Burgers

### Реализованные сценарии

Созданы API - тесты:

Создание пользователя:
создание уникального пользователя;
создание пользователя, который уже зарегистрирован;
создание пользователя без заполнения одного из обязательных полей.


Логин пользователя:
логин под существующим пользователем,
логин с неверным логином и паролем.

Изменение данных пользователя:
с авторизацией,
без авторизации,

Создание заказа:
с авторизацией,
без авторизации,
с ингредиентами,
без ингредиентов,
с неверным хешем ингредиентов.

Получение заказов конкретного пользователя:
авторизованный пользователь,
неавторизованный пользователь.

### Структура проекта


- `tests` - пакет, содержащий тесты, разделенные энд-поинтам:
- test_registration.py
- test_login.py
- test_changing_users_parms.py
- test_get_order

### Запуск автотестов

$ pytest tests --alluredir=allure_results


**Установка зависимостей**

> `$ pip install -r requirements.txt`



