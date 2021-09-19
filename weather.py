import requests
import json

location= input("Şehir arayınız:")
endpoint= "https://www.metaweather.com/api/location/search/?query={}".format(location)
response= requests.get(endpoint)

def filter_cities(response):
    cities= list(filter(lambda x: x.get("location_type")== 'City', response))
    return cities

def print_cities(cities):
    for id, city in enumerate(cities):
        print("{} - {}".format(id, city.get("title")))


def forecast(woeid):
    endpoint_forecasting= "https://www.metaweather.com/api/location/{}/".format(woeid)
    response= requests.get(endpoint_forecasting)
    response_to_json= json.loads(response.content)
    consolidated_weather= response_to_json.get("consolidated_weather")
    return consolidated_weather
    


if response.status_code == 200:
    convert_to_dict= json.loads(response.content)
    cities= filter_cities(convert_to_dict)
    print_cities(cities)

    city_id= int(input("Şehir kodu seçiniz:"))
    city= cities[city_id]
    city_woeid= city.get("woeid")


    forecasting_result= forecast(city_woeid)

    for weather in forecasting_result:
        print(weather.get("applicable_date"), weather.get("weather_state_name"))

