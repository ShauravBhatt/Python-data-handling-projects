'''
Challenge: CSV-to-JSON Converter Tool

Create a Python utility that reads tabular data from a .csv file
and converts it into a .json file (structured like API data).

Requirements:
1. Read from a file named converted_data.csv in the same folder.
2. Convert the CSV content (rows of data) into converted_data.json.
3. Automatically use the first row of the CSV as field names (headers).
4. Ensure all values are correctly mapped under their respective keys.

Sample CSV (converted_data.csv):
id,name,email,location,is_active
101,Riya,riya@example.com,Delhi,True
102,Aman,aman@example.com,Mumbai,False
103,Neha,neha@example.com,Bangalore,True
104,Raj,raj@example.com,Chennai,True
105,Simran,simran@example.com,Kolkata,False

Bonus Features:
- Provide feedback on how many records were converted.
- Allow the user to pretty-print JSON (indented format).
- Handle missing or extra fields gracefully.
'''

import json
import csv 
import os 

INPUT_FILE = "converted_data.csv"
OUTPUT_FILE = "converted_data.json"

def load_csv_data(filename):
    if not os.path.exists(filename):
        print("\nCSV file not found !!")
        return []

    with open(filename , "r" , encoding="utf-8") as f:
        reader = csv.DictReader(f)
        data = list(reader)
        return data 

def csv_to_json(data, filename):
    if not data:
        print("\nThere is no data to convert !!")
        return []
    
    with open(filename , "w" , encoding="utf-8") as f:
        json.dump(data, f ,indent=4)
    print(f"\nConverted {len(data)} records to {filename} !!")

def preview_data(data , count):
    for row in data[:count]:
        print()
        print(json.dumps(row, indent=2))
    print(".....")

def main():
    data = load_csv_data(INPUT_FILE)
    if not data:
        return 
    csv_to_json(data, OUTPUT_FILE)
    choice = input("\nWant to preview data (y/n) : ").strip().lower()
    if choice == "y":
        row = int(input("\nEnter how much rows you wanna preview: ").strip())
        preview_data(data,row)


if __name__ == "__main__":
    main()



