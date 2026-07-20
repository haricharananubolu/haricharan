import requests
import json
import time
from pathlib import Path
from typing import Optional, Dict

class WeatherAPI:
    def __init__(self, api_key: str, base_url: str = "https://api.openweathermap.org/data/2.5"):
        self.api_key = api_key
        self.base_url = base_url
        self.cache_dir = Path("data/cache")
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.cache_duration = 600  # 10 minutes cache duration

    def _get_cached_data(self, cache_key: str) -> Optional[Dict]:
        cache_file = self.cache_dir / f"{cache_key}.json"
        if cache_file.exists():
            cache_time = cache_file.stat().st_mtime
            if time.time() - cache_time < self.cache_duration:
                try:
                    with open(cache_file, 'r') as f:
                        return json.load(f)
                except:
                    pass
        return None

    def _save_to_cache(self, cache_key: str, data: Dict):
        try:
            with open(self.cache_dir / f"{cache_key}.json", 'w') as f:
                json.dump(data, f, indent=2)
        except:
            pass

    def _make_request(self, endpoint: str, params: Dict) -> Optional[Dict]:
        try:
            params['appid'] = self.api_key
            params['units'] = 'metric'  # Collect raw data in Metric Celsius
            
            response = requests.get(f"{self.base_url}/{endpoint}", params=params, timeout=10)
            
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 401:
                print("\n❌ Error: Invalid API key. Check your .env setup.")
            elif response.status_code == 404:
                print("\n❌ Error: City not found.")
            else:
                print(f"\n❌ Error: API failed with status {response.status_code}")
        except Exception as e:
            print(f"\n❌ Network Error: {e}")
        return None

    def get_current_weather(self, city: str) -> Optional[Dict]:
        cache_key = f"current_{city.lower().replace(' ', '_')}"
        cached = self._get_cached_data(cache_key)
        if cached:
            return cached
        
        data = self._make_request("weather", {'q': city})
        if data:
            self._save_to_cache(cache_key, data)
        return data

    def get_forecast(self, city: str) -> Optional[Dict]:
        cache_key = f"forecast_{city.lower().replace(' ', '_')}"
        cached = self._get_cached_data(cache_key)
        if cached:
            return cached
        
        data = self._make_request("forecast", {'q': city})
        if data:
            self._save_to_cache(cache_key, data)
        return data