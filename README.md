# Sprint_7
Проект 7 спринта, 28_qa-python

```text
Sprint_7/
│── allure-results/                             # Отчёты Allure
│
├── api_methods/
│   └── api_methods.py                          # Методы взаимодействия с api
│
├── data/
│   ├── data_couriers.py                        # Тестовые данные для курьеров
│   └── data_orders.py                          # Тестовые данные для заказов
│   └── data_response_text.py                   # Тестовые данные для ответов на запросы
│   └── data_urls.py                            # Тестовые данные с url и endpoints
│
├── helpers/
│   ├── create_params.py                        # Логика, создающая параметры для авторизации курьера
│   └── generate_registration_courier.py        # Логика для генерации данных курьера
│
├── tests/
│   ├── test_create_order.py                    # Тесты на создание заказа
│   ├── test_creating_courier.py                # Тесты на сощдание курьера
│   ├── test_list_of_orders.py                  # Тесты на получения списка заказов
│   └── test_login_courier.py                   # Тесты на ligin курьера
│
├── requirements.txt                            # Подключённые библиотеки
├── conftest.py                                 # Фикстуры pytest
└── README.md                                   # Описание проекта
