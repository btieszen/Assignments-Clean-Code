#1. Refactoring a Weather Forecast Application into Classes and Modules
#dentifying and Creating Classes Analyze the provided script and identify distinct functionalities 
# that can be encapsulated into classes. Create classes that represent different aspects of the weather forecast
# application, such as fetching data, parsing data, and user interaction.
#Clear definitions of classes such as `WeatherDataFetcher`, `DataParser`, and `UserInterface`, each handling specific parts of the application.

import getcity
import parse_weather


class WeatherDataFetcher:
    def weather_data(city):
        getcity.fetch_weather_data(city)
    
class DataParser:
    def parse_weather_data(data):
        from parse_weather import ParseData


class UserInterface:
    def main():
        while True:
            city = input("Enter the city(New York,London,Tokyo) to get the weather forecast or 'exit' to quit: ")
            if city.lower() == 'exit':
                break
        
            else:
                forecast= getcity.fetch_weather_data(city)
            print(forecast)

    if __name__ == "__main__":
        main()