import requests
from flight_data import FlightData

tequila_api = "MYAPI"
tequila_endpoint = "https://tequila-api.kiwi.com"


class FlightSearch:

    def get_target_code(self, city_name):
        location_endpoint = f"{tequila_endpoint}/locations/query"
        headers = {
        "apikey": tequila_api
        }
        query = {
            "term": city_name,
            "location_types": "city",
        }
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def check_flight(self, fly_from_code, fly_to_code, date_from, date_to):
        headers = {
            "apikey": tequila_api,
        }

        query = {
            "fly_from": fly_from_code,
            "fly_to": fly_to_code,
            "date_from": date_from.strftime("%d/%m/%Y"),
            "date_to": date_to.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "TRY"
        }

        response = requests.get(url=f"{tequila_endpoint}/v2/search", headers=headers, params=query)

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {fly_to_code}")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )

        print(f"{flight_data.destination_city}: {flight_data.price}TRY  Out_Date:{flight_data.out_date},"
              f"Return Date: {flight_data.return_date}")
        return flight_data


