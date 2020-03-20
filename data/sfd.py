import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
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

ax = for_plotting.plot(column='Number of confirmed cases', cmap = 'Reds', figsize=(20,9), linewidth=0.3, edgecolor='black', k=4, legend = True, legend_kwds={'label': "Confirmed Cases of COVID-19 by Province",'orientation': "horizontal"});

ax.set_axis_off()                                                 
                                
##canada.plot();
plt.axis([-1.65e7,-0.5e7,0.5e7,1.2e7])
plt.show()

