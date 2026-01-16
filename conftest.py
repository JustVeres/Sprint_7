import pytest
from api_methods.api_methods import ApiCourierMethods

@pytest.fixture
def courier_api():
    api = ApiCourierMethods()
    yield api
    if api.created:
        api.delete_courier()

