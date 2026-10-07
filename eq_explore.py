import json
from pathlib import Path
import plotly.express as px

path = Path("eq_data/eq_data_1_day_m1.geojson")
contents = path.read_text()
all_eq_data =json.loads(contents)

all_dict = all_eq_data['features']
mags, lons, lats, eq_titles= [], [], [], []

for dicta in all_dict:
    mags.append(dicta['properties']['mag'])
    lons.append(dicta['geometry']['coordinates'][0])
    lats.append(dicta['geometry']['coordinates'][1])
    eq_titles.append(dicta['properties']['title'])


title = all_eq_data["metadata"]['title']
fig = px.scatter_geo(lat= lats, lon = lons, size = mags, title=title,
                     color = mags,
                     color_continuous_scale="icefire",
                     labels= {"color":'Magnitude'},
                     projection= "orthographic",
                     hover_name= eq_titles,
                     )

fig.show()