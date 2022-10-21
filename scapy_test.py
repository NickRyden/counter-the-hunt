#!/usr/bin/env python3

from scapy.all import *
from threading import Thread
import os
import time
import scapy
import pandas
import subprocess

# Put wireless adapter into monitor mode, can be achieved with 'sudo ifconfig wlan0 down' and 'sudo iwconfig wlan0 mode monitor'
subprocess.run('sudo airmon-ng check kill')
subprocess.run('sudo airmon-ng start wlan1')
subprocess.run('sudo kismet -c wlan1')

# Dataframes that contains all nearby access points
networks = pandas.Datarame(columns={"BSSID","SSID","dBm_Signal","Channel", "Crypto"})
networks.set_index("BSSID", inplace=True)

def callback(packet):
    if packet.haslayer(Dot11Beacon):
    # Extract MAC address of the network
        bssid = packet[Dot11].addr2
        ssid = packet [Dot11Elt].info.decode()
        try:
            dbm_signal = packet.dBm_AntSignal
        except:
            dbm_signal = "N/A"

        # Extract network stats
        stats = packet[Dot11Beacon].network_stats()
        # Get the channel of the AP
        channel = stats.get("channel")
        # Get the cryptography used by the AP
        crypto = stats.get("crypto")
        
        # Put it all together
        networks.loc[bssid] = (ssid, dbm_signal, channel, crypto)

def print_all():
    while True:
        os.system("clear")
        print(networks)
        time.sleep(0.5)

def change_channels():
    ch = 1
    while True:
        os.system(f"iwconfig {interface} channel {ch}")
        # Switch the channel every n seconds
        ch = ch % 14 + 1
        time.sleep(0.5)
        
if __name__ == "__main__":
    # Set interface name, check by using iwconfig
    interface = "wlan1mon"
    # Start the thread to print all networks
    printer = Thread(target=print_all)
    # Summon a Daemon
    printer.daemon = True
    printer.start
    
    # Start the channel changer
    channel_changer = Thread(target=change_channels)
    channel_changer.daemon = True
    channel_changer.start()
    
    # Start sniffing for packets
    sniff(prn=callback, iface=interface)
