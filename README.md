# war-driver
War driving utility - Jesus takes the wheel

## Description
Originally got the idea from a PC Mag article [https://au.pcmag.com/security/95637/are-you-being-followed-use-a-raspberry-pi-to-find-out], So i thought it might be an interesting challenge to try and biuld it. Originally was going to build it on a raspberry pi with a wifi adapter, GPS module and a pelican case, however there were a few issues to overcome on ARM architehture. Instead, I am using a laptop to build the project.

## Technical Details
Essentially, data will be captured and stored in a db file, read into python and analysed every 'n' minutes depending on a person's moving speed and analyse if someone is being followed.

## Tools
Python 3.10
Kismet
Scapy

