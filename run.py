#!/usr/bin/env python3

# Data tools
import sqlite3
import json

# Time and scheduling tools
import time
import datetime
import pytz
import sched
import threading

import os # Operating system
import subprocess

import re # Regex
from colorama import Fore, Back, Style # Terminal colours
import atexit

# Hashing and encoding
import base64
import hashlib
import uuid

# global variables
kismet_db = ''
analysis_db = 'analysis.db'
now = 0
alert_length = 5 # Minutes
schedule = sched.scheduler(time.time, time.sleep)
threadLock = threading.Lock()
global_counter = 0

# Fimd compatible .kismet files in the directory using regex
for file in os.listdir():
    if re.match('Kismet-([0-9]+(-[0-9]+)+)\.kismet(?!.[a-zA-Z])', file):
        kismet_db = file

def getEpochTime():
    dt = datetime.datetime.now()
    epoch_time = datetime.datetime(1970, 1, 1)
    delta = abs(dt - epoch_time)
    return round(delta.total_seconds(), 0)

start_time = getEpochTime()

def timeFull(epoch):
    # Hours, minutess and seconds (hh:mm:ss)
    return datetime.timedelta(seconds=epoch)

#calculate approximate distace from adapter
def calcDist(dBm):
    dist_ref = 1
    power_ref = -55 # arbitrary value
    path_loss_exp = 2.0
    stdev_power = 2.5
    # Any object, such as walls creates uncertainty
    uncertainty = 2*stdev_power

    # Calculate the estimate, min and max
    d_est = round(dist_ref*(10**(-(dBm - power_ref)/(10*path_loss_exp))), 2)
    d_min = round(dist_ref*(10**(-(dBm - power_ref + uncertainty)/(10*path_loss_exp))), 2)
    d_max = round(dist_ref*(10**(-(dBm - power_ref - uncertainty)/(10*path_loss_exp))), 2)
    return [d_est, d_min, d_max]

# Initiate the database connection
def conn(db_file):
    dbconn = None
    try:
        dbconn = sqlite3.connect(db_file, isolation_level=None)
    except:
        print('Database connection failed')
    
    return dbconn

# TO-DO: Implement when i can get a UI working
def whitelist(mac_addr):
    cur = conn(analysis_db).cursor()
    cur.execute("INSERT INTO whitelist () VALUES ()")
    return 'MAC address', mac_addr, 'added to the whitellist.'

# Check MAC Addresses against our whitelist table
def checkWhitelist(mac):
    cur = conn(analysis_db).cursor()
    cur.execute("SELECT mac_addr, friendly_name FROM whitelist WHERE mac_addr='" + mac + "'")

    row = cur.fetchone()
    if row is None:
        return False
    else:
        return True

def analysis(first, last, data):
    now = getEpochTime() - abs(time.localtime().tm_gmtoff)
    #now = 1667124227 - 39600 # Convert to UTC

    last_between = abs(int(last) - now)
    first_between = abs(int(first) - now)

    # Convert to hours, minutes and seconds
    follow_time = str(timeFull(first_between))

    # Calculate the Distance and the deviationprint(now, first, last, kismet_db)
    dist = calcDist(data[4])
    deviation = round(abs(((dist[2] - dist[1]) / 2)), 2)

    # We don't care for Wi-Fi Access Points
    if data[7] == 'Wi-Fi Client' or data[7] == 'Wi-Fi Bridge':
        if last_between >= 120:
            if first_between >= 240:
                # Print out an alert
                print(Back.RED, Fore.WHITE + 'ALERT: You\'re likely being followed', Style.RESET_ALL)
                print('Followed for ', follow_time)
                print('Distance: ', dist[0],'m', u"\u00B1", deviation, 'm')
                print('Device type: : ', data[7])
                print('Manufacturer: ', data[6])
                print('Data added to forensics database for further investigation')

                # Initiate variables
                arrItem = []
                strHash = ''

                # Generates a unique id for each alert
                uniqueID = str(uuid.uuid4())

                arrData = (data[2], follow_time, first, last, data)

                # Convert everything to base64, escape special characters
                for items in arrData:
                    item = str(items)
                    bytes = item.encode('ascii')
                    base = base64.b64encode(bytes)
                    strFinal = str(base)[2:-1]
                    strHash += strFinal
                    arrItem.append(strFinal)
                
                # Geneate our hashes for our data
                md5 = hashlib.md5(strHash.encode('utf-8')).hexdigest()
                sha256 = hashlib.sha256(strHash.encode('utf-8')).hexdigest()

                # Insert data into the forensics table...
                cur = conn(analysis_db).cursor()
                insert_data = (uniqueID, arrItem[0], arrItem[1], arrItem[2], arrItem[3], arrItem[4])
                query = """INSERT OR IGNORE INTO forensics (id, mac_addr, time_followed, first_time, last_time, details) VALUES (?,?,?,?,?,?);"""
                cur.execute(query, insert_data)

                # ...or update it if it exists
                insert_data = (uniqueID, arrItem[1], arrItem[3], str(arrItem[0]))
                query = """UPDATE forensics SET id=?, time_followed=?, last_time=? WHERE mac_addr=?;"""
                cur.execute(query, insert_data)

                # Put our hashes into the hashes table...
                insert_data = (uniqueID, md5, sha256)
                query = """INSERT OR IGNORE INTO hashes (id, md5, sha256) values (?,?,?);"""
                cur.execute(query, insert_data)

                # ...or update it if our hashes already exist
                insert_data = (uniqueID, md5, sha256, md5, sha256)
                query = """UPDATE hashes SET id=?, md5=?, sha256=? WHERE md5=? AND sha256=?;"""
                cur.execute(query, insert_data)

        else:
            # Print a yellow warning, no data captured.
            print(Back.YELLOW + 'ALERT: Stay vigilant, Distance:', dist[0],'m', u"\u00B1", deviation, 'm', Style.RESET_ALL)

def main():
    # Get our counter
    global global_counter

    # Grab all of our Kismet data
    cur = conn(kismet_db).cursor()
    cur.execute("SELECT devmac, first_time, last_time, strongest_signal, device FROM devices")

    rows = cur.fetchall()

    # Recursive process
    for row in rows:
        if checkWhitelist(row[0]) is True:
            print(Back.GREEN + "Friendly in range", Style.RESET_ALL)
        else:
            # Required for some reason
            devmac, first_time, last_time, signal, device_info = row

            # Grab from our row array
            devmac = row[0]
            first_time = row[1]
            last_time = row[2]
            signal = row[3]

            # Clean and load our JSON record
            device_json = str(row[4])
            clean = device_json[2:-1]
            try:
                obj = json.loads(clean)

                mac_addr = obj['kismet.device.base.macaddr']
                freq = obj['kismet.device.base.freq_khz_map']
                crypt = obj['kismet.device.base.crypt']
                manufacturer = obj['kismet.device.base.manuf']
                device_type = obj['kismet.device.base.type']
                device_name = obj['kismet.device.base.phyname']
                bssid = obj['dot11.device']['dot11.device.last_bssid']

                # Put our data into a list
                data = [first_time, last_time, mac_addr, freq, signal, crypt, manufacturer, device_type, device_name, bssid]

                # Run our analysis once Kismet has populated
                if global_counter > 0:
                    analysis(first_time, last_time, data)
            except:
                print(Back.BLUE + "UUID Unicode encode failed'", Style.RESET_ALL)

    # Determine if its the first iteration
    if global_counter == 0:
        print('Allowing Kismet to gather data...')
    else:
        print('Analysis complete')

    # Increment our global counter
    with threadLock:
        global_counter += 1
    
    # Refresh program every 5 (arbitrary) seconds
    time.sleep(5)
    threading.Timer(alert_length, main).start()

# Run main on start
if __name__ == "__main__":
    main()

# On closing our program...
def exit_handler():
    print('closing')
    # TO-DO: Kill Kismet
    # TO-DO: Delete Kismet db

atexit.register(exit_handler)
