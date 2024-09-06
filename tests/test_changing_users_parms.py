import allure
import requests
import pytest
from constants import Constants
from faker import Faker

class TestChangeUsersParms:

    @allure.title('Позитивный тест изменения данных  пользователя полсе авторизации')
    @allure.description('Позитивный тест. Получение в тело ответа. code == 200 и наличия в ответе "user"  Проверяется замена трёх параметров')
    @pytest.mark.parametrize('test_number', [1, 2, 3])
    def test_change_user_parms_wuth_authorization(self, new_user, test_number):
        faker = Faker()
        user = new_user
        response_1 = requests.post(Constants.REGISTRATION_USER_URL, json=user)#Регистрация пользователя
        accessToken_1 = list(response_1.json().values())[2]
        if test_number == 1:
            user['email'] = faker.email()
        elif test_number == 2:
            user["password"] = faker.password(10)
        elif test_number == 3:
            user["name"] = faker.name()
        response_2 = requests.patch(Constants.NEW_PARMS_USER_URL, json=user, headers={'Authorization': accessToken_1})
        assert response_2.status_code == 200 and ("user" in list(response_2.json()))
        requests.delete(Constants.DELETE_USER_URL, headers={'Authorization': accessToken_1})#Удаление пользователя

    @allure.title('Негативный тест изменения данных  пользователя без авторизации')
    @allure.description('Негативный  тест. Получение в тело ответа. code == 401 и наличия в ответе "You should be authorised"  Проверяется замена трёх параметров')
    @pytest.mark.parametrize('test_number', [1, 2, 3])
    def test_change_user_parms_wuth_no_authorization(self, new_user, test_number):
        faker = Faker()
        user = new_user
        response_1 = requests.post(Constants.REGISTRATION_USER_URL, json=user)#Регистрация пользователя
        accessToken_1 = list(response_1.json().values())[2]
        if test_number == 1:
            user['email'] = faker.email()
        elif test_number == 2:
            user["password"] = faker.password(10)
        elif test_number == 3:
            user["name"] = faker.name()
        response_2 = requests.patch(Constants.NEW_PARMS_USER_URL, json=user)
        print(list(response_2.json().values()))
        assert response_2.status_code == 401 and ( "You should be authorised" in list(response_2.json().values()))
        requests.delete(Constants.DELETE_USER_URL, headers={'Authorization': accessToken_1})#Удаление пользователя





        

