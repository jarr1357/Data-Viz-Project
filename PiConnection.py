import sys  
import clr
import time

import pandas as pd
import numpy as np

from Logging import *

#Connecting to ProcessBook using .NET
sys.path.append(r'C:\Program Files (x86)\PIPC\AF\PublicAssemblies\4.0')    
clr.AddReference('OSIsoft.AFSDK')  
  
from OSIsoft.AF import *  
from OSIsoft.AF.PI import *  
from OSIsoft.AF.Asset import *  
from OSIsoft.AF.Data import *  
from OSIsoft.AF.Time import *  
from OSIsoft.AF.UnitsOfMeasure import *

#Setting up PiServer connection
piServers = PIServers()    
piServer = piServers.DefaultPIServer;

#Connecting to PiServer
timer = 1
while True:
    try:
        pt = PIPoint.FindPIPoint(piServer, 'SINUSOID') #testing integrated PiServer sensor
        logger("Connected to PiServer")
        break
    except:
        logger("PiServer could not be found. Retrying in {0} seconds.".format(timer))
        time.sleep(timer)
        if timer < 60:
            timer = timer * 2
        if timer > 60:
            timer = 60
        
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
    current_value = pt.CurrentValue()
    #test = pt.GetAttribute(UOM)
    #print(test)
##    uom = pt.UOM()
##    print(uom)
    try:
        ret_value = float(current_value.Value)
    except:
        ret_value = str(current_value.Value)
    return (ret_value)

#pulls a range of values from the requested sensor
def RecordedValues(sensor, startTime, endTime):
    pt = PIPoint.FindPIPoint(piServer, sensor)  
    timerange = AFTimeRange(startTime, endTime)  #time in format "yyyy/mm/dd hh:mm AM/PM"
    recorded = pt.RecordedValues(timerange, AFBoundaryType.Inside, "", False)
    timelist = []
    valuelist = []
    for event in recorded: #converting AFValues object into panda dataframe
        timelist.append(str(event.Timestamp.LocalTime))
        try:
            valuelist.append(float(event.Value))
        except:
            valuelist.append(event.Value)
    data = {'Time':timelist,
            'Value':valuelist}
    df = pd.DataFrame(data)
    return (df) #returns dataframe of times and values

#print(RecordedValues('WCHPCOGEN_WEPV1.STTP.PRESENT_VALUE','2019/08/24 11:00 PM','2019/08/24 11:30 PM'))
print(CurrentValue('WCHPCOGEN_WEPV1.STTP.PRESENT_VALUE'))
