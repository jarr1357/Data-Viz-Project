from PiConnection import *
from DatabaseConnection import *
from Conditions import *
from Logging import *

while True:
  try:
    nameList = ReadNames()
    logger('Database found')
    CompareSensors()
    logger('CompareSensors complete - Any new sensors added')
    break
  except:
    logger('Database not found - constructing new')
    FirstRun()
  
logger('Writing to database')
for sensor in nameList:

  str_sensor = ''.join(sensor)
  print(str_sensor)

  str_value = CurrentValue(str_sensor) #requests current values of sensors as a string
  print(str_value)

  WriteValue(str_sensor, str_value, Conditions(str_value))

CommitClose()


