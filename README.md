# Counter the hunt
Using a war driving tool to see if you're being hunted.

## Description
Originally got the idea from a <a href="https://au.pcmag.com/security/95637/are-you-being-followed-use-a-raspberry-pi-to-find-out">PC Mag article</a>, So i thought it might be an interesting challenge to try and build it. Originally was going to build it on a raspberry pi with a wifi adapter, GPS module and a pelican case, however there were a few issues to overcome on ARM architehture. Instead, I am using a laptop to build the project.

## Technical Details
Essentially, data will be captured and stored in a db file, read into python and analysed every 'n' minutes depending on a person's moving speed and analyse if someone is being followed.

## Tools
* Python 3.10
* Kismet
* Scapy
* Aircrack-ng (sp. airmon-ng)

## Instructions

1. Give setup.sh executable privileges and run the script <code>sudo chmod +x setup.sh && ./setup.sh</code>
2. Import analysis.sql into Sqlite3 database browser and save as analysis.db <code>cat analysis.sql | sqlite3 analysis.db</code>
3. Give mon.sh, reverse-mon.sh chmod executable privileges <code>sudo chmod +x mon.sh && chmod +x reverse-mon.sh</code>
4. Run mon.sh <code>./mon.sh</code>
5. Run the python script, run.py using <code>python3 run.py</code>. It will start analysing and produce alerts after 3 minutes and 4 minutes
6. Once finished, run reverse-mon.sh <code>./reverse-mon.sh</code> to stop Kismet and restore internet connectivity.
