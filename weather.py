import tkinter as tk
import requests

def get_weather():

    city = entry.get()

    api_key = "fa0367ace7bece093a98c84059d18837"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)

    data = response.json()

    if data["cod"] != 200:
        result.config(
            text="❌ City not found",
            fg="red"
        )

    else:
        temperature = data["main"]["temp"]

        humidity    = data["main"]["humidity"]

        condition = data["weather"][0]["main"]

        wind_speed = data["wind"]["speed"]

        result.config(
            text=f"""
🌦️ Weather: {condition}

🌡️ Temperature: {temperature}°C

💧 Humidity: {humidity}%

🌬️ Wind Speed: {wind_speed} km/h
""",
            fg="white"
        )

window = tk.Tk()

window.title("Weather App")

window.geometry("500x500")

window.config(bg="#1e1e1e")

title = tk.Label(
    window,
    text="🌦️ Weather Forecast App",
    font=("Arial", 22, "bold"),
    bg="#1e1e1e",
    fg="cyan"
)

title.pack(pady=20)

entry = tk.Entry(
    window,
    width=30,
    font=("Arial", 16)
)

entry.pack(pady=20)

button = tk.Button(
    window,
    text="Get Weather",
    font=("Arial", 14, "bold"),
    bg="cyan",
    fg="black",
    padx=10,
    pady=5,
    command=get_weather
)

button.pack(pady=20)

result = tk.Label(
    window,
    text="",
    font=("Arial", 16),
    bg="#1e1e1e",
    fg="white",
    justify="left"
)

result.pack(pady=20)

window.mainloop()