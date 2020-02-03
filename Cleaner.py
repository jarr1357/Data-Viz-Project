import datetime
from calendar import monthrange
from Logging import *

def cleaner():
    """takes today's date and calculates date of "dayskept" days ago
    then rewrites logs made after that date"""

    dayskept = 1 #number of days logs to keep
    
    date = datetime.datetime.today()

    removeyear = date.year
    removemonth = date.month
    removeday = date.day

    remaining = dayskept

    while remaining > 0:

        remaining = remaining - 1 #Keep days and counter seperate
        removeday = removeday - 1 #Days are modified apart from just -1

        if removeday == 0:
            if removemonth == 1:
                removemonth = 12
                removeyear = removeyear - 1
            else:
                removemonth = removemonth - 1
            removeday = int(monthrange(removeyear, removemonth)[1])

    #buffers existing log file
    f = open("log_file.txt", "r")
    searchlines = f.readlines()
    f.close()

    #only rewrites log enteries after calculated day
    f = open("log_file.txt", "w")
    count = 0

    for i, line in enumerate(searchlines):
        day = int(line[8:10]) #extracting times from the log lines
        month = int(line[5:7])
        year = int(line[0:4])

        if year < removeyear: #logic to figure out if a log is before or after
            count = count + 1 #Ignore the line, does NOT write

        elif year == removeyear:

            if month < removemonth:
                count = count + 1

            elif month == removemonth:

                if day < removeday:
                    count = count + 1

        #If no conditions are met, write the line
                else:
                    f.write(line)
            else:
                f.write(line)
        else:
            f.write(line)

    f.close()
    logger("Cleaner overwrote {0} enteries older than {1}/{2}/{3}".format(count,removemonth,removeday,removeyear))

cleaner()
