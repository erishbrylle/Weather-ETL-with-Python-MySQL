# 🌦 Weather ETL with Python + MySQL

A simple **ETL (Extract, Transform, Load)** pipeline in Python that fetches live weather data from the [OpenWeatherMap API](https://openweathermap.org/), transforms it into a structured format, saves results as CSV, and loads the data into a MySQL database for storage and analysis.

## 📌 Features
- Fetches weather data for **multiple cities** at once
- Converts temperature from Kelvin → Celsius
- Saves transformed data into a CSV file
- Loads data into a MySQL database table (`weather_data`)
- Designed to be run in **Jupyter Notebook** or as a Python script

## 🛠 Tech Stack
- **Python** (requests, pandas, mysql-connector, json, datetime)
- **MySQL** (for structured storage)
- **OpenWeatherMap API**

## 📂 Project Structure
```bash
weather-etl/
│── weather_etl.ipynb # Main Jupyter Notebook
│── weather_etl.py # Script version
│── db_config.json # MySQL connection settings
│── config.json # API key (not committed to GitHub)
│── sample_output.csv # Example output file
│── README.md # Documentation
```

## ⚙️ Setup Instructions

### 1. Clone Repository
```bash
git clone https://github.com/erishbrylle/Weather-ETL-with-Python-MySQL
cd weather-etl
```

2. Install Dependencies
```bash
pip install requests pandas mysql-connector-python
```

3. Configure MySQL
Create a database and table:
```bash
CREATE DATABASE weather_db;
USE weather_db;

CREATE TABLE weather_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    city VARCHAR(100),
    country VARCHAR(10),
    temperature_c FLOAT,
    humidity INT,
    wind_speed FLOAT,
    description VARCHAR(100),
    timestamp DATETIME
);
```
4. Add Config Files
db_config.json
```bash
{
  "host": "localhost",
  "user": "root",
  "password": "yourpassword"
}
```
config.json
```bash
{
  "api_key": "your_openweathermap_api_key"
}
```
5. Run the Script
```bash
python weather_etl.py
```

## 📊 Example Output
CSV file (sample_output.csv)
```bash
city,country,temperature_c,humidity,wind_speed,description,timestamp
Manila,PH,31.25,74,3.6,"broken clouds",2025-09-10 14:35:21
Tokyo,JP,28.67,65,5.1,"clear sky",2025-09-10 14:35:22
```
MySQL Table (weather_data)
+----+--------+---------+---------------+----------+------------+----------------+---------------------+
| id | city   | country | temperature_c | humidity | wind_speed | description    | timestamp           |
+----+--------+---------+---------------+----------+------------+----------------+---------------------+
|  1 | Manila | PH      |         31.25 |       74 |        3.6 | broken clouds  | 2025-09-10 14:35:21 |
|  2 | Tokyo  | JP      |         28.67 |       65 |        5.1 | clear sky      | 2025-09-10 14:35:22 |
+----+--------+---------+---------------+----------+------------+----------------+---------------------+
