#!/bin/bash
# find device
/etc/netplan$ /bin/lsusb | grep "wireless"

# Drivers
ls /sys/bus/usb/drivers/{usb_device}/*:1.0/net/

# put detected device into monitor mode in rc.local
#!/bin/bash
usb_driver=rt2800usb
wlan=\$(/bin/ls /sys/bus/usb/drivers/\$usb_driver/*/net/)
if [ $? -eq 0 ]; then
        set -ex
        /usr/sbin/ifconfig "\$wlan" down
        /usr/sbin/iwconfig "\$wlan" mode monitor
        /usr/sbin/ifconfig "\$wlan" up
        set +ex
fi
RC_LOCAL

# Make rc.local executable and put device into mon mode
sudo chmod u+x /etc/rc.local && shutdown -r now "Enabling monitor mode"

# check adapter is in monitor mode
iwconfig wlan1

