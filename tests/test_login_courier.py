import allure
import pytest
from helpers.create_params import Params
from data.data_couriers import DataCouriers as DC
from data.data_response_text import ResponseText as RT

class TestLoginCourier:
    @allure.title("Курьер может авторизоваться")
    @allure.description("Авторизация курьера со всеми обязательными полями")
    def test_authorisation_couriers(self, courier_api):
        with allure.step("Отправляем запрос на создание курьера"):
            _, _ = courier_api.create_courier()

        with allure.step("Проходим авторизацию"):
            status, text = courier_api.get_courier_id()

        with allure.step("Проверяем код ответа"):
            assert status == 200

        with allure.step("Проверяем наличие id в ответе"):
            assert 'id' in text and text['id'] is not None



    @allure.title("Нельзя авторизоваться под несуществующим курьером")
    @allure.description("Если передать несуществующие логин и пароль, сервис должен вернуть ошибку")
    def test_login_with_non_existing_user(self, courier_api):

        with allure.step("Проходим авторизацию"):
            status, body = courier_api.get_courier_id(DC.non_existing_courier)

        with allure.step("Проверяем код ответа"):
            assert status == 404

        with allure.step("Проверяем сообщение ошибки"):
            assert body["message"] == RT.courier_not_found



    @pytest.mark.parametrize(
        "field,value",
        [
            ("login", "wrong_login_123"),
            ("password", "wrong_password_123"),
        ],
        ids=["Неверный логин", "Неверный пароль"]
    )
    def test_login_with_wrong_credentials(self, courier_api, field, value):
        with allure.step("Готовим данные с неправильными данными"):
            params = Params.courier_log_pass_params().copy()
            params[field] = value

        with allure.step("Проходим авторизацию"):
            status, body = courier_api.get_courier_id(params)

        with allure.step("Проверяем код ответа"):
            assert status == 404

        with allure.step("Проверяем сообщение ошибки"):
            assert body["message"] == RT.courier_not_found
