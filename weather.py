import requests

api_key = "1638214d0c98fc61220c996a6e9f01a7"  # please, change the API KEY
base_url = "http://api.openweathermap.org/data/2.5/forecast?"
city_name = "London"  # write the name of the city you want the forecast
url = base_url + "appid=" + api_key + "&q=" + city_name  # URL format to execute the query

response = requests.get(url)

if response.status_code == 200:
    forecast_data = response.json()
    print(forecast_data)
    #print("Forecast")
    #print("-"*20)
    #print("City", forecast_data["name"])
    #print("Weather")
    #print("-" * 20)
    #print(forecast_data["weather"][0]["main"])
    #print(forecast_data["weather"][0]["description"])
    #print("Temp:", forecast_data["main"]["temp"])
    #print("Feels like:", forecast_data["main"]["feels_like"])
    #print("Temp min:", forecast_data["main"]["temp_min"])
    #print("Temp max:", forecast_data["main"]["temp_max"])
    #print("Pressure:", forecast_data["main"]["pressure"])
    #print("Humidity:", forecast_data["main"]["humidity"])
    #print("Visibility:", forecast_data["visibility"])
    #print("Wind")
    #print("-" * 20)
    #print("Speed:", forecast_data["wind"]["speed"])
    #print("Sunrise:", forecast_data["sys"]["sunrise"])
    #print("Sunset:", forecast_data["sys"]["sunset"])
    