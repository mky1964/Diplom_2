import allure
import requests
import pytest
from constants import Constants



class TestRegistration:

    @allure.title('Позитивный тест авторизации нового пользователя')
    @allure.description('Позитивный тест. Получение в тело ответа. code == 200 и наличия в ответе к "success": true ')
    def test_new_user_registration(self, new_user):
        response = requests.post(Constants.REGISTRATION_USER_URL, json=new_user)
        accessToken = list(response.json().values())[2]
        assert response.status_code == 200  and ("accessToken" in list(response.json()))  # Проверка code == 200 и наличия в ответе кода 'accessToken'
        response_1 = requests.delete(Constants.DELETE_USER_URL, headers={'Authorization': accessToken})
        #print(response_1.status_code)


    @allure.title('Негативный тест авторизации существующего пользователя')
    @allure.description('Негативный тест. Получение  в тело ответа. code == 403 и наличия в ответе кода "message": "User already exists"')
    def test_repeat_registration_of_the_existing_user(self,new_user):
        response = requests.post(Constants.REGISTRATION_USER_URL, json=new_user)
        accessToken = list(response.json().values())[2]
        response_1 = requests.post(Constants.REGISTRATION_USER_URL, json=new_user)
        assert response_1.status_code == 403  and ( "User already exists"  in  list(response_1.json().values()))
        requests.delete(Constants.DELETE_USER_URL, headers={'Authorization': accessToken})


    @allure.title('Негативный тест авторизации пользователя без заполнения одного из обязательных полей (email)')
    @allure.description('Негативный тест. Получение  в тело ответа. code == 403 и наличия в ответе  "message": "Email, password and name are required fields"')
    def test_registration_of_user_without_one_param_email(self, new_user):
        new_user["email"] = None
        response = requests.post(Constants.REGISTRATION_USER_URL, json=new_user)
        assert response.status_code ==403 and  ("Email, password and name are required fields" in list(response.json().values()))

    @allure.title('Негативный тест авторизации пользователя без заполнения одного из обязательных полей (password)')
    @allure.description('Негативный тест. Получение  в тело ответа. code == 403 и наличия в ответе  "message": "Email, password and name are required fields"')
    def test_registration_of_user_without_one_param_password(self, new_user):
        new_user["password"] = None
        response = requests.post(Constants.REGISTRATION_USER_URL, json=new_user)
        assert response.status_code ==403 and  ("Email, password and name are required fields" in list(response.json().values()))

    @allure.title('Негативный тест авторизации пользователя без заполнения одного из обязательных полей (name)')
    @allure.description('Негативный тест. Получение  в тело ответа. code == 403 и наличия в ответе  "message": "Email, password and name are required fields"')
    def test_registration_of_user_without_one_param_name(self, new_user):
        new_user["name"] = None
        response = requests.post(Constants.REGISTRATION_USER_URL, json=new_user)
        assert response.status_code ==403 and  ("Email, password and name are required fields" in list(response.json().values()))

