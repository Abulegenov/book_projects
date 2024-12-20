from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path("weather_data/sitka_weather_2021_simple.csv")
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)
rows = list(reader)

for index, column_header in enumerate(header_row):
    print(index, column_header)

# extract high and low temperatures, dates

highs = [int(row[4]) for row in rows if row[4] != ""]
lows = [int(row[5]) for row in rows if row[4] != ""]
dates = [datetime.strptime(row[2], "%Y-%m-%d") for row in rows if row[4] != ""]
# print(dates)
# print(highs)
# print(lows)
# plot the high temperatures.
plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.plot(dates, highs, color="red", alpha=0.5)
ax.plot(dates, lows, color="blue", alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)
# Format plot.
ax.set_title("Daily High Temperatures, 2021", fontsize=24)
ax.set_xlabel("", fontsize=16)
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)
fig.autofmt_xdate()
plt.show()
