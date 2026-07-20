from datetime import datetime

class WeatherParser:
    # Maps internal OpenWeather icon names/conditions to clear terminal emojis
    ICON_MAPPING = {
        "Thunderstorm": "⛈️",
        "Drizzle": "🌧️",
        "Rain": "🌧️",
        "Snow": "❄️",
        "Clear": "☀️",
        "Clouds": "☁️",
        "Mist": "🌫️",
        "Haze": "🌫️",
    }

    @staticmethod
    def get_emoji(condition: str) -> str:
        return WeatherParser.ICON_MAPPING.get(condition, "🌤️")

    @classmethod
    def parse_current(cls, data: dict) -> dict:
        """Flattens raw JSON data for current conditions"""
        sys_data = data.get("sys", {})
        weather_main = data.get("weather", [{}])[0]
        
        return {
            "city": data.get("name"),
            "country": sys_data.get("country"),
            "temp": round(data["main"]["temp"]),
            "feels_like": round(data["main"]["feels_like"]),
            "humidity": data["main"]["humidity"],
            "pressure": data["main"]["pressure"],
            "wind_speed": round(data["wind"]["speed"] * 3.6), # Convert m/s to km/h
            "condition": weather_main.get("main", "Unknown"),
            "description": weather_main.get("description", "").capitalize(),
            "sunrise": datetime.fromtimestamp(sys_data.get("sunrise", 0)).strftime("%H:%M"),
            "sunset": datetime.fromtimestamp(sys_data.get("sunset", 0)).strftime("%H:%M"),
            "timestamp": datetime.fromtimestamp(data.get("dt", 0)).strftime("%Y-%m-%d %H:%M:%S")
        }

    @classmethod
    def parse_forecast(cls, data: dict) -> list:
        """Extracts 5 distinct daily items from the 3-hour interval data list"""
        parsed_days = []
        seen_dates = set()
        
        for item in data.get("list", []):
            dt_obj = datetime.fromtimestamp(item["dt"])
            date_str = dt_obj.strftime("%a %d %b")
            
            # OpenWeather gives data every 3 hours. We pick the first one per unique day.
            if date_str not in seen_dates:
                seen_dates.add(date_str)
                weather_main = item.get("weather", [{}])[0]
                
                parsed_days.append({
                    "date": date_str,
                    "temp": round(item["main"]["temp"]),
                    "humidity": item["main"]["humidity"],
                    "condition": weather_main.get("main", "Unknown")
                })
            if len(parsed_days) >= 5:
                break
        return parsed_days