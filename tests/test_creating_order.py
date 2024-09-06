import allure
import requests
from constants import Constants


class TestCreatingOrder:

    @allure.title('Позитивный тест создание заказа c авторизацией и ингредиентами')
    @allure.description('Позитивный тест. Получение в тело ответа. code == 200 и наличия в ответе "order"')
    def test_creating_order_with_author_and_ingredients(self, new_user):
        user = new_user
        order_ingredients = {'ingredients': [Constants.HASH_INGREDIENT_FLUO_BUN, Constants.HASH_INGREDIENT_MEAT_MOLLUSC]}
        response_1 = requests.post(Constants.REGISTRATION_USER_URL, json=user)
        accessToken_1 = list(response_1.json().values())[2]
        requests.post(Constants.LOGIN_USER_URL, json=user)
        response_3 = requests.post(Constants.CREATING_ORDER_URL, json=order_ingredients, headers={'Authorization': accessToken_1})
        assert response_3.status_code == 200 and ('order' in list(response_3.json()))
        requests.delete(Constants.DELETE_USER_URL, headers={'Authorization': accessToken_1})



    @allure.title('Позитивный тест создание заказа без авторизации')
    @allure.description('Позитивный тест. Получение в тело ответа. code == 200 и наличия в ответе "order"')
    def test_creating_order_without_author_with_ingredients(self, new_user):
        user = new_user
        order_ingredients = {'ingredients': [Constants.HASH_INGREDIENT_FLUO_BUN, Constants.HASH_INGREDIENT_MEAT_MOLLUSC]}
        response_1 = requests.post(Constants.REGISTRATION_USER_URL, json=user)
        accessToken_1 = list(response_1.json().values())[2]
        requests.post(Constants.LOGIN_USER_URL, json=user)
        response_3 = requests.post(Constants.CREATING_ORDER_URL, json=order_ingredients)
        assert response_3.status_code == 200 and ('order' in list(response_3.json()))
        requests.delete(Constants.DELETE_USER_URL, headers={'Authorization': accessToken_1})


    @allure.title('Негативный  тест создание заказа без авторизации ,без ингредиентов')
    @allure.description('Негативный тест. Получение в тело ответа. code == 400 и наличия в ответе "Ingredient ids must be provided"')
    def test_creating_order_without_author_without_ingredients(self, new_user):
        user = new_user

        response_1 = requests.post(Constants.REGISTRATION_USER_URL, json=user)
        accessToken_1 = list(response_1.json().values())[2]
        requests.post(Constants.LOGIN_USER_URL, json=user)
        response_3 = requests.post(Constants.CREATING_ORDER_URL)
        assert response_3.status_code == 400 and ("Ingredient ids must be provided" in list(response_3.json().values()))
        requests.delete(Constants.DELETE_USER_URL, headers={'Authorization': accessToken_1})


    @allure.title('Негативный  тест создание заказа без авторизации с неверным хешем ингредиента')
    @allure.description('Позитивный тест. Получение в тело ответа. code == 500  ')
    def test_creating_order_without_author_with_wrong_ingredients(self, new_user):
        user = new_user
        order_ingredients = {'ingredients': [Constants.HASH_INGREDIENT_FLUO_BUN, 'erroringredienthash']}
        response_1 = requests.post(Constants.REGISTRATION_USER_URL, json=user)
        accessToken_1 = list(response_1.json().values())[2]
        requests.post(Constants.LOGIN_USER_URL, json=user)
        response_3 = requests.post(Constants.CREATING_ORDER_URL, json=order_ingredients)
        assert response_3.status_code == 500
        requests.delete(Constants.DELETE_USER_URL, headers={'Authorization': accessToken_1})


