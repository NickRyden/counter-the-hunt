# Technical notes

## Overview
Originally this project was designed to be launched on a raspberry pi, however due to restraints of the ARM architechture we used a laptop to launch the project. The aim is to research and develop a tool that detects surveillance or reconnaisance devices tracking an individual. Chances are that even if stalkers or state-backed operatives are using surveillance devices, that a perpetrator entering an area will still have a phone one them.

## Dot11Beacons
Dot11Beacons are beacons given off by 802.11 complient devices which other devices use to determine signal strength, BSSIDs and SSIDs for a connection.
These beacons can be captured and their data decoded and analysed for further use. Doc11 signals contain valueable information when war driving including a device's BSSID, SSID
the channel in use and the Cryptography a device is utilising (WEP, WAP, WPA2 etc)

## Discussions on limitations
What if the device following you is recursively using a MAC changer to regularly change their MAC address. Again, chances are that even if stalkers or state-backed operatives are using surveillance devices, that a perpetrator entering an area will still have a phone one them. If the same device is in your vicinity, there is a decent chance you're being followed.


## Calculating approximate distance from signal strength and frequency
Signal distance, measured in dBm, can be approximated using the following formula - 10^(27.55 * log10(frequency), absoluteOf(dBm) / 20.0).
From this formula we can measure the approximate distance, in meters, where a device is located around us - without a known bearing.
The signal strength and distance can vary signficantly due to a number of factors including walls and other surrounding or interferring signals.
There is no real way of determining it a signal is using the 5GHz band or the 2.4GHz band.

## Analysis over time

## Taking down our managed adapter
Identify the adapter to use (show on presentation slide)
Determine the location of the driver in use
Put the detected device into monitor mode using airmon-ng

## Tools and equipment
Tools used:
Laptop with Linux Mint
Kismet enabled with logging
Python (Pips: Pips: Pandas, Pybluez, kismetdb, kismet_analyzer, kismet_rest)
Aircrack-ng
SQLite 3 databse browser

## Steps to analysis
1. Convert our Wireless adapter from managed mode into monitor mode.
2. Capture Dot11 Signals
3. Allow Kismet to record timestamps and the data of devices surrounding our Wireless Adapter
4. Using Python to analyse the .kismet logs - just a fancier SQLite 3 database.
5. Determine if there are any devices around our wireless adapter that have been following the user over the course of 5 to 10 minutes depending on speed.
6. Determine if a user or their follower has changed distance or GPS location.



