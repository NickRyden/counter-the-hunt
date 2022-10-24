from datetime import datetime

def getSeconds():
    dt = datetime(2018, 10, 22, 0, 0)
    kismet_time = datetime(2019, 1, 1)
    delta = abs(dt - kismet_time)
    return delta.total_seconds()

print('Datetime to Seconds since kismet:', getSeconds())
