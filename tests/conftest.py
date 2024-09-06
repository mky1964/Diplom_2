import requests
import random
import string
import pytest
import allure
from constants import Constants
from faker import Faker




@pytest.fixture
def new_user():

    faker = Faker()
    # генерируем логин, пароль и имя курьера
    email = faker.email()
    password = faker.password(10)
    name = faker.name()

    # собираем тело запроса
    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    # возвращаем список
    yield payload
    #requests.delete(f"{Constants.DELETING_COURIER_URL}{login_pass[0]}")"""