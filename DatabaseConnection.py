import sqlite3
from flask import g
from PiConnection import *
from Conditions import *
from Logging import *

conn = sqlite3.connect('SensorFlags.db')
cursor = conn.cursor()
logger("Connected to database")

def WriteInitial(name, descriptor, flag, uom, typical):
    try:
        commandstring = '''UPDATE Sensors SET Descriptor = ?,Flag = ?,UOM = ?,Typical = ? WHERE Tag_Name = ?'''
        values = (descriptor, flag, uom, typical, name)
        cursor.execute(commandstring, values)
    except:
        logger("No table! This should never happen.")

def WriteCondition(name, condition):
    try:
        commandstring = '''UPDATE Sensors SET Condition = ? WHERE Tag_Name = ?'''
        values = (condition, name)
        cursor.execute(commandstring, values)
    except:
        logger("Error adding condition to table.")

def ReadNames():
    cursor.execute('''SELECT Tag_Name FROM Sensors WHERE Flag != "PI"''')
    nameList = cursor.fetchall()
    return(nameList)

def ReadRecord(sensor):
    cursor.execute('SELECT * FROM Sensors WHERE Tag_Name = ?', (sensor,))
    recordList = cursor.fetchall()
    return(recordList)
    

def PassCommand(commandstring, values):
    cursor.execute(commandtring, values)
    return('Complete')

def MakeTable():
    try:
        cursor.execute('''CREATE TABLE Sensors(Tag_Name, Descriptor, Flag, UOM, Typical, Condition)''')
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
        except:
            cursor.execute('INSERT INTO Sensors(Tag_Name) VALUES(?)', (str_sensor,))
            WriteInitial(str_sensor, GetDescriptor(str_sensor), Flagging(str_sensor),
                         GetEU(str_sensor), GetTypicalValue(str_sensor))
            logger("Inserting new tag into database - {0}".format(str_sensor))
    
    tablelist = ReadNames()
    for name in tablelist:
        name = ''.join(name)
        try:
            sensorTest(name)
        except:
            cursor.execute("DELETE FROM Sensors WHERE Tag_Name = (?)", (name,))
            logger("Deleting old tag from database - {0}".format(name))
    
    logger('CompareSensors complete!')

def CommitClose():
    conn.commit()
    conn.close()
    logger('Closed SQL connection!')
    return()

def FirstRun(): 
    MakeTable()
    CompareSensors()
