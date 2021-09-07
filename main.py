from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta

data_manager = DataManager()
sheet_data = data_manager.get_target_data()
origin_city_iata = "IST"
flight_search = FlightSearch()
# print(sheet_data[0])


if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_target_code(row["city"])


    data_manager.target_data = sheet_data
    data_manager.update_target_codes()


tomorrow = datetime.now() + timedelta(days=1)
six_month_later = datetime.now() + timedelta(days=6*30)

for target in sheet_data:
    flight = flight_search.check_flight(
        origin_city_iata,
        target["iataCode"],
        date_from=tomorrow,
        date_to=six_month_later
    )
