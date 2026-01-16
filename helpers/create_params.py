from helpers import generate_registration_courier

class Params:
    _courier_data = None

    @staticmethod
    def create_new_courier_params():
        if Params._courier_data is None:
            data = generate_registration_courier.generate_couriers_data()
            Params._courier_data = {
                "login": data["login"],
                "password": data["password"],
                "firstName": data["firstName"]
            }
        return Params._courier_data

    @staticmethod
    def courier_log_pass_params():
        data = Params.create_new_courier_params()
        return {
            "login": data["login"],
            "password": data["password"]
        }
