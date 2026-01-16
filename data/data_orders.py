import datetime

class DataOrders:
    @staticmethod
    def order_data(color):
        today_date = datetime.date.today()

        data = {
            "firstName": "Леон",
            "lastName": "Кеннеди",
            "address": "г.Москва",
            "metroStation": "Охотный ряд",
            "phone": "+79967772233",
            "rentTime": 7,
            "deliveryDate": f"{today_date}",
            "comment": "Ожидаю заказ",
            "color" : color
        }

        return data
