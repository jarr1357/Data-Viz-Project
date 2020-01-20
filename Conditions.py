from datetime import datetime, timedelta
from PiConnection import *

def YellowCon(sensor):

  try:
    dayspast = 5
    
    date = datetime.datetime.now()
    today = date.strftime('%Y-%m-%d %I:%M %p')
    
    past = date - timedelta(days=dayspast)
    past = past.strftime('%Y-%m-%d %I:%M %p')
    
    df = RecordedValues(sensor, today, past)

    if float(df.mean()) == CurrentValue(sensor):
      condition = 1
    else: condition = 3

  except:
    condition = 2
    
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
  else:  
    yellowCase = YellowCon(sensor)
    if yellowCase == 2:
      condition = 'RED'
    elif yellowCase == 1:
      condition = 'YELLOW'

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

