#/bin/bash

# Find the process ID and stop Kismet
process_id=$(pidof kismet)
kill $process_id

# Stop monitor mode and restore internet connectivity on the wireless adapter
interface=$(iw dev | awk '$1=="Interface"{print $2}') 
sudo airmon-ng stop $interface

interface=$(iw dev | awk '$1=="Interface"{print $2}') 
sudo ifconfig $interface up

sudo service NetworkManager restart
