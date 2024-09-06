import allure
import requests
from constants import Constants

class TestGetOrder:
    @allure.title('Позитивный тест получение списка заказов c авторизацией')
    @allure.description('Позитивный тест. Получение в тело ответа. code == 200 и наличия в ответе "order"')
    def test_get_order_with_auth(self, new_user):
        user = new_user
        response_1 = requests.post(Constants.REGISTRATION_USER_URL, json=user)
        accessToken_1 = list(response_1.json().values())[2]
        requests.post(Constants.LOGIN_USER_URL, json=user)
        response_3 = requests.get(Constants.CREATING_ORDER_URL, headers={'Authorization': accessToken_1})
        assert response_3.status_code == 200 and ('orders' in list(response_3.json()))
        requests.delete(Constants.DELETE_USER_URL, headers={'Authorization': accessToken_1})

    @allure.title('Позитивный тест получение списка заказов ,без авторизации')
    @allure.description('Позитивный тест. Получение в тело ответа. code == 200 и наличия в ответе "You should be authorised"')
    def test_get_order_without_auth(self, new_user):
        user = new_user
        response_1 = requests.post(Constants.REGISTRATION_USER_URL, json=user)
        accessToken_1 = list(response_1.json().values())[2]
        requests.post(Constants.LOGIN_USER_URL, json=user)
        response_3 = requests.get(Constants.CREATING_ORDER_URL)
        assert response_3.status_code == 401 and ('You should be authorised' in list(response_3.json().values()))
        requests.delete(Constants.DELETE_USER_URL, headers={'Authorization': accessToken_1})