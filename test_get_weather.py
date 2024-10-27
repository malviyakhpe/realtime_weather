import requests
import pytest

API_KEY = "Your_API_KEY"
BASE_URL = "https://api.weatherapi.com/v1/current.json"

@pytest.mark.parametrize("city", ["Udaipur", "New York", "Tokyo"])
def test_get_weather_data(city):
    url = f"{BASE_URL}?key={API_KEY}&q={city}"
    
    response = requests.get(url)
    assert response.status_code == 200, f"Failed to fetch data for city: {city}"
    
    data = response.json()
    assert "error" not in data, f"Error in API response for city: {city}"

    weather = data["current"]["condition"]["text"]
    temp = data["current"]["temp_c"]
    wind = data["current"]["wind_kph"]

    print(f"Weather in {city}: {weather}, Temperature: {temp}°C, Wind: {wind} kph")
