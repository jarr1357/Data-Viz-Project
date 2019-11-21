import sqlite3

from DatabaseConnection import CommitClose
from PiConnection import ReadAllTags

conn = sqlite3.connect('SensorFlags.db')

cursor = conn.cursor()

def MakeTable():
    try:
        cursor.execute('''CREATE TABLE Sensors(Tag_Name, Flag, Current_Value, Condition)''')
    except:
        print("Already a table")

    sensorlist = ReadAllTags()

    for sensor in sensorlist: #goes through every sensor
        str_sensor = ''.join(sensor)
        cursor.execute('INSERT INTO Sensors(Tag_Name) VALUES(?)', (str_sensor,))
        print(str_sensor)

MakeTable()

conn.commit()
conn.close()
print('Closed SQL connection!')
