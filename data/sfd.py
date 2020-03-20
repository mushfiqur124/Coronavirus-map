import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
tables = pd.read_html("https://www.canada.ca/en/public-health/services/diseases/2019-novel-coronavirus-infection.html", header=0) 

df = tables[0]  

df = df.set_index('Province, territory or other')

infodict = df.to_dict()

confirmedCase = infodict["Number of confirmed cases"]
probableCase = infodict["Number of probable cases"]

zipfile = "zip:///Users/Mushfiqur/Desktop/data/gpr_000b11a_e.zip!gpr_000b11a_e.shp"       
canada = gpd.read_file(zipfile)   

# Let's make a copy of our data
orig = canada.copy()

# Reproject the data
canada = canada.to_crs(epsg=3395)

print(canada)

  
###
#canada.plot(); 
#plt.show()

