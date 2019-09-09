#!/usr/bin/env python3
import requests
api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
city = 'Akademgorodok'
url = api_address + city
    
json_data = requests.get(url).json()
format_add = json_data['main']['temp']
format_add = round(format_add -273.15)
print(format_add)