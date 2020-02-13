# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 20:05:54 2020

@author: Mike
"""

import time
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio

pio.renderers.default = "browser"

TotalHours = 6    #Used to determine how many charts will be created. 1 per hour
Line = 690         #Refers to the line in the .csv (while open in excel)
Hour = (Line - 2) #This will be used to reference a row in the .csv. Hours are all sequential so hours can be used to 
                  #reference the day as well. The Line in the .scv is offset by -2
SensorData = pd.read_csv('ACData_Jan2020.csv') #This loads the .csv for Jan 2020 into a pandas dataframe

#This for loop will generate a number of charts based on the given days
for i in range(TotalHours):    
  
  
  CurrentHour = SensorData.iloc[Hour,1]
  
  print(SensorData.iloc[Hour,103])
  
  TotalPowerInput = (float(SensorData.iloc[Hour,103]) + float(SensorData.iloc[Hour,92]) + float(SensorData.iloc[Hour,95]))
  TotalPowerOutput = (float(SensorData.iloc[Hour,11]) + float(SensorData.iloc[Hour,16]) + float(SensorData.iloc[Hour,98]) + 
                      float(SensorData.iloc[Hour,20]) + float(SensorData.iloc[Hour,24]) + float(SensorData.iloc[Hour,28]) + 
                      float(SensorData.iloc[Hour,32]) + float(SensorData.iloc[Hour,37]) + float(SensorData.iloc[Hour,42]) + 
                      float(SensorData.iloc[Hour,47]) + float(SensorData.iloc[Hour,52]) + float(SensorData.iloc[Hour,57]) +
                      float(SensorData.iloc[Hour,72]) + float(SensorData.iloc[Hour,77]) + float(SensorData.iloc[Hour,82]) + 
                      float(SensorData.iloc[Hour,87]) + float(SensorData.iloc[Hour,62]) + float(SensorData.iloc[Hour,67]) + 
                      float(SensorData.iloc[Hour,6]) )
  
  #This set of if statements accounts for the higher power usage of the two total power variables
  if TotalPowerOutput > TotalPowerInput:
    PowerDifference = TotalPowerOutput - TotalPowerInput
    TotalPower = TotalPowerOutput
    
  elif TotalPowerOutput < TotalPowerInput:
    PowerDifference = TotalPowerInput - TotalPowerOutput
    TotalPower = TotalPowerInput
    
  else:
    PowerDifference = TotalPowerInput - TotalPowerOutput
    TotalPower = TotalPowerInput

  #These can be removed without affecting the program. This just gives the user feedback for each chart to verify values
  print("Chart #%d:" %(i+1))
  print(CurrentHour)
  print(TotalPowerInput)  
  print(TotalPowerOutput)
  print(PowerDifference)
  print(str())

  fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      
      #label adds information to each node (data point) on the sankey diagram.
      label = ["Hydro Power (%.2fKW )" %SensorData.iloc[Hour,103], "COGEN 1 (%.2fKW)" %SensorData.iloc[Hour,92], 
               "COGEN 2 (%.2fKW)" %float(SensorData.iloc[Hour,95]), "Solar 1 (KW)", "Solar 2 (KW)", 
               "Total Power (%.2fKW)" %float(TotalPower), "Building A (%.2fKW)" %float(SensorData.iloc[Hour,2]), 
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
      
      #Used to select colours for the charts
      color = ["Green", "Green", "Green", "Green", "Green", "Yellow", "Red", "Red", "Red", "Red", "Red", "Red", "Red", 
               "Red", "Red", "Red", "Red", "Red", "Red", "Red", "Red", "Red", "Red", "Red", "Red", "Red"]
    ),
    #This dictionary is used to specify the constraints of the sankey diagram
    link = dict(
      #source is used specifiy where each trace begins. Starts at 0
      source = [0, 1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
      #each of the values in the target list pairs to the corrosponding value in the start list to create the trace
      target = [5, 5, 5, 5, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],
      #value assigns a number to each of the traces in the sankey diagram
      value = [SensorData.iloc[Hour,103], SensorData.iloc[Hour,92], SensorData.iloc[Hour,95], 0, 0, 
               SensorData.iloc[Hour,2], SensorData.iloc[Hour,11], SensorData.iloc[Hour,16], SensorData.iloc[Hour,98], 
               SensorData.iloc[Hour,20], SensorData.iloc[Hour,25], SensorData.iloc[Hour,28], SensorData.iloc[Hour,32], 
               SensorData.iloc[Hour,37], SensorData.iloc[Hour,42], SensorData.iloc[Hour,47], SensorData.iloc[Hour,52], 
               SensorData.iloc[Hour,57], SensorData.iloc[Hour,72], SensorData.iloc[Hour,77], SensorData.iloc[Hour,82], 
               SensorData.iloc[Hour,87], SensorData.iloc[Hour,62], SensorData.iloc[Hour,67], SensorData.iloc[Hour,6]]
  ))])

  #This block of code updates the title, font size and title offset of the chart.
  fig.update_layout(title_text= ("Algonquin College Power Usage at {0}:00h Jan, {1} 2020 (In KW)" 
                                 .format(str(SensorData.iloc[Hour,1]).split(":")[0],
                                 str(SensorData.iloc[Hour,0]).split("-")[1])),
                    font_size=10, 
                    title_x = 0.5) #title_x of 0.5 centers the title
  #Outputs the image to the renderer.
  fig.show()

  Hour += 1 #(Increments the hour)
  
  time.sleep(0.5) #Adds a 500 millisecond delay to the for loop