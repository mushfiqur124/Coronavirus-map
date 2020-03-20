import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
from geopandas import GeoDataFrame
from shapely.geometry import Point
import adjustText as aT
import pathlib

tables = pd.read_html("https://www.canada.ca/en/public-health/services/diseases/2019-novel-coronavirus-infection.html", header=0) 

df = tables[0]  
dfedit = df.drop([13,14], axis=0)

#df = df.set_index('Province, territory or other')

#infodict = df.to_dict()

#confirmedCase = infodict["Number of confirmed cases"]
#probableCase = infodict["Number of probable cases"]

#zipfile = "zip:///Users/Mushfiqur/Documents/Github/coronavirus-map/data/gpr_000b11a_e.zip!gpr_000b11a_e.shp"       
zipfile = "zip://" + str(pathlib.Path(__file__).parent.absolute()) + "/gpr_000b11a_e.zip!gpr_000b11a_e.shp"       

canada = gpd.read_file(zipfile)   

# Let's make a copy of our data
orig = canada.copy()

# Reproject the data
canada = canada.to_crs(epsg=3395)

for_plotting = canada.merge(dfedit, left_on = 'PRENAME', right_on = 'Province, territory or other')

canada["center"] = canada["geometry"].centroid
canada_points = canada.copy()
canada_points.set_geometry("center", inplace = True)

ax = for_plotting.plot(column='Number of confirmed cases', cmap = 'Reds', figsize=(20,9), linewidth=0.3, edgecolor='black', k=4, legend = True, legend_kwds={'label': "Confirmed Cases of COVID-19 by Province",'orientation': "horizontal"});

ax.set_axis_off()                                                 

texts = []

for x, y, label in zip(canada_points.geometry.x, canada_points.geometry.y, for_plotting['Number of confirmed cases']):
    texts.append(plt.text(x, y, label, fontsize = 8))

aT.adjust_text(texts, force_points=0.3, force_text=0.8, expand_points=(1,1), expand_text=(1,1), 
               arrowprops=dict(arrowstyle="-", color='grey', lw=0.5))

##canada.plot();
plt.axis([-1.65e7,-0.5e7,0.5e7,1.2e7])

plt.show()

