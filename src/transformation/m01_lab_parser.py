"""
Your Goal: Create src/transformation/m01_lab_parser.py. This script will:

Read the latest JSON file from data/raw/.

Extract the data.

Append it to a master CSV file in data/processed/user_registry.csv.
"""

import json
import csv
import os
import glob

def get_latest_file(path):
    # This finds the most recent .json file in your raw folder
    list_of_files = glob.glob(f'{path}/*.json')
    return max(list_of_files, key=os.path.getctime)

def transform_data():
    raw_folder = "data/raw"
    processed_file = "data/processed/user_registry.csv"
    
    # 1. Load the latest raw data
    latest_json = get_latest_file(raw_folder)
    print(f"📂 Reading latest raw file: {latest_json}") # Added
    with open(latest_json, 'r') as f:
        data = json.load(f)
    
    # 2. Structure for CSV
    # Note: We use a list because CSVs are row-based
    row = [data['email'], data['city'], data['age']]
    
    # 3. Save to CSV (Append Mode)
    file_exists = os.path.isfile(processed_file)
    with open(processed_file, 'a', newline='') as f:
        writer = csv.writer(f)
        # Add header only if the file is new
        if not file_exists:
            writer.writerow(['Email', 'City', 'Age'])
        writer.writerow(row)
        print(f"✅ Data appended to {processed_file}") # Added
        print(f"📊 Processed data: {row}") # Added

if __name__ == "__main__":
    transform_data()
    print("Transformation complete: Bronze to Silver achieved.")