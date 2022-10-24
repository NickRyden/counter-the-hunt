import math

def calcDist(dBm, frequency):
    return pow(10.0, (27.55 - (20 * math.log(frequency, 10) + abs(dBm)) / 20.0))

print(calcDist(57, 2412), "m")
