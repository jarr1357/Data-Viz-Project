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
logger("piServer is {0}".format(piServer))

#Used to test if a sensor is on the server
def sensorTest(sensor):
    pt = PIPoint.FindPIPoint(piServer, sensor)
    
#Connecting to PiServer and checking network stability
def Connection(sensor):
    timer = 1
    while True:
        try:
            pt = PIPoint.FindPIPoint(piServer, sensor)
            break
        except: #Network unstable, start testing connection
            logger("PiServer could not be found. Retrying in {0} seconds.".format(timer))
            time.sleep(timer)
            if timer < 60:
                timer = timer * 2
            if timer > 60:
                timer = 60
    return(pt)
        
#finds all tag names in system
def ReadAllTags():
    id_num = 0
    failure = 0
    namelist = []
    while failure < 100: #number of non-existant ids accepted before ending the search
        try:
            ppt = Connection(id_num) #pulls tag based off numeric id
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
    pt = Connection(sensor)  
    current_value = pt.CurrentValue()
    try:
        ret_value = float(current_value.Value)
    except:
        ret_value = current_value.Value
    return (ret_value)

#pulls a range of values from the requested sensor
def RecordedValues(sensor, startTime, endTime):
    pt = Connection(sensor)  
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

#pulls typical value from PI system
def GetTypicalValue(sensor):
    pt = Connection(sensor)
    attr = PICommonPointAttributes.TypicalValue

    attr_list = list()
    attr_list.append(attr)
    pt.LoadAttributes(attr_list)
    return(pt.GetAttribute(attr))

#pulls engineering units from PI system
def GetEU(sensor):
    pt = Connection(sensor)
    attr = PICommonPointAttributes.EngineeringUnits

    attr_list = list()
    attr_list.append(attr)
    pt.LoadAttributes(attr_list)
    return(pt.GetAttribute(attr))

#pulls descriptor from PI system
def GetDescriptor(sensor):
    pt = Connection(sensor)
    attr = PICommonPointAttributes.Descriptor

    attr_list = list()
    attr_list.append(attr)
    pt.LoadAttributes(attr_list)
    return(pt.GetAttribute(attr))

#pulls max value from PI system over a span of time divided into ranges where it is averaged
def GetMax(sensor, time):
    
    span = AFTimeSpan.Parse("{0}d".format(time))
    timerange = AFTimeRange("*-{}d".format(time), "*") 
    
    pt = Connection(sensor)
    summaries = pt.Summaries(timerange, span, AFSummaryTypes.Maximum, AFCalculationBasis.TimeWeighted, AFTimestampCalculation.Auto)
    
    for summary in summaries:  
        for event in summary.Value:  
            value = float(event.Value)
    
    return(value)

#pulls min value from PI system over a span of time divided into ranges where it is averaged
def GetMin(sensor, time):
    
    span = AFTimeSpan.Parse("{0}d".format(time))
    timerange = AFTimeRange("*-{}d".format(time), "*") 
    
    pt = Connection(sensor)
    summaries = pt.Summaries(timerange, span, AFSummaryTypes.Minimum, AFCalculationBasis.TimeWeighted, AFTimestampCalculation.Auto)
    
    for summary in summaries:  
        for event in summary.Value:  
            value = float(event.Value)
    
    return(value)

#pulls average value from PI system over a span of time divided into ranges where it is averaged
def GetAvg(sensor, time):
    
    span = AFTimeSpan.Parse("{0}d".format(time))
    timerange = AFTimeRange("*-{}d".format(time), "*") 
    
    pt = Connection(sensor)
    summaries = pt.Summaries(timerange, span, AFSummaryTypes.Average, AFCalculationBasis.TimeWeighted, AFTimestampCalculation.Auto)
    
    for summary in summaries:  
        for event in summary.Value:  
            value = float(event.Value)
    
    return(value)

#pulls percent good (percentage of expected sensor reading over time) from PI system
def GetPG(sensor, time):
    
    span = AFTimeSpan.Parse("{0}d".format(time))
    timerange = AFTimeRange("*-{}d".format(time), "*") 
    
    pt = Connection(sensor)
    summaries = pt.Summaries(timerange, span, AFSummaryTypes.PercentGood, AFCalculationBasis.TimeWeighted, AFTimestampCalculation.Auto)
    
    for summary in summaries:  
        for event in summary.Value:  
            value = float(event.Value)
    
    return(value)

#pulls standard deviation from PI system
def GetSD(sensor, time):
    
    span = AFTimeSpan.Parse("{0}d".format(time))
    timerange = AFTimeRange("*-{}d".format(time), "*") 
    
    pt = Connection(sensor)
    summaries = pt.Summaries(timerange, span, AFSummaryTypes.StdDev, AFCalculationBasis.TimeWeighted, AFTimestampCalculation.Auto)
    
    for summary in summaries:  
        for event in summary.Value:  
            value = float(event.Value)
    
    return(value)
