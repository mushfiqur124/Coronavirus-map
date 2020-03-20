import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

table = pd.read_html("https://www.canada.ca/en/public-health/services/diseases/2019-novel-coronavirus-infection.html", header=0)[0]
table.set_index('Province, territory or other')
rona_data = table.to_dict()
# print(rona_data)

zipfile = r"zip://./gpr_000b11a_e.zip!gpr_000b11a_e.shp"
canada = gpd.read_file(zipfile).to_crs(epsg=3035)

canada.plot(facecolor='none',edgecolor='black',linewidth=.2)
plt.show()