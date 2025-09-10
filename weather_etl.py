import requests
import pandas as pd
import mysql.connector
import json
from datetime import datetime

# ---------------------------
# Load DB config
# ---------------------------
with open(r"C:\Users\Brylle\Desktop\Jupyter Projects\Weather-ETL-with-Python-MySQL\db_config.json") as f:
    config = json.load(f)

# ---------------------------
# Load Weather API config
# ---------------------------
with open(r"C:\Users\Brylle\Desktop\Jupyter Projects\Weather-ETL-with-Python-MySQL\config.json") as f:
    secrets = json.load(f)

API_KEY = secrets["api_key"]

# List of cities to fetch
CITIES = ["Manila", "Tokyo", "New York", "London", "Sydney"]

# ---------------------------
# Extract
# ---------------------------
def extract(cities):
    results = []
    for city in cities:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
        response = requests.get(url)
        print(f"Fetching {city}: {response.status_code}")
        if response.status_code == 200:
            results.append(response.json())
        else:
            print(f"❌ Failed for {city}: {response.text}")
    return results

# ---------------------------
# Transform
# ---------------------------
def transform(data_list):
    records = []
    for data in data_list:
        record = {
            "city": data["name"],
            "country": data["sys"]["country"],
            "temperature_c": round(data["main"]["temp"] - 273.15, 2),  # Kelvin → Celsius
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "description": data["weather"][0]["description"],
            "timestamp": datetime.now()
        }
        records.append(record)
    return pd.DataFrame(records)

# ---------------------------
# Load
# ---------------------------
def load(df):
    conn = mysql.connector.connect(
        host=config["host"],
        user=config["user"],
        password=config["password"],
        database="weather_db"
    )
    cursor = conn.cursor()

    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO weather_data (city, country, temperature_c, humidity, wind_speed, description, timestamp)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            row["city"],
            row["country"],
            row["temperature_c"],
            row["humidity"],
            row["wind_speed"],
            row["description"],
            row["timestamp"]
        ))

    conn.commit()
    cursor.close()
    conn.close()
    print("✅ Data loaded into MySQL")

# ---------------------------
# Main Script
# ---------------------------
if __name__ == "__main__":
    raw_data_list = extract(CITIES)
    df = transform(raw_data_list)
    print(df)  # preview in Jupyter
    df.to_csv("sample_output.csv", index=False)  # Save to CSV
    load(df)
