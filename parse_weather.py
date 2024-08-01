# Function to parse weather data

class ParseData:
    def parse_data(data):
    
        if not data:
            return "Weather data not available"
        else:
            city = data["city"]
            temperature = data["temperature"]
            condition = data["condition"]
            humidity = data["humidity"]
            return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"

    def get_detailed_forecast(city):
     
        data = getcity.fetch_weather_data(city)
        return parse_weather_data(data)

   
  
