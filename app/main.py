from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from services.weather_api import get_weather

app = FastAPI(title='Weather API', version='1.0.2')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_heades=['*']
)


@app.get('/')
async def index():
    return {'message': 'Use a /weather/{city} path to get a forecast for your city!'}


@app.get('/weather/{city}')
async def weather(city: str, units: str = 'metric'):
    forecast = [{'city': city}, await get_weather(city, units)]
    return forecast
