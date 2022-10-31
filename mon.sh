#!/bin/bash

# !IMPORTANT - Run at first start
# sudo usermod --append --groups kismet $USER
# AND
# Create a username and password in the Kismet web interface at http://localhost:2501

# Set adapter to monitor mode
interface=$("iw dev | awk '$1==\"Interface\"{print $2}'")
sudo airmon-ng check kill
sudo airmon-ng start $interface

# Adapter has changed, use this insetad.
interface=$("iw dev | awk '$1==\"Interface\"{print $2}'")
kismet -c $interface
sudo aireplay-ng $interface
