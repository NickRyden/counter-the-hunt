#!/bin/bash
interface=$(iw dev | awk '$1=="Interface"{print $2}') 

sudo airmon-ng check kill
sudo airmon-ng start $interface

# Grab the new interface name and run kismet in the background
newInterface=$(iw dev | awk '$1=="Interface"{print $2}') 
nohup kismet -c $newInterface & disown

# OR don't background the process with...
#newInterface=$(iw dev | awk '$1=="Interface"{print $2}') 
#kismet -c $newInterface


### NOTES #####################################
# Either way, running reverse-mon.sh will stop
# Kismet and restore internet connectivity

# Connect to Kismet using http://localhost:2501
