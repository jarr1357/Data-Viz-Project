import sqlite3
from flask import g
from PiConnection import *
from Conditions import *
from Logging import *

conn = sqlite3.connect('SensorFlags.db')
cursor = conn.cursor()
logger("Connected to database")

#part of the intial creation of the database, adds important analysis information
def WriteInitial(name, descriptor, flag, uom, typical):
    try:
        commandstring = '''UPDATE Sensors SET Descriptor = ?,Flag = ?,UOM = ?,Typical = ? WHERE Tag_Name = ?'''
        values = (descriptor, flag, uom, typical, name)
        cursor.execute(commandstring, values)
    except:
        logger("No table! This should never happen.")

#writes condition to the conditions column of the database
def WriteCondition(name, condition):
    try:
        commandstring = '''UPDATE Sensors SET Condition = ? WHERE Tag_Name = ?'''
        values = (condition, name)
        cursor.execute(commandstring, values)
    except:
        logger("Error adding condition to table.")

#reads all tage in the SQL database
def ReadNames():
    cursor.execute('''SELECT Tag_Name FROM Sensors WHERE Flag != "PI"''')
    nameList = cursor.fetchall()
    return(nameList)

#reads a particular row defined by tag
def ReadRecord(sensor):
    cursor.execute('SELECT * FROM Sensors WHERE Tag_Name = ?', (sensor,))
    recordList = cursor.fetchall()
    return(recordList)
    
#allows execution of custom SQL command (not used)
def PassCommand(commandstring, values):
    cursor.execute(commandtring, values)
    return('Complete')

#part of initial database creation, makes the sensor table
def MakeTable():
    try:
        cursor.execute('''CREATE TABLE Sensors(Tag_Name, Descriptor, Flag, UOM, Typical, Condition)''')
    except:
        logger('Already a "Sensors" table')

#adds and removes sensors based on those existing in the PI system
def CompareSensors():
    sensorlist = ReadAllTags() #reads all tags from PI server
    for sensor in sensorlist: #goes through every sensor
        str_sensor = ''.join(sensor)
        cursor.execute('SELECT Tag_Name FROM Sensors WHERE Tag_Name == (?)', (str_sensor,))
        tagexist = cursor.fetchall() #fetches data for tag name from database
        try: #testing if tag exists
            tagexist = str(tagexist[0]) 
        except: #if it doesn't exist, add into database
            cursor.execute('INSERT INTO Sensors(Tag_Name) VALUES(?)', (str_sensor,))
            WriteInitial(str_sensor, GetDescriptor(str_sensor), Flagging(str_sensor),
                         GetEU(str_sensor), GetTypicalValue(str_sensor))
            logger("Inserting new tag into database - {0}".format(str_sensor))
    
    tablelist = ReadNames() #reads all tags from database
    for name in tablelist:
        name = ''.join(name)
        try: #tests if sensor is on PI server
            sensorTest(name)
        except: #deletes if tag has been removed
            cursor.execute("DELETE FROM Sensors WHERE Tag_Name = (?)", (name,))
            logger("Deleting old tag from database - {0}".format(name))
    
    logger('CompareSensors complete!')

#closes the database and saves changes VERY IMPORTANT
def CommitClose():
    conn.commit()
    conn.close()
    logger('Closed SQL connection!')
    return()

#Makes database
def FirstRun(): 
    MakeTable()
    CompareSensors()
