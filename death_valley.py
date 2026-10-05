from datetime import datetime
import csv
import matplotlib.pyplot as plt
from pathlib import Path
path = Path('weather_data/death_valley_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

dates = []
highs = []
lows = []

for row in reader:
    date= datetime.strptime(row[2], '%Y-%m-%d') 
    try:
        high = int(row[3])
        low= int(row[4])
    except ValueError:
        print(f"missing Data for Date {date}")
    else:
        dates.append(date)
        highs.append(high)
        lows.append(low)

plt.style.use('dark_background')

fig, ax = plt.subplots()
ax.plot(dates, highs, color="red", alpha = 0.5)
ax.plot(dates, lows, color = "blue", alpha = 0.5)
ax.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.2)

ax.set_title('Death valley', fontsize = 25)
ax.set_xlabel('Dates', fontsize = 16)
ax.set_ylabel("temps", fontsize = 18)

ax.tick_params(labelsize = 10)
plt.show()