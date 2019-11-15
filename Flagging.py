def Conditions(str_value):
  if str_value == "Calc Failed":
    flag ='RED'
  elif str_value == '0.0':
    flag = 'RED'
  elif str_value == 'I/O Timeout':
    flag = 'RED'
  return(flag)
