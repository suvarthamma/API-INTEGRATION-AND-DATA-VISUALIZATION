import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Step 1: API Configuration
API_KEY = "1a010fb3cbcb3ed4ea0907d2cd063ef9" 
CITY = "Hyderabad"
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# Step 2: Fetch Data
response = requests.get(URL)
data = response.json()

if response.status_code != 200:
    print("Error fetching data:", data)
    exit()

# Step 3: Parse Data into DataFrame
forecast_list = data['list']
weather_data = {
    "datetime": [item["dt_txt"] for item in forecast_list],
    "temperature": [item["main"]["temp"] for item in forecast_list],
    "humidity": [item["main"]["humidity"] for item in forecast_list],
    "weather": [item["weather"][0]["description"] for item in forecast_list]
}

df = pd.DataFrame(weather_data)
df["datetime"] = pd.to_datetime(df["datetime"])
print(df.head(10))

# Step 4: Visualization
plt.figure(figsize=(10, 6))

# Temperature trend
plt.subplot(2, 1, 1)
plt.plot(df["datetime"], df["temperature"], marker='o', color='orange',ls='--',mec='yellow',ms=8)
plt.title(f"Temperature Trend in {CITY}",color='purple')
plt.xlabel("Date & Time")
plt.ylabel("Temperature (°C)")
plt.grid(True)

# Humidity trend
plt.subplot(2, 1, 2)
plt.plot(df["datetime"], df["humidity"], marker='p', color='tab:blue',mec='cyan',ms=8)
plt.title(f"Humidity Trend in {CITY}",color='purple')
plt.xlabel("Date & Time")
plt.ylabel("Humidity (%)")
plt.grid(True)

plt.tight_layout()
plt.show()
