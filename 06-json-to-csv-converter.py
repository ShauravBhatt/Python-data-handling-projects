"""
Challenge: JSON-to-Excel Converter Tool

Create a Python utility that reads structured data (like you'd get from an API) 
from a `.json` file and converts it to a CSV file that can be opened in Excel.

Your program should:
1. Read from a file named `api_data.json` in the same folder.
2. Convert the JSON content (a list of dictionaries) into `converted_data.csv`.
3. Automatically extract field names as CSV headers.
4. Handle nested structures by flattening or skipping them.

Sample Data:
[
  {
    "id": 101,
    "name": "Riya",
    "email": "riya@example.com",
    "location": "Delhi",
    "is_active": true
  },
  {
    "id": 102,
    "name": "Aman",
    "email": "aman@example.com",
    "location": "Mumbai",
    "is_active": false
  },
  {
    "id": 103,
    "name": "Neha",
    "email": "neha@example.com",
    "location": "Bangalore",
    "is_active": true
  },
  {
    "id": 104,
    "name": "raj",
    "email": "raj@example.com",
    "location": "Chennai",
    "is_active": true
  },
  {
    "id": 105,
    "name": "Simran",
    "email": "simran@example.com",
    "location": "Kolkata",
    "is_active": false
  }
]

Bonus:
- Provide feedback on how many records were converted
- Allow user to define which fields to extract
- Handle missing fields gracefully
"""

import json
import csv 
import os 

INPUT_FILE = 'api_data.json'
OUTPUT_FILE = 'converted_data.csv'

def load_json_data(filename):
    if not os.path.exists(filename):
        print("File not exists !!")
        return []
    with open(INPUT_FILE , "r" , encoding="utf-8") as f:
        try:
            return json.load(f)
        except:
            print("Invalid JSON Format !!")

def json_to_csv(data , filename):
    if not data:
        print("No data to convert !!")
        return []
    fieldname = list(data[0].keys())
    with open(filename , "w" , newline="" , encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames = fieldname)
        writer.writeheader()
        for record in data:
            writer.writerow(record)
    print(f"Converted {len(data)} records to {OUTPUT_FILE} !!")

def main():
    print("Converting JSON to CSV ...")
    data = load_json_data(INPUT_FILE)
    json_to_csv(data, OUTPUT_FILE)

if __name__ == "__main__":
    main()
