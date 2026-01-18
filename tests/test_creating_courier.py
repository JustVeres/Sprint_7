import allure
import pytest

from helpers.create_params import Params
from data.data_response_text import ResponseText as RT

class TestCreatingCourier:
    @allure.title("Создание курьера")
    @allure.description(
        "Проверяет, что курьер успешно создаётся, "
        "API возвращает статус 201 и тело ответа {\"ok\": true}."
    )
    def test_can_create_courier(self, courier_api):
        with allure.step("Отправляем запрос на создание курьера"):
            status, text = courier_api.create_courier()

        with allure.step("Проверяем код ответа"):
            assert status == 201

        with allure.step("Проверяем тело ответа"):
            assert text == RT.creating_courier



    @allure.title("Создание двух одинаковых курьеров")
    @allure.description("Одинаковый курьер не создается")
    def test_cant_create_two_identical_couriers(self, courier_api):
        with allure.step("Отправляем первый запрос на создание курьера"):
            _, _ = courier_api.create_courier()

        with allure.step("Отправляем второй запрос на создание курьера"):
            status_2, text_2 = courier_api.create_courier()

        with allure.step("Проверяем код ответа"):
            assert status_2 == 409

        with allure.step("Проверяем тело ответа"):
            assert text_2['message'] == RT.two_identical_couriers


    @allure.title("Курьера можно создать с обязательными полями login и password")
    @allure.description("Курьер создается с login и password")
    def test_create_courier_with_required_fields(self, courier_api):
        with allure.step("Отправляем запрос на создание курьера с логином и паролем"):
            status, text = courier_api.create_courier_with_required_fields()
        with allure.step("Проверяем код ответа"):
            assert status == 201
        with allure.step("Проверяем тело ответа"):
            assert text == RT.creating_courier


    @allure.title("Курьера невозможно создать без обязательных полей")
    @allure.description("Если не передать login или password, сервис должен вернуть ошибку")
    @pytest.mark.parametrize(
        'empty_field',
        ['login', 'password'],
        ids=['Без логина', 'Без пароля']
    )
    def test_create_courier_without_required_fields(self, courier_api, empty_field):

        with allure.step(f"Готовим данные без поля: {empty_field}"):
            params = Params.create_new_courier_params().copy()
            params.pop(empty_field)

        with allure.step("Отправляем запрос"):
            status, body = courier_api.create_courier(params)

        with allure.step("Проверяем код"):
            assert status == 400

        with allure.step("Проверяем сообщение"):
            assert body["message"] == RT.not_enough_data
