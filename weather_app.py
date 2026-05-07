import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

city = input("Enter a City: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)

data = response.json()

if response.status_code == 200:
    temp = round(data["main"]["temp"])
    print(f"Temperature in {city}: {temp}°C")
else:
    print(f"Error: {data['message']}")