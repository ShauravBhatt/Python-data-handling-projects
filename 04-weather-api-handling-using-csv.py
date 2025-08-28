"""
 Challenge: Real-Time Weather Logger (API + CSV)

Build a Python CLI tool that fetches real-time weather data for a given city and logs it to a CSV file for daily tracking.

Your program should:
1. Ask the user for a city name.
2. Fetch weather data using the OpenWeatherMap API.
3. Store the following in a CSV file (`weather_log.csv`):
   - Date (auto-filled as today's date)
   - City
   - Temperature (in °C)
   - Weather condition (e.g., Clear, Rain)
4. Prevent duplicate entries for the same city on the same day.
5. Allow users to:
   - Add new weather log
   - View all logs
   - Show average, highest, lowest temperatures, and most frequent condition

Bonus:
- Format the output like a table
- Handle API failures and invalid city names gracefully
"""

import csv
import os
from datetime import datetime
import requests
from collections import Counter

FILENAME = "weather_log.csv"
API_KEY = "8c1f4061ce8231a37ed9cbb7ba81404e"

if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "City", "Temperature", "Condition"])

def log_weather():
    city = input("\nEnter the city name: ").strip().lower()
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if not city:
        print("\nEnter valid name !!")
        return

    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['City'].lower() == city or row['Date'] == date:
                print("\nEntry for this city or time already exists !!")
                return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            city = data['name']
            temperature = round(data['main']['temp'] - 273, 2)
            condition = data['weather'][0]['main']

            with open(FILENAME, "a", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow([date, city, temperature, condition])

            print(f"\nLogged weather for {city.title()} : {temperature}°C , {condition} !!")

        elif response.status_code == 404:
            print("\nCity not found !!")
        elif response.status_code == 401:
            print("\nInvalid API Key !!")
        else:
            print("\nFailed to fetch data. Status Code:", response.status_code, response.reason)

    except requests.exceptions.RequestException as e:
        print("\nError during request:", e)

def view_log():
    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

        if not rows:
            print("\nNothing there !!")
            return

        print("\n--- All Weather Logs ---\n")
        for row in rows:
            print(f"{row['Date']} : {row['City']} | {row['Temperature']}°C | {row['Condition']}")
    print()

def log_analysis():
    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    if not rows:
        print("\nNo data is there for analysis !!")
        return 

    temperatures = [float(row['Temperature']) for row in rows]
    conditions = [row['Condition'] for row in rows]

    counter = Counter(conditions)
    most_common = counter.most_common(1)

    if most_common:
        condition, count = most_common[0]
    else:
        condition, count = "N/A", 0

    print("\n--- Analysis based on logs ---\n")
    print(f"Maximum temperature : {max(temperatures)}°C")
    print(f"Minimum temperature : {min(temperatures)}°C")
    print(f"Average temperature : {round(sum(temperatures)/len(temperatures), 2)}°C")
    print(f"Most common weather condition : {condition} ({count} times)")

def main():
    while True:
        print(f"\n{'-'*15} Welcome to Real-Time Weather Logger {'-'*15}")
        print("1. Add Weather Log")
        print("2. View All Logs")
        print("3. Get Log Analysis")
        print("4. Exit")

        choice = input("\nEnter the choice (1-4): ").strip()

        match choice:
            case "1":
                log_weather()
            case "2":
                view_log()
            case "3":
                log_analysis()
            case "4":
                print("\nExited successfully !!")
                break
            case _:
                print("\nInvalid Choice !!")

if __name__ == "__main__":
    main()
