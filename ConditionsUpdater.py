from PiConnection import *
from DatabaseConnection import *
from Conditions import *
from Logging import *

try:
  CompareSensors() #Test to see if database exists
except:
  logger('Database not found - constructing new')
  FirstRun() #Builds new database if none found

nameList = ReadNames() #Pulls all tage from database
logger('Writing conditions to database')
for sensor in nameList: #Goes through each sensor

    str_sensor = ''.join(sensor) #Formatting
    condition = Conditions(str_sensor) #Finds condition of sensor
    
    WriteCondition(str_sensor, condition) #writes condition to database
    
CommitClose() #Closes database when finished.