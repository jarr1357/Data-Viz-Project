from PiConnection import *
from DatabaseConnection import *
from Conditions import *
from Logging import *


try:
  CompareSensors()
except:
  logger('Database not found - constructing new')
  FirstRun()

nameList = ReadNames()
logger('Writing conditions to database')
for sensor in nameList:

    str_sensor = ''.join(sensor)
    WriteCondition(str_sensor, Conditions(str_sensor))

CommitClose()

