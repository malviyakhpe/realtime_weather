import requests
import pytest

# Replace with your actual API key for weather data
API_KEY = "Your_API_KEY"

# Base URL for the Weather API endpoint
BASE_URL = "https://api.weatherapi.com/v1/current.json"

@pytest.mark.parametrize("city", ["Udaipur", "New York", "Tokyo"])
def test_get_weather_data(city):
    """
    Test function to fetch and verify weather data for a given city using the Weather API.  
    Parameters:
    city (str): The name of the city for which weather data is to be fetched.
    This function makes a GET request to the Weather API and checks:
    - The response status code is 200 (indicating success).
    - The response JSON does not contain an error.
    If the response is successful, it extracts and prints weather conditions,
    temperature, and wind speed for the specified city.
    """
    
    # Construct the request URL with the API key and city as query parameters
    url = f"{BASE_URL}?key={API_KEY}&q={city}"
    
    # Send the GET request to the Weather API
    response = requests.get(url)
    
    # Verify that the request was successful (status code 200)
    assert response.status_code == 200, f"Failed to fetch data for city: {city}"
    
    # Parse the response as JSON data
    data = response.json()
    
    # Verify that the response does not contain an "error" key
    assert "error" not in data, f"Error in API response for city: {city}"

    # Extract weather details from the response data
    weather = data["current"]["condition"]["text"]  # Current weather condition
    temp = data["current"]["temp_c"]  # Current temperature in Celsius
    wind = data["current"]["wind_kph"]  # Current wind speed in kph

    # Print the weather information for the specified city
    print(f"Weather in {city}: {weather}, Temperature: {temp}°C, Wind: {wind} kph")


