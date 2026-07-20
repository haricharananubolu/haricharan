import sys
from weather_app.config import API_KEY
from weather_app.weather_api import WeatherAPI
from weather_app.weather_parser import WeatherParser
from weather_app.weather_display import WeatherDisplay

def main():
    if not API_KEY or "your_api_key" in API_KEY:
        print("❌ CRITICAL: Please update your .env file with a valid API Key from OpenWeatherMap.")
        sys.exit(1)
        
    api = WeatherAPI(api_key=API_KEY)
    current_city = "London"  # Default startup city
    
    while True:
        # Fetch operations
        raw_current = api.get_current_weather(current_city)
        raw_forecast = api.get_forecast(current_city)
        
        if raw_current and raw_forecast:
            parsed_current = WeatherParser.parse_current(raw_current)
            parsed_forecast = WeatherParser.parse_forecast(raw_forecast)
            
            # Render View
            WeatherDisplay.show_dashboard(parsed_current, parsed_forecast)
        else:
            print("⚠️ Could not fetch complete weather profiles for your query.")

        # User Input Interaction block
        user_choice = input("\nType 'refresh' to update, 'search' for a new city, or 'quit': ").strip().lower()
        
        if user_choice == 'quit':
            print("Thank you for using the Weather Dashboard. Goodbye!")
            break
        elif user_choice == 'refresh':
            print(f"Refreshing data for {current_city}...")
            # Forcing network fetch by ignoring cache could be done here, or let cache expire naturally
            continue
        elif user_choice == 'search':
            new_city = input("Enter city name: ").strip()
            if new_city:
                current_city = new_city
        else:
            print("Invalid instruction. Defaulting back to home loop.")

if __name__ == "__main__":
    main()