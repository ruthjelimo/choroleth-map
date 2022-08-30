
import plotly.express as px
import json,os
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd

#https://towardsdatascience.com/plot-choropleth-maps-with-shapefiles-using-geopandas-a6bf6ade0a49

election_results = pd.read_csv('data/kenyans.csv',encoding='utf-8')
election_results.head()
print(election_results)


# set the filepath and load in a shapefile
fp = "data/kenyan-counties/County.shp"
#reading the file stored in variable fp
map_df = gpd.read_file(fp)

# check data type so we can see that this is not a normal dataframe, but a GEOdataframe
map_df.head()

print(map_df)

# join the geodataframe with the cleaned up csv dataframe
merged = map_df.set_index("COUNTY").join(election_results.set_index("county"))
merged.head()

print(merged.head())
print(merged)



fig = px.choropleth(merged, geojson=merged.geometry,
                    locations=merged.index, color="winner",
                    height=500,color_discrete_sequence=['blue','yellow'],
                   color_continuous_scale="Viridis")

fig.update_geos(fitbounds="locations", visible=True)

fig.update_layout(
    title_text='Election Results 2022'
)

fig.update(layout = dict(title=dict(x=0.5)))

fig.update_layout(
    margin={"r":0,"t":30,"l":10,"b":10},
    coloraxis_colorbar={
        'title':'winner'},clickmode='event+select')



fig.show()

