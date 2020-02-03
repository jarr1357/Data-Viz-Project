from datetime import datetime, timedelta
from PiConnection import *

def YellowCon(sensor):

  dayspast = 10
  value = CurrentValue(sensor)

  try:
    error = (GetAvg(sensor,dayspast)/value)*100
    if (error == 100) and (value != 0.0 and value != 1.0):
        condition = 1
        
    elif GetPG(sensor,dayspast) < 99:
        condition = 2
  
    else: condition = False

  except:
      condition = False

  return(condition)

def RedCon(sensor):
  
  str_value = str(CurrentValue(sensor))

  if str_value == "Calc Failed":
    condition = True
  elif str_value == 'I/O Timeout':
    condition = True
  else: condition = False

  return(condition)

def Conditions(sensor):

  if RedCon(sensor):
    condition = 'RED'
  elif YellowCon(sensor) == 1:
    condition = 'YELLOW - AVG'
  elif YellowCon(sensor) == 2:
    condition = 'YELLOW - PG'
  else:
    condition = 'GREEN'

  return(condition)

def Flagging(sensor_name):
  
  flags = []
  if sensor_name.find("PI-SERVER") != -1:
    flags.append('PI')
  if sensor_name.find("PI-NODE") != -1:
    flags.append('PI')
  if sensor_name.find("PI-OMNODE") != -1:
    flags.append('PI')
  if sensor_name.find("PI-WEB") != -1:
    flags.append('PI')
  if sensor_name.find("PI-AFSERVER") != -1:
    flags.append('PI')
  if sensor_name.find("ACCE") != -1:
    flags.append('ACCE')
  if sensor_name.find("COGEN") != -1:
    flags.append('COGEN')
  sentflag = (str(flags))[2:-2]
  
  return(sentflag)

#Conditions('ACCE.PH.PXCM2_ACRS.WEATHERSTATION:SOLAR_RAD.PRESENT_VALUE')
