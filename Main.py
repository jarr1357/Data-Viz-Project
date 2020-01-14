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
  print(str_sensor)

  str_value = CurrentValue(str_sensor) #requests current values of sensors as a string
  print(str_value)

  WriteCondition(str_sensor, str_value, Conditions(str_value))

CommitClose()


