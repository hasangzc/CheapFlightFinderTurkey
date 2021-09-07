import requests
sheety_prices_endpoints = "MYENDPOINT"


class DataManager:
    def __init__(self):
        self.target_data = {}

    def get_target_data(self):
        response = requests.get(url=sheety_prices_endpoints)
        data = response.json()
        self.target_data = data["price"]
        return self.target_data

    def update_target_codes(self):
        for city in self.target_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{sheety_prices_endpoints}/{id}", json=new_data)
            return response.json()
