# Initial setup
sudo apt -y update && sudo apt -y upgrade
sudo apt install -y python 3.10
sudo apt-get install -y aircrack-ng
sudo apt install bluetooth libbluetooth-dev
sudo apt-get install -y golang-cfssl

# Install kismet
wget -O - https://www.kismetwireless.net/repos/kismet-release.gpg.key | sudo apt-key add -
echo 'deb https://www.kismetwireless.net/repos/apt/release/focal focal main' | sudo tee /etc/apt/sources.list.d/kismet.list
sudo apt update
sudo apt install kismet

# Python pips
pip3 install scapy
pip3 install kismet
pip3 install kismetdb
pip3 install kismet_rest
pip3 install pandas
pip3 install pybluez
pip3 install kismet-analyzer


# Source: https://www.freecodecamp.org/news/wireless-security-using-raspberry-pi-4-kismet-and-python/

# Set a SUID for kismet for security
sudo usermod --append --groups kismet $USER

# Create a SSL encryption to use Kismet
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -sha256 -days 365

# Kismet web override
#!/bin/bash
# Kismet setup
usb_driver=rt2800usb
wlan=$(ls /sys/bus/usb/drivers/$usb_driver/*/net/)
if [ $? -eq 0 ]; then
    set -ex
    /usr/sbin/ifconfig "$wlan" down
    /usr/sbin/iwconfig "$wlan" mode monitor
    /usr/sbin/ifconfig "$wlan" up
    set +ex
    /bin/cat<<KISMETOVERR>/etc/kismet/kismet_site.conf
server_name=Nunez Barrios Kismet server
logprefix=/data/kismet
source=$wlan
httpd_ssl=true
httpd_ssl_cert=/etc/pki/raspberrypi/raspberry-server.csr
httpd_ssl_key=/etc/pki/raspberrypi/raspberry-server-key.pem
KISMETOVERR
fi

# start Kismet - non-root
kismet
# access from http://localhost:2501

print_f("Access from http://localhost:2501, First time must setup Username and Password");
