from datetime import datetime
import csv
from pathlib import Path
import matplotlib.pyplot as plt


path = Path("weather_data/sitka_weather_2021_full.csv")
path2 = Path('pcc_3e-main/chapter_16/the_csv_file_format/weather_data/death_valley_2021_full.csv')
lines = path.read_text().splitlines()
linesd = path2.read_text().splitlines()
reader2 = csv.reader(linesd)
headers2= next(reader2)
reader = csv.reader(lines)
headers = next(reader)

precep_sitka = []
precep_deathvally= []
dates = []

for row in reader:
    try:
        precep = float(row[5])
    except ValueError:
        print(f"invalid value in row {row}  of sitka data")
        continue
    else:
        precep_sitka.append(precep)

for row in reader2:
    try:
        precep2= float(row[5])
    except ValueError:
        print(f"invalid data in row {row} of death valley data")
        continue
    else:
        precep_deathvally.append(precep2)

plt.style.use('dark_background')

fig, ax = plt.subplots()

ax.plot(precep_sitka, color = "blue", alpha = 0.4)
ax.plot(precep_deathvally, color = "red", alpha = 0.4)

ax.set_title("precepitation in Sitla(Blue) And Death valley(red)", fontsize = 18)
ax.set_xlabel("", fontsize= 10)
ax.set_ylabel("Precipitaion", fontsize = 14)

ax.tick_params(labelsize = 10)
plt.show()
