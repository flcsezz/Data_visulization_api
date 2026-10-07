from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path()

lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

highs = []
dates = []
lows = []

for row in reader:
    date = datetime.strptime(row[2], "%Y-%m-%d")
    try:
        high = int(row[4])
        low = int(row[5])
    except ValueError:
        print(f"Missing data for {date}")
    else:
        highs.append(high)
        lows.append(low)
        dates.append(date)






plt.style.use('dark_background')
fig, ax = plt.subplots()

ax.plot(dates,highs,  color= "red", alpha = 0.5)
ax.plot(dates,lows, color = "blue", alpha = 0.5)
ax.fill_between(dates, highs, lows,facecolor = 'blue', alpha = 0.1)

ax.set_title("random shi" , fontsize=24)
ax.set_xlabel("date", fontsize = 14)
ax.set_ylabel("Red=Highs, Blue=Lows", fontsize=14)

ax.tick_params(labelsize=10)
plt.show()