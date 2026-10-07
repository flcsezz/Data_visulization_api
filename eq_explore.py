import json
from pathlib import Path
import plotly.express as px

path = Path("eq_data/eq_data_1_day_m1.geojson")
contents = path.read_text()
all_eq_data =json.loads(contents)

all_dict = all_eq_data['features']
mags, lons, lats, eq_titles= [], [], [], []

for dicta in all_dict:
    mag = dicta['properties']['mag']
    lon = dicta['geometry']['coordinates'][0]
    lat = dicta['geometry']['coordinates'][1]
    titles = dicta['properties']['title']

    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    eq_titles.append(titles)


title = "Global Earthquakes"
fig = px.scatter_geo(lat= lats, lon = lons, size = mags, title=title,
                     color = mags,
                     color_continuous_scale="icefire",
                     labels= {"color":'Magnitude'},
                     projection= "orthographic",
                     hover_name= eq_titles)

fig.show()