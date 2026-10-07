import csv
import plotly.express as px
from pathlib import Path

path = Path("pcc_3e-main/chapter_16/mapping_global_datasets/eq_data/world_fires_7_day.csv")
lines = path.read_text().splitlines()
reader = csv.reader(lines)
Header = next(reader)

lats, lons, mags = [], [], []

for row in reader:
    lats.append(float(row[0]))
    lons.append(float(row[1]))
    mags.append(float(row[2]))

title = "World Fire in 30 Days"

fig = px.scatter_geo(lat=lats, lon=lons, size= mags, title=title,
                     color = mags,
                     color_continuous_scale= "icefire",
                     labels= {"color": "Fire Magnitude"},
                     projection= "orthographic",
                     )

fig.show()