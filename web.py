import flask
import json
from flask import jsonify

from DatabaseConnection import *

app = flask.Flask(__name__)
app.config["DEBUG"] = True

logger('Refreshing JSON')

sensorlist = ReadAllTags()


JSONs = []
idCount = 0

for sensor in sensorlist:
  
    sensor = ''.join(sensor)    
  
    record = ReadRecord(sensor)
    recordTuple = record[0]
    
    entery = {'id': idCount,
             'Tag_Name': recordTuple[0],
             'Descriptor': recordTuple[1],
             'Flag': recordTuple[2],
             'UOM': recordTuple[3],
             'Typical': recordTuple[4],
             'Condition': recordTuple[5]
             }
  
    idCount = idCount + 1
   
    JSONs.append(entery)
          
CommitClose()

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Algonquin Data Viz</h1>
<p>A prototype API for getting sensor data. Go to /json.</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/json', methods=['GET'])
def api_all():  
    return jsonify(JSONs)

app.run(debug = False)

