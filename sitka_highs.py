from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('weather_data/sitka_weather_07-2021_simple.csv')

lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

highs = []
dates = []
lows = []

for row in reader:
    high = int(row[4])
    highs.append(high)
    date = datetime.strptime(row[2], "%Y-%m-%d")
    dates.append(date)
    low = int(row[5])
    lows.append(low)






plt.style.use('dark_background')
fig, ax = plt.subplots()

ax.plot(dates,highs,  color= "red", alpha = 1)
ax.plot(dates,lows, color = "blue", alpha = 1)
ax.fill_between(dates, highs, lows,facecolor = 'blue', alpha = 0.2)

ax.set_title("random shi" , fontsize=24)
ax.set_xlabel("date", fontsize = 14)
ax.set_ylabel("Red=Highs, Blue=Lows", fontsize=14)

ax.tick_params(labelsize=10)
plt.show()