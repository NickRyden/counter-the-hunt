# Counter the Hunt
I am extending a war-driving tool, Kismet, to check if the user is being followed

## Description
Originally got the idea from a <a href="https://au.pcmag.com/security/95637/are-you-being-followed-use-a-raspberry-pi-to-find-out">PC Mag article</a>, So I thought it might be an exciting challenge to try and build it. I would have done the project with a raspberry pi and a wifi adapter. However, there were a few issues to overcome with the Operating systems. Instead, I am using a laptop loaded with Linux Mint to build the project.

## Technical Details
Essentially, data will be captured and stored in a *.db file, read into python and analysed every 'n' minutes depending on a person's moving speed and investigate if someone is being followed.

## Tools
* Python 3.10
* Kismet
* Aircrack-ng
* SQLite3 Database Browser

## Instructions

1. Give setup.sh executable privileges and run the script <code>sudo chmod +x setup.sh && ./setup.sh</code>
2. Import analysis.sql into the Sqlite3 database browser and save it as analysis.db <code>cat analysis.sql | sqlite3 analysis.db</code>
3. Give mon.sh and reverse-mon.sh chmod executable privileges <code>sudo chmod +x mon.sh && chmod +x reverse-mon.sh</code>
4. Run mon.sh <code>./mon.sh</code>
5. Run the python script, run.py using <code>python3 run.py</code>. It will start analysing and produce alerts after 3 minutes and 4 minutes
6. Once finished, run reverse-mon.sh <code>./reverse-mon.sh</code> to stop Kismet and restore internet connectivity.

# Technical notes

## Dot11Beacons
Dot11Beacons are beacons given off by 802.11-compliant devices, which other devices use to determine signal strength, BSSIDs and SSIDs for a connection.
The wireless client's beacons are captured, and their data is decoded and analysed for further use. Dot11 signals contain valuable information when war-driving, including a device's BSSID, SSID, the channel in use and the Cryptography a device is utilising (WEP, WAP, WPA2 etc.)

## Limitations
* MAC address randomisation.
* Unicode decode errors for Wifi Protected Setup (WPS) UUIDs.
* Wireless adapter range.

## Tools and equipment
Tools used:
Laptop with Linux Mint
Kismet
Python
SQLite3 Database Browser
