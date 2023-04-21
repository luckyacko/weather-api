import requests
class NetworkService:
    def __init__(self):
        self.api_key = "dcea23fa697c4940b63135524232104"
        ##"http://api.weatherapi.com/v1/forecast.json?key=dcea23fa697c4940b63135524232104&q=London&days=1&aqi=no&alerts=no"

    def lookup_weather(self, city):
        respons =requests.get(f"http://api.weatherapi.com/v1/forecast.json?key={self.api_key}&q={city}&days=1&aqi=no&alerts=no")
        if respons.status_code == 200:
            data = respons.json()
            current_condition = data["current"]["condition"]["text"]
            print(f"Current condition: {current_condition}")
            print()
        else:
            print(f"Sorry, the city '{city}' does not exist")