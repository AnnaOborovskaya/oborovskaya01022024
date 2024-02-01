import requests
from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse, FileResponse
from app.models.model import first_model, second_model, third_model
import hashlib
from typing import Union, Annotated
import json

weather_router = APIRouter()
open_weather = "80a4796ed267b015ea14d7cecf5dde57"
def get_weather_func(city, open_weather):
    r = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather}&units=metric")
    data = r.json()
    temperature = data["main"]["temp"]
    feels = data["main"]["feels_like"]
    wind = data["wind"]["speed"]
    visibility = data["visibility"]
    humidity = data["main"]["humidity"]
    return {'temperature':temperature, 'feels':feels, 'wind':wind, 'visibility':visibility, 'humidity':humidity}


@weather_router.get("/api/weather", response_model=Union[first_model])
def get_weather_one_city(city: str, parameter:str):
    """Вывести информцию о погоде по городу и определённым параметрам"""
    weather = first_model(city=city)
    param = parameter.split()
    d = {}
    func = get_weather_func(weather.city, open_weather)
    for i in param:
        d[i] = func[i]
    weather.parameters = json.loads(json.dumps(d))
    return weather


@weather_router.post("/api/weather", response_model=Union[second_model, first_model, list[first_model], list[second_model]])
def get_weather_some_cities(item: Annotated[second_model, Body(embed=True)]):
    """Вывести информцию о погоде по городам и определённым параметрам"""
    list_cities = []
    for one_city in item.city:
        weather = first_model(city=one_city)
        param = item.parameters.split()
        d = {}
        func = get_weather_func(weather.city, open_weather)
        for i in param:
            d[i] = func[i]
        weather.parameters = json.loads(json.dumps(d))
        list_cities.append(weather)
    return list_cities
