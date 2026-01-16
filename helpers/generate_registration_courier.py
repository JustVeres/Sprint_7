import random
import string
import allure

@allure.step('Сгенерируем данные курьера')
def generate_couriers_data():
    """Генерирует рандомные данные для создания курьера"""
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for _ in range(length))
        return random_string

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    params = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    return params
