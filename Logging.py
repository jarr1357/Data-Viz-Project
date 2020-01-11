import datetime

def logger(msg):
    """removes milliseconds, writes passed msg with date and time to log file"""

    f = open("log_file.txt", "a")
    time = str(datetime.datetime.now())
    time = time[:-(len(time) - time.find('.'))]
    f.write("{0} - {1}\n".format(time, msg))
    print("{0} - {1}\n".format(time, msg))
    f.close()


