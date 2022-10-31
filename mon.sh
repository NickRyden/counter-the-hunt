#!/bin/bash

# Set adapter to monitor mode
interface=$("iw dev | awk '$1==\"Interface\"{print $2}'")
sudo airmon-ng check kill
sudo airmon-ng start $interface

# Adapter has changed, use this insetad.
interface=$("iw dev | awk '$1==\"Interface\"{print $2}'")
kismet -c $interface
sudo aireplay-ng $interface
