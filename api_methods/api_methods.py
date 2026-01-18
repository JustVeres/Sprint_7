import allure
import requests
from helpers.create_params import Params
from data.data_urls import TotalUrl

class ApiCourierMethods:

    def __init__(self):
        self.created = None

    @allure.step("Авторизоваться курьером")
    def get_courier_id(self, params=None):
        if params is None:
            params = Params.courier_log_pass_params()
        response = requests.post(TotalUrl.LOGIN_IN_THE_SYSTEM_URL, json=params)
        return response.status_code, response.json()

    @allure.step("Создать курьера")
    def create_courier(self, params=None):
        if params is None:
            params = Params.create_new_courier_params()
    
        response = requests.post(TotalUrl.CREATE_COURIER_URL, json=params)
    
        if response.status_code == 201:
            self.created = True
    
        return response.status_code, response.json()

    @allure.step("Создать курьера с логином и паролем")
    def create_courier_with_required_fields(self):
        response = requests.post(
            TotalUrl.CREATE_COURIER_URL,
            json=Params.courier_log_pass_params()
        )
        return response.status_code, response.json()

    @allure.step("Удалить курьера")
    def delete_courier(self):
        _, id_response = self.get_courier_id()
        courier_id = id_response["id"]

        response = requests.delete(
            TotalUrl.DELETE_COURIER_URL + str(courier_id)
        )
        return response.status_code, response.json()

class ApiOrdersMethods:
    @staticmethod
    @allure.step("Создать заказ")
    def create_order(order_data):
        return requests.post(TotalUrl.CREATING_ORDER_URL, json=order_data)

    @staticmethod
    @allure.step("Получить список всех заказов")
    def get_orders():
        response = requests.get(TotalUrl.ORDERS_URL)
        return response.status_code, response.json()
