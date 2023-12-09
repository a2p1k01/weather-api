from fastapi import FastAPI
from services.weather_api import get_weather

app = FastAPI(title='Weather API')


@app.get('/')
async def index():
    return {'message': 'Use a /weather/{city} path to get a forecast for your city!'}


@app.get('/weather/{city}')
async def weather(city: str, units: str = 'metric'):
    forecast = [{'city': city}, await get_weather(city, units)]
    return forecast
