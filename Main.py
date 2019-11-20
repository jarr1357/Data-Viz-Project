from PiConnection import *
from DatabaseConnection import *
from Flagging import *

nameList = ReadNames()

print ('Writing to database')
for sensor in nameList:

  str_sensor = ''.join(sensor)
  print(str_sensor)

  str_value = CurrentValue(str_sensor) #requests current values of sensors as a string
  print(str_value)

  WriteValue(str_sensor, str_value, Conditions(str_value))

print(CommitClose())


