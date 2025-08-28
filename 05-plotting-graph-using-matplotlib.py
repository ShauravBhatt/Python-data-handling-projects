"""
Sample Data :

Date,City,Temperature,Condition
2025-06-11,Delhi,36.5,Clear
2025-06-12,Delhi,37.8,Sunny
2025-06-13,Delhi,38.0,Sunny
2025-06-14,Delhi,34.2,Rain
2025-06-15,Delhi,35.0,Clouds
2025-06-16,Delhi,33.4,Rain
2025-06-17,Delhi,34.7,Clear

Store this data in your pwd and then
Plot graph from this data !!

"""
import csv 
from collections import defaultdict
import matplotlib.pyplot as plt 

FILENAME = "data.csv"

def visualise_weather():
    dates = []
    temps = []
    conditions = defaultdict(int)
    
    with open(FILENAME , "r" , encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            try:
                dates.append(row['Date'])
                temps.append(float(row['Temperature']))
                conditions[row['Condition']] += 1
            except:
                continue 

        if not dates:
            print("No data is available there !!")
            return

        plt.figure(figsize=(10,7))
        plt.plot(dates, temps, marker='o')
        plt.title("Temperature over time !!")
        plt.xlabel("Date")
        plt.ylabel("Temperature")
        plt.tight_layout()
        plt.grid(True)
        plt.show()
        
        plt.figure(figsize=(7,5))        
        plt.bar(conditions.keys() , conditions.values() , color='red')
        plt.title("Condition over days !!")
        plt.xlabel("Conditions")
        plt.ylabel("Days")
        plt.show()

visualise_weather()

