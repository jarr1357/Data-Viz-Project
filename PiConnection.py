import sys  
import clr

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

#finds all tag names in system
def ReadAllTags():
    id_num = 0
    failure = 0
    namelist = []
    while failure < 100: #number of non-existant ids accepted before ending the search
        try:
            ppt = PIPoint.FindPIPoint(piServer, id_num) #pulls tag based off numeric id
            name = ppt.ToString() #gets the name
            namelist.append(name) # adds to list
            id_num = id_num + 1 #increased id being requested
            failure = 0 #resets failure counter
        except:
            failure = failure + 1 #increases number of failures to find end of list
            id_num = id_num + 1 #increases id requested
    return(namelist)
    

#pulls the current value of the requested sensor
def CurrentValue(sensor): 
    pt = PIPoint.FindPIPoint(piServer, sensor)  
   # name = pt.Name.lower()
    current_value = pt.CurrentValue()
    str_value = str(current_value.Value)
    return (str_value)

#pulls a range of values from the requested sensor
def RecordedValues(sensor, startTime, endTime):
    pt = PIPoint.FindPIPoint(piServer, sensor)  
  #  name = pt.Name.lower()
    timerange = AFTimeRange(startTime, endTime)  #time in format yy/mm/dd 11:56 PM start,end str
    recorded = pt.RecordedValues(timerange, AFBoundaryType.Inside, "", False)    
    return (recorded) #recorded is a list of 'event' enteries

