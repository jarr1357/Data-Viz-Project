from __future__ import print_function

from datetime import datetime, timedelta

from sys import exit, path

import adodbapi

import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)


def operational_data():

  days_back = 7

 

  # Connect to the ODI PI server.
  try:

      conn_str = "Provider=PIOLEDBENT.1;Integrated Security=SSPI;" \
      "Persist Security Info=False;Initial Catalog=ODI-AF;" \
      "Data Source=DEV-AF"

      print(conn_str)

      db = adodbapi.connect(conn_str, timeout=100000)

      cur = db.cursor()

      operational_data = retrieve_operational_data(cur, days_back)

  except:

       print("Failed to connect to database")
 

def retrieve_operational_data(cur, days_back):

  # Composition of string can be ascertained from the OLEDB Enterprise manual.

  sql = """SELECT eh.Path + eh.Name + ea.Path + ea.Name Path, ar.Time, ar.Value
  FROM [ODI-AF].[Asset].[ElementHierarchy] eh
  INNER JOIN [ODI-AF].[Asset].[ElementAttribute] ea on eh.ElementID=ea.ElementID
  INNER JOIN [ODI-AF].Data.Archive ar ON ar.ElementAttributeID = ea.ID
  WHERE eh.Path LIKE N'\%'
  and ea.Name IN (N'%')
  and ar.Time > N'*-{1}d'
  OPTION (FORCE ORDER)"""

  try:

      cur.execute(sql.format(sql, days_back))

      operational_data = cur.fetchall()
      print ("Testing")      

      return operational_data

  except:

      error_msg = "Failed to retrieve information from the AF server."
      print(error_msg)

 

  return []

 

  return operational_data

 

if __name__ == "__main__":

  try:

      operational_data()

  except KeyboardInterrupt:

      exception_message = "Ctrl-C pressed. Stopping..."
      print(exception_message)
