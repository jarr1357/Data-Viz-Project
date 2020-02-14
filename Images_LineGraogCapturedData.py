# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 13:33:28 2020

@author: Mike
"""

import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio

pio.renderers.default = "browser"

Line = 170         #Refers to the line in the .csv (while open in excel)
StartHour = (Line - 2) #This will be used to reference a row in the .csv. Hours are all sequential so hours can be used to 
EndHour = StartHour + 24



#These variables put the requested values into a pandas dataframe for each building.
SensorData = pd.read_csv('ACData_Jan2020.csv') #This loads the .csv for Jan 2020 into a pandas dataframe


#This list is referenced later to set the colours used in the chart. uses CSS colours
colors = []

#Set up the first figure

fig = go.Figure()
fig.add_trace(go.Scatter(x=SensorData.iloc[StartHour:EndHour,1], 
                         y=SensorData.iloc[StartHour:EndHour,103],
                         name='Hydro Power'))

fig.add_trace(go.Scatter(x=SensorData.iloc[StartHour:EndHour,1], 
                         y=SensorData.iloc[StartHour:EndHour,92],
                         name='CoGen 1'))

fig.add_trace(go.Scatter(x=SensorData.iloc[StartHour:EndHour,1], 
                         y=SensorData.iloc[StartHour:EndHour,95],
                         name='CoGen 2'))

#title_text allows a title to be set for the chart.
#The (title_x = 0.5) argument allows for orientation of the title. This can be any number from 0-1.
fig.update_layout(title_text= ("Power Generation From {0}:00 Jan, {1} 2020 to {2}:00 Jan, {3} 2020 (In KW)" 
    .format(str(SensorData.iloc[StartHour,1]).split(":")[0],
            str(SensorData.iloc[StartHour,0]).split("-")[1],
            str(SensorData.iloc[EndHour,1]).split(":")[0],
            str(SensorData.iloc[EndHour,0]).split("-")[1])),
    font_size=12,
    title_x = 0.5,
    showlegend=True)

#display the chart
#Outputs the chart to the image files.
FileName = ("StackedLineFig%d.svg" %1)
fig.write_image(FileName)
