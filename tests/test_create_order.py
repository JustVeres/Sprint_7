import allure
import pytest
from api_methods.api_methods import ApiOrdersMethods as AOM
from data.data_orders import DataOrders

class TestCreateOrder:
    @allure.title('Создание заказа')
    @allure.description('Заказ создается с указанием одного цвета, двумя цветами, без указания цвета')
    @pytest.mark.parametrize('color', [ ['BLACK'], ['GREY'], ['BLACK', 'GREY'], [] ])
    def test_create_order(self, color):
        order_data=DataOrders.order_data(color)
        order_response = AOM.create_order(order_data)
        assert order_response.status_code == 201
        assert "track" in order_response.json()
        