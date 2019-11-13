from Ingestion import *
from DatabaseInteraction import *
import pandas as pd

#Loading the Sensor List excel sheet

df = pd.read_excel (r'sensor_list.xlsx')
sensorlist = pd.DataFrame(df, columns= ['Name'])

scount = 3 #sensor count starts at row 3
slen = len(sensorlist.index)-1 #-1 for zero offset

def Conditions(str_value):
  if str_value == "Calc Failed":
    flag ='RED'
  elif str_value == '0.0':
    flag = 'RED'
  elif str_value == 'I/O Timeout':
    flag = 'RED'
  else:
    flag = 'GREEN'
  return(flag)

while scount <= slen: #goes through every sensor
  sensor = sensorlist.at[scount, 'Name']
  scount = scount + 1

  str_value = CurrentValue(sensor) #requests current values of sensors as a string

  print ('\n Current value of {0}: {1} {2}'.format(sensor, str_value, Conditions(str_value)))

  WriteValue(sensor, str_value, Conditions(str_value))


CommitClose()
