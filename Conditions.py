import datetime
from PiConnection import *

def ConstantValue(sensor):
  today = datetime.datetime.now()
  print(today)
  #df = RecordedValues(sensor, today, past)
  return('YELLOW')

def Conditions(sensor, str_value):
  if str_value == "Calc Failed":
    condition ='RED'
  elif str_value == '0.0':
    condition = 'RED'
  elif str_value == 'I/O Timeout':
    condition = 'RED'
  else:
    condition = 'GREEN'
  return(condition)

def Flagging(sensor_name):
  flags = []
  if sensor_name.find("PI-SERVER") != -1:
    flags.append('PI')
  if sensor_name.find("ACCE") != -1:
    flags.append('ACCE')
  if sensor_name.find("COGEN") != -1:
    flags.append('COGEN')
  sentflag = (str(flags))[1:-1]
  return(sentflag)

