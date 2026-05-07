import requests

API_KEY = "4ecc9be25b75d2858474b9ceeb0ab4fc"

city = input("Enter a City: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)

data = response.json()

if response.status_code == 200:
    temp = round(data["main"]["temp"])
    print(f"Temperature in {city}: {temp}°C")
else:
    print(f"Error: {data['message']}")