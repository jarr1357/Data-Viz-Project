from datetime import datetime, timedelta
from PiConnection import *

dayspast = 1 #used for averaging

#condition Yellow if sensor is reporting data, but inconsistent over time
def YellowCon(sensor):

  value = CurrentValue(sensor)

  try:  #try to get average over dayspast
    error = (GetAvg(sensor,dayspast)/value)*100
    if (error == 100) and (value != 0.0 and value != 1.0): #if 100% error rate and not boolean
        condition = 1
        
    elif GetPG(sensor,dayspast) < 99: #check PI percent good (expected sensor response over time as a percent with 100 being perfect)
        condition = 2
  
    else: condition = False

  except:
      condition = False

  return(condition)

#condition Red if no expected data available
def RedCon(sensor):
  
  str_value = str(CurrentValue(sensor))

  if str_value == "Calc Failed":
    condition = True
  elif str_value == 'I/O Timeout':
    condition = True
  else: condition = False

  return(condition)

def Conditions(sensor):
    
  value = CurrentValue(sensor)

  if RedCon(sensor):
    condition = 'RED'
  elif YellowCon(sensor) == 1:
    condition = 'YELLOW - AVG at {0}'.format(str((GetAvg(sensor,dayspast)/value)*100))
  elif YellowCon(sensor) == 2:
    condition = 'YELLOW - PG at {0}'.format(str(GetPG(sensor,dayspast)))
  else:
    condition = 'GREEN' #if not Red or Yellow, set to Green

  return(condition)

#flag to help determine purpose of sensor (eg PI not conditioned)
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

