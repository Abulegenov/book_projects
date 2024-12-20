from pathlib import Path
import json
import plotly.express as px

# Read data as a string and convert it to a Python object
path = Path("geo_data/eq_data_1_day_m1.geojson")
contents = path.read_text()
all_eq_data = json.loads(contents)

# Create a more readable version of the data file
# path = Path('geo_data/readable_eq_data.json')
# readable_contents = json.dumps(all_eq_data,indent = 4)
# path.write_text(readable_contents)

features = all_eq_data["features"]

mags, lons, lats, eq_titles = [], [], [], []
for eq_dict in features:
    mags.append(eq_dict["properties"]["mag"])
    lons.append(eq_dict["geometry"]["coordinates"][0])
    lats.append(eq_dict["geometry"]["coordinates"][1])
    eq_titles.append(eq_dict["properties"]["title"])

print(mags[:10])
print(lons[:5])
print(lats[:5])

title = all_eq_data["metadata"]["title"]  # 'Global Earthquakes'
fig = px.scatter_geo(
    lat=lats,
    lon=lons,
    size=mags,
    title=title,
    color=mags,
    color_continuous_scale="Viridis",
    labels={"color": "Magnitude"},
    projection="natural earth",
    hover_name=eq_titles,
)

fig.write_html("earthquakes_vis.html")
# fig.show()
