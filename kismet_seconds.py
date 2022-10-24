from datetime import datetime

def getEpochTime():
    dt = datetime(2018, 10, 22, 0, 0)
    kismet_time = datetime(1970, 1, 1)
    delta = abs(dt - kismet_time)
    return delta.total_seconds()

print(getEpochTime())
