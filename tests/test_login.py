import allure
import requests
import pytest
from constants import Constants

class TestLogin:

    @allure.title('Позитивный тест авторизации существующего пользователя')
    @allure.description('Позитивный тест. Получение в тело ответа. code == 200 и наличия в ответе "accessToken"' )
    def test_existing_user_login(self, new_user):
        response_1 = requests.post(Constants.REGISTRATION_USER_URL, json=new_user)
        accessToken_1 = list(response_1.json().values())[2]
        response_2 = requests.post(Constants.LOGIN_USER_URL, json=new_user)
D        assert response_2.status_code == 200 and ("accessToken" in list(response_2.json()))
        requests.delete(Constants.DELETE_USER_URL, headers={'Authorization': accessToken_1})



    @allure.title('Негативный  тест авторизация существующего пользователя')
    @allure.description('Негативный тест. Логин с неверным логином и паролем.Получение в тело ответа. code == 401 и наличия в ответе "email or password are incorrect"' )
    @pytest.mark.parametrize('test_number', [1, 2])
    def test_existing_user_login_wrong_parms(self, new_user, test_number):
            response = requests.post(Constants.REGISTRATION_USER_URL, json=new_user)
            #print(response.json())
            accessToken = list(response.json().values())[2]
            user = new_user
            if test_number == 1:
                new_user['email'] = 'hhhh@gmail.com'
                response_1 = requests.post(Constants.LOGIN_USER_URL, json=user)
                print(response_1.json())
                assert (response_1.status_code == 401) and ("email or password are incorrect" in list(response_1.json().values()))
                delete_1 = requests.delete(Constants.DELETE_USER_URL,  headers={'Authorization': accessToken} )

            elif test_number ==2:
                new_user['password'] = 'Hhhhhh'
                response_2 = requests.post(Constants.LOGIN_USER_URL, json=user)
                #print(response_2.json())
                assert (response_2.status_code == 401) and ("email or password are incorrect" in list(response_2.json().values()))
                delete_1 = requests.delete(Constants.DELETE_USER_URL, headers={'Authorization': accessToken})
