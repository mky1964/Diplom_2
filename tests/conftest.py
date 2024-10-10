
import pytest
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
