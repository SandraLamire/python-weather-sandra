from dotenv import load_dotenv
from pprint import pprint
import requests
import os


load_dotenv()

def get_current_weather(city="Rennes"):
    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric&lang=fr'
    
    weather_data = requests.get(request_url).json()
    
    return weather_data

if __name__ == "__main__":
    print('\n*** Météo actuelle ***\n')
    city = input("\nEntrer le nom d'une ville (Rennes par défaut): ")
    
    # Check for empty string or sting with only spaces
    if not bool(city.strip()):
        city = "Rennes (par défaut)"
            
    weather_data = get_current_weather(city)
    print("\n")
    pprint(weather_data)
    