# Function to display the weather forecast for a city


def get_detailed_forecast(city):
    # Function to provide a detailed weather forecast for a city
    data = fetch_weather_data(city)
    return parse_weather_data(data)