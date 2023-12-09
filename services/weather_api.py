from config.config import api_key as token
import httpx


async def get_weather(city: str, units: str = None):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}'
    if units:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}&units={units}'

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()

    data = response.json()
    weather = data['main']

    return weather
