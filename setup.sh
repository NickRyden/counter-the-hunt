# Initial setup
sudo apt -y update && sudo apt -y upgrade
sudo apt install -y python 3.10
sudo apt-get install -y aircrack-ng
sudo apt install bluetooth libbluetooth-dev
sudo apt-get install -y golang-cfssl
sudo apt install -y sqlite3
sudo apt install -y sqlitebrowser

# Install kismet
wget -O - https://www.kismetwireless.net/repos/kismet-release.gpg.key | sudo apt-key add -
echo 'deb https://www.kismetwireless.net/repos/apt/release/focal focal main' | sudo tee /etc/apt/sources.list.d/kismet.list
sudo apt update
sudo apt install kismet

# Python pips
pip3 install scapy
pip3 install kismet
pip3 install pybluez
pip3 install PyQt5

# Source: https://www.freecodecamp.org/news/wireless-security-using-raspberry-pi-4-kismet-and-python/

# Set a SUID for kismet for security
sudo usermod --append --groups kismet $USER
