import pandas as pd
from shapely.geometry import Point
import geopandas as gpd
from geopandas import GeoDataFrame
import matplotlib.pyplot as plt
import random

# United States
US_LAT_HIGH = 50.862137
US_LAT_LOW = 26.903456
US_LON_HIGH = -123.708449
US_LON_LOW = -59.548298

# Europe
EU_LAT_HIGH = 71.982614
EU_LAT_LOW = 34.931584
EU_LON_HIGH = -19.171315
EU_LON_LOW = 52.371647

# Asia
AS_LAT_HIGH = 50.324893
AS_LAT_LOW = 5.496438
AS_LON_HIGH = 95.789622
AS_LON_LOW = 148.348211

# Get api-key
api_file = open("api-key.txt", "r")
api_key = api_file.read()
api_file.close()

# Read data and connect with Google maps API to get latitude and longitude
df_plasmids = pd.read_excel(r'Perli_plasmids_Still_to_be_drawn.xlsx', header=None, names=['ID', 'Professor', 'Institute', 'Year'])
df_plasmids['Address'] = df_plasmids['Professor'] + ', ' + df_plasmids['Institute']

df = pd.read_csv('New_Long_Lats.csv')

for i in range(len(df)):
    df['Latitude'][i] = (df['Latitude'][i] + random.uniform(0.1, 1)).copy()
    df['Longitude'][i] = (df['Longitude'][i] + random.uniform(0.1, 1)).copy()

# Reading coordinates for Asia
df = df[(df['Latitude'] < AS_LAT_HIGH) & (df['Latitude'] > AS_LAT_LOW)]
df = df[(df['Longitude'] < AS_LON_LOW) & (df['Longitude'] > AS_LON_HIGH)]
AS = df.ID.count()

geometry = [Point(xy) for xy in zip(df['Longitude'], df['Latitude'])]
gdf = GeoDataFrame(df, geometry=geometry)

# This is a simple world map that goes with geopandas
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Plot only USA
# USA = world.cx[US_LAT_LOW:US_LAT_HIGH, US_LON_LOW:US_LON_HIGH]

# We remove Antarctica.
ax = world[world.name != 'Antarctica'].plot(figsize=(30, 10), color='#F9E076')
ax.axis('off')

# We can now plot our ``GeoDataFrame``.
gdf.plot(ax=ax, marker='o', color='red', markersize=25)

plt.show()

