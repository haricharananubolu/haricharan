import sys
from weather_app.weather_parser import WeatherParser

class WeatherDisplay:
    # Simple Terminal Color Codes
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

    @classmethod
    def show_dashboard(cls, current: dict, forecast: list):
        """Prints a cleanly formatted weather screen inside terminal"""
        emoji = WeatherParser.get_emoji(current["condition"])
        
        print(f"\n{cls.YELLOW}{cls.BOLD}{emoji}  WEATHER DASHBOARD{cls.RESET}")
        print("=======================")
        print(f"📍 Location:     {cls.BOLD}{current['city']}, {current['country']}{cls.RESET}")
        print(f"🕐 Last Updated: {current['timestamp']}")
        print("\nCurrent Weather:")
        print("────────────────")
        print(f"Temperature:   {cls.BLUE}{current['temp']}°C{cls.RESET} (Feels like: {current['feels_like']}°C)")
        print(f"Conditions:    {current['description']} {emoji}")
        print(f"Humidity:      {current['humidity']}%")
        print(f"Wind:          {current['wind_speed']} km/h")
        print(f"Pressure:      {current['pressure']} hPa")
        print(f"Sun Movement:  🌅 {current['sunrise']}  /  🌇 {current['sunset']}\n")
        
        print("5-Day Forecast:")
        print("───────────────")
        for day in forecast:
            day_emoji = WeatherParser.get_emoji(day["condition"])
            print(f"{day['date']}:  {day_emoji}   {cls.BLUE}{day['temp']}°C{cls.RESET}  (Humidity: {day['humidity']}%)")
        print("────────────────")