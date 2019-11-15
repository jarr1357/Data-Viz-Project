from PiConnection import *
from DatabaseInteraction import *
from Flagging import *
import pandas as pd

#Loading the Sensor List excel sheet

df = pd.read_excel (r'sensor_list.xlsx')
sensorlist = pd.DataFrame(df, columns= ['Name'])

scount = 0 #sensor count starts at row 3
slen = len(sensorlist.index)-1 #-1 for zero offset

print ('Writing to database')
while scount <= slen: #goes through every sensor
  sensor = sensorlist.at[scount, 'Name']
  scount = scount + 1

  str_value = CurrentValue(sensor) #requests current values of sensors as a string

  WriteValue(sensor, str_value, Conditions(str_value))

print(CommitClose())


