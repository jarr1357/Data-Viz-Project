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
      condition = True
    else: condition = False

  except:
    condition = False
    
  return(condition)

def RedCon(sensor):
  
  str_value = CurrentValue(sensor)
  if str_value == "Calc Failed":
    condition = True
  elif str_value == 0.0:
    condition = True
  elif str_value == 'I/O Timeout':
    condition = True
  else: condition = False
  
  return(condition)

def Conditions(sensor):
  
  if RedCon(sensor):
    condition = 'RED'
  elif YellowCon(sensor):
    condition = 'YELLOW'
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
