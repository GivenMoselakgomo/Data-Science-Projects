# -*- coding: utf-8 -*-
"""
Created on Thu Dec  4 10:25:28 2025

@author: givenmo
"""
import requests

def get_city_from_ip():
    """Get your city name using your IP address."""
    try:
        response = requests.get("https://ipinfo.io/", timeout=5)
        data = response.json()
        return data.get("city")
    except:
        return None


def get_weather_short(city: str):
    """Get a one-line weather summary."""
    try:
        url = f"https://wttr.in/{city}?format=3"
        response = requests.get(url, timeout=50)
        return response.text
    except Exception as e:
        return f"Error: {e}"


def get_weather_full(city: str):
    """Get the full ASCII weather report."""
    try:
        url = f"https://wttr.in/{city}"
        response = requests.get(url, timeout=10)
        return response.text
    except Exception as e:
        return f"Error: {e}"


def main():
    print("=" * 50)
    print("🌦 WEATHER PROJECT — WTTR METHOD")
    print("=" * 50)

 
    city = get_city_from_ip()

    if city:
        print(f"\n📍 Detected your location as: {city}")
        use_it = input("Use this city? (y/n): ").lower()

        if use_it != "y":
            city = input("\nEnter a city name: ")
    else:
        print("\n⚠ Could not detect your city.")
        city = input("Enter a city name: ")


    print("\n" + "=" * 50)
    print("🌤 SHORT WEATHER SUMMARY")
    print("=" * 50)
    print(get_weather_short(city))

  
    print("\n" + "=" * 50)
    print("📜 FULL WEATHER REPORT")
    print("=" * 50)
    print(get_weather_full(city))


if __name__ == "__main__":
    main()

