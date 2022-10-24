from datetime import datetime

def getEpochTime():
    dt = datetime(2018, 10, 22, 0, 0)
    kismet_time = datetime(1970, 1, 1)
    delta = abs(dt - kismet_time)
    return delta.total_seconds()

def createAlertInterval(alert_length):
    # Return an alert in seconds minus the alert length
    return getEpochTime() - (alert_length * 60)

print(getEpochTime())
print(createAlertInterval(5))
print(createAlertInterval(10))
print(createAlertInterval(15))
print(createAlertInterval(20))
print(createAlertInterval(25))
