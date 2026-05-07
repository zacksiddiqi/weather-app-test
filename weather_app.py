import tkinter as tk
import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

def get_weather():
    city = entry.get()

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    data = response.json()

    if response.status_code == 200:
        temp = round(data["main"]["temp"])
        result_label.config(text=f"The current tempurature in {city} is {temp}°C")
    else:
        result_label.config(text="city not found")


window = tk.Tk()
window.title("Zack's Weather App")
window.geometry("350x250")
 

label = tk.Label(window, text="Enter a City: ", font=("Arial", 14))
label.pack(pady=10)

entry = tk.Entry(window, font=("Arial", 14))
entry.pack(pady=10)

button = tk.Button(window, text="Get Temp", command=get_weather)
button.pack()

city_label = tk.Label(window, text="", font=("Arial", 14))
city_label.pack(pady=5)

result_label = tk.Label(window, text="", font=("Arial", 12, "bold"))
result_label.pack()



window.mainloop()