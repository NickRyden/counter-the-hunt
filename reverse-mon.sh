#!/bin/bash

# Kill Kismet
pid=$(pidof kismet)
kill pid

# Reset connection
interface=$("iw dev | awk '$1=="Interface"{print $2}'")
airmon-ng stop $interface
ifconfig $interface up

# Restart the Network manager
sudo service NetworkManager restart
