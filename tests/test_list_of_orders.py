import allure
from api_methods.api_methods import ApiOrdersMethods as AOM

class TestGetOrders:

    @allure.title("Проверка получения списка заказов")
    @allure.description("Убедимся, что GET /orders возвращает список заказов в поле 'orders'")
    def test_orders_list(self):
        with allure.step("Отправляем GET запрос на получение списка заказов"):
            status, body = AOM.get_orders()

        with allure.step("Проверяем код ответа"):
            assert status == 200, f"Ожидаем 200 OK, получили {status}"

        with allure.step("Проверяем наличие поля 'orders'"):
            assert "orders" in body, "'orders' отсутствует в ответе API"

        with allure.step("Проверяем, что это список"):
            assert isinstance(body["orders"], list), "'orders' не является списком"

        with allure.step("Проверяем, что список заказов не пустой"):
            assert len(body["orders"]) > 0, "Список заказов пустой"
