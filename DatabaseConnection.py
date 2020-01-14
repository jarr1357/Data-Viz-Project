import sqlite3
from PiConnection import ReadAllTags
from Conditions import Flagging
from Logging import *

conn = sqlite3.connect('SensorFlags.db')
cursor = conn.cursor()

def WriteCondition(name, current_value, condition):
    try:
        commandstring = '''UPDATE Sensors SET Current_Value = ? ,Condition = ? WHERE Tag_Name = ?'''
        values = (current_value, condition, name)
        cursor.execute(commandstring, values)
    except:
        print("No table!")

def WriteFlag(name, flag):
    try:
        commandstring = '''UPDATE Sensors SET Flag = ? WHERE Tag_Name = ?'''
        values = (flag, name)
        cursor.execute(commandstring, values)
    except:
        print("No table!")

def ReadNames():
    cursor.execute('''SELECT Tag_Name FROM Sensors''')
    nameList = cursor.fetchall()
    return(nameList)

def PassCommand(commandstring, values):
    cursor.execute(commandtring, values)
    return('Complete')

def MakeTable():
    try:
        cursor.execute('''CREATE TABLE Sensors(Tag_Name, Flag, Current_Value, Condition)''')
    except:
        logger('Already a "Sensors" table')

def CompareSensors():
    sensorlist = ReadAllTags()
    for sensor in sensorlist: #goes through every sensor
        str_sensor = ''.join(sensor)
        cursor.execute('SELECT Tag_Name FROM Sensors WHERE Tag_Name == (?)', (str_sensor,))
        tagexist = cursor.fetchall()
        try:
            tagexist = str(tagexist[0])
            print('Tag exists - {0}'.format(tagexist))
        except:
            cursor.execute('INSERT INTO Sensors(Tag_Name) VALUES(?)', (str_sensor,))
            print(str_sensor)
            WriteFlag(str_sensor, Flagging(str_sensor))
            logger("Inserting new tag into database - {0}".format(str_sensor))
    logger('CompareSensors complete - Any new sensors added')

def CommitClose():
    conn.commit()
    conn.close()
    logger('Closed SQL connection!')
    return()

def FirstRun(): 
    MakeTable()
    CompareSensors()
