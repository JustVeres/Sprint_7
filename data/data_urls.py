class Urls:
    BASE_URL = "https://qa-scooter.praktikum-services.ru/"

class ApiEndpoints:
    COURIERS_LOGIN_IN_THE_SYSTEM_ENDPOINT = "api/v1/courier/login" # Courier - Логин курьера в системе
    CREATING_COURIER_ENDPOINT = "api/v1/courier" # Courier - Создание курьера
    DELETE_COURIER_ENDPOINT = "api/v1/courier/" # Courier - Удаление курьера (без id)
    CREATE_ORDER_ENDPOINT = "api/v1/orders" # Orders - Создание заказа
    ORDERS_ENDPOINT= "api/v1/orders" # Orders - Получение списка заказов

class TotalUrl:
    CREATE_COURIER_URL = Urls.BASE_URL + ApiEndpoints.CREATING_COURIER_ENDPOINT # Создание курьера
    LOGIN_IN_THE_SYSTEM_URL = Urls.BASE_URL + ApiEndpoints.COURIERS_LOGIN_IN_THE_SYSTEM_ENDPOINT # Получаем логин и id курьера
    DELETE_COURIER_URL = Urls.BASE_URL + ApiEndpoints.DELETE_COURIER_ENDPOINT # Удаление курьера
    CREATING_ORDER_URL = Urls.BASE_URL + ApiEndpoints.CREATE_ORDER_ENDPOINT # Создание заказа
    ORDERS_URL = Urls.BASE_URL +ApiEndpoints.ORDERS_ENDPOINT # Получение списка заказов
