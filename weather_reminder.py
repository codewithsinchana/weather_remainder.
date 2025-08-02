import requests

API_KEY = '96110236254d8c370a19b0e0bdc83c28'  
CITY = 'Bangalore'  
URL = f'https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'

def get_weather():
    try:
        response = requests.get(URL)
        if response.status_code == 200:
            data = response.json()
            temp = data['main']['temp']
            weather = data['weather'][0]['description']
            humidity = data['main']['humidity']
            return temp, weather, humidity
        else:
            print("❌ Error: Failed to fetch weather data. Check your API key or city name.")
            return None, None, None
    except Exception as e:
        print("❌ Exception occurred:", e)
        return None, None, None

def give_reminder(temp, weather, humidity):
    print(f"\n🌤️ Weather in {CITY}")
    print(f"Temperature: {temp}°C")
    print(f"Condition: {weather}")
    print(f"Humidity: {humidity}%")

    print("\n🔔 Reminders:")
    if 'rain' in weather.lower():
        print("• It's going to rain. Don't forget your umbrella ☔")
    if 'clear' in weather.lower():
        print("• Clear sky! Great time for a walk ☀️")
    if 'cloud' in weather.lower():
        print("• Overcast day. You may not need sunglasses ☁️")
    if temp > 35:
        print("• It's very hot! Stay hydrated 🥵")
    elif temp < 15:
        print("• It's cold. Wear warm clothes 🧥")
    if humidity > 80:
        print("• High humidity. Avoid drying clothes outside 🌫️")
    if all(cond not in weather.lower() for cond in ['rain', 'clear', 'cloud']):
        print("• Weather looks okay. Have a great day! 😊")

temp, weather, humidity = get_weather()
if temp is not None:
    give_reminder(temp, weather, humidity)
