import sqlite3

conn = sqlite3.connect('SensorFlags.db')

cursor = conn.cursor()
    
def WriteValue(name, current_value, condition):
    try:
        commandstring = '''UPDATE Sensors SET Current_Value = ? ,Condition = ? WHERE Tag_Name = ?'''
        values = (current_value, condition, name)
        cursor.execute(commandstring, values)
    except:
        print("No table!")

def ReadNames():
    cursor.execute('''SELECT Tag_Name FROM Sensors''')
    nameList = cursor.fetchall()
    return(nameList)

def CommitClose():
    conn.commit()
    conn.close()
    return('Closed SQL connection!')
