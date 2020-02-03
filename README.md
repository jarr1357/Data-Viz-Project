# Data-Viz-Project

This project is designed to recall data from OSIsoft Pi systems of Algonquin College. The data is then used to determine the condition of sensors and also to display the data in a variety of charts.

ConditionsUpdater coordinates data requests and comparisons to determine sensor health.
PiConnection is responsible for communicating with the Pi system.
DatabaseConnection is responsible for talking with the SQL database.
Conditions has statements defining a healthy sensor.
Logging is basic logging with timestamp.
Cleaner keeps log file manageable (with changeable days to keep).
