# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 13:33:28 2020

@author: Mike
"""

import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio

pio.renderers.default = "browser"

Line = 178         #Refers to the line in the .csv (while open in excel)
Hour = (Line - 2) #This will be used to reference a row in the .csv. Hours are all sequential so hours can be used to 



#These variables put the requested values into a pandas dataframe for each building.
SensorData = pd.read_csv('ACData_Jan2020.csv') #This loads the .csv for Jan 2020 into a pandas dataframe


#This list is referenced later to set the colours used in the chart. uses CSS colours
colors = []

#Set up the first figure
fig = go.Figure(data=[go.Pie(labels=["Building A (%.2fKW)" %float(SensorData.iloc[Hour,2]), 
                                     "Building A Fitness Zone (%.2fKW)" %float(SensorData.iloc[Hour,11]), "Building B (%.2fKW)" %float(SensorData.iloc[Hour,16]), 
                                     "Building C (%.2fKW)" %float(SensorData.iloc[Hour,98]), "Building D (%.2fKW)" %float(SensorData.iloc[Hour,20]),
                                     "Building E (%.2fKW)" %float(SensorData.iloc[Hour,25]), "Building G (%.2fKW)" %float(SensorData.iloc[Hour,28]), 
                                     "Building H (%.2fKW)" %float(SensorData.iloc[Hour,32]), "Building J (%.2fKW)" %float(SensorData.iloc[Hour,37]), 
                                     "Building K (%.2fKW)" %float(SensorData.iloc[Hour,42]), "Building M (%.2fKW)" %float(SensorData.iloc[Hour,47]), 
                                     "Building N (%.2fKW)" %float(SensorData.iloc[Hour,52]), "Building P (%.2fKW)" %float(SensorData.iloc[Hour,57]),
                                     "Building S (%.2fKW)" %float(SensorData.iloc[Hour,72]), "Building T (%.2fKW)" %float(SensorData.iloc[Hour,77]), 
                                     "Building V (%.2fKW)" %float(SensorData.iloc[Hour,82]), "Building Z (%.2fKW)" %float(SensorData.iloc[Hour,87]), 
                                     "Residence 1&2 (%.2fKW)" %float(SensorData.iloc[Hour,62]), "Residence 3 (%.2fKW)" %float(SensorData.iloc[Hour,67]), 
                                     "Plant Chillers (%.2fKW)" %float(SensorData.iloc[Hour,6])],
                                                                      
                             values=[SensorData.iloc[Hour,2], SensorData.iloc[Hour,11], SensorData.iloc[Hour,16], SensorData.iloc[Hour,98], 
                                     SensorData.iloc[Hour,20], SensorData.iloc[Hour,25], SensorData.iloc[Hour,28], SensorData.iloc[Hour,32], 
                                     SensorData.iloc[Hour,37], SensorData.iloc[Hour,42], SensorData.iloc[Hour,47], SensorData.iloc[Hour,52], 
                                     SensorData.iloc[Hour,57], SensorData.iloc[Hour,72], SensorData.iloc[Hour,77], SensorData.iloc[Hour,82], 
                                     SensorData.iloc[Hour,87], SensorData.iloc[Hour,62], SensorData.iloc[Hour,67], SensorData.iloc[Hour,6]])])

#Format traces on chart
fig.update_traces(hoverinfo='label+percent', textinfo='label', textfont_size=8,
                  marker=dict(colors=colors, line=dict(color='#000000', width=0)))

#title_text allows a title to be set for the chart.
#The (title_x = 0.5) argument allows for orientation of the title. This can be any number from 0-1.
fig.update_layout(title_text= ("Algonquin College Power Usage at {0}:00 Jan, {1} 2020 (In KW)" 
    .format(str(SensorData.iloc[Hour,1]).split(":")[0], str(SensorData.iloc[Hour,0]).split("-")[1])),
    font_size=12,
    title_x = 0.5,
    showlegend=False)

#display the chart
#Outputs the chart to the image files.
FileName = ("PieFig%d.svg" %1)
fig.write_image(FileName)
