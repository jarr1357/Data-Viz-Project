import sqlite3
import pandas as pd

from DatabaseInteraction import CommitClose

conn = sqlite3.connect('SensorFlags.db')

cursor = conn.cursor()

def MakeTable():
    try:
        cursor.execute('''CREATE TABLE Sensors(Tag_Name, Flag, Current_Value, Condition)''')
    except:
        print("Already a table")

    df = pd.read_excel (r'sensor_list.xlsx')
    sensorlist = pd.DataFrame(df, columns= ['Name'])

    scount = 0 #sensor count starts at row 3
    slen = len(sensorlist.index)-1 #-1 for zero offset

    while scount <= slen: #goes through every sensor
        sensor = sensorlist.at[scount, 'Name']
        scount = scount + 1

        cursor.execute('INSERT INTO Sensors(Tag_Name) VALUES(?)', (sensor,))
        print(sensor)

MakeTable()

print(CommitClose())
