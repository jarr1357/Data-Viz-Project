import sqlite3
conn = sqlite3.connect('SensorFlags.db')

c = conn.cursor()

def MakeTable():
    try:
        c.execute('''CREATE TABLE Sensors
             (name, current_value, flag)''')
    except:
        print("Already a table")

def WriteValue(name, current_value, flag):
    commandstring = ("INSERT INTO Sensors VALUES ('{0}','{1}') WHERE name = {2}".format(current_value, flag, name))
    c.execute(commandstring)

def CommitClose():
    conn.commit()
    conn.close()
