import sys  
import clr
import pandas as pd

#Connecting to ProcessBook using .NET

sys.path.append(r'C:\Program Files (x86)\PIPC\AF\PublicAssemblies\4.0')    
clr.AddReference('OSIsoft.AFSDK')  
  
from OSIsoft.AF import *  
from OSIsoft.AF.PI import *  
from OSIsoft.AF.Asset import *  
from OSIsoft.AF.Data import *  
from OSIsoft.AF.Time import *  
from OSIsoft.AF.UnitsOfMeasure import *

#Connecting to PiServer

piServers = PIServers()    
piServer = piServers.DefaultPIServer;

#Loading the Sensor List excel sheet

df = pd.read_excel (r'sensor_list.xlsx')
sensorlist = pd.DataFrame(df, columns= ['Name'])

scount = 3 #sensor count starts at row 3
slen = len(sensorlist.index)-1

while scount <= slen:
  sensor = sensorlist.at[scount, 'Name']
  scount = scount + 1
  
  pt = PIPoint.FindPIPoint(piServer, sensor)  
  name = pt.Name.lower()
  current_value = pt.CurrentValue()
  str_value = str(current_value.Value)

  print ('\n Current value of {0}: {1}'.format(sensor, str_value))

  if str_value == "Calc Failed":
    print('RED')
  if str_value == '0.0':
    print('RED')
  if str_value == 'I/O Timeout':
    print('RED')
