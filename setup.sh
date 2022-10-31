# Initial setup
sudo apt -y update && sudo apt -y upgrade
sudo apt install -y python 3.10
sudo apt-get install -y aircrack-ng
sudo apt-get install -y golang-cfssl
sudo apt install -y sqlite3
sudo apt install -y sqlitebrowser

# Install kismet
wget -O - https://www.kismetwireless.net/repos/kismet-release.gpg.key | sudo apt-key add -
echo 'deb https://www.kismetwireless.net/repos/apt/release/focal focal main' | sudo tee /etc/apt/sources.list.d/kismet.list
sudo apt -y update
sudo apt install -y kismet

# Python pips
pip3 install kismet

# Source: https://www.freecodecamp.org/news/wireless-security-using-raspberry-pi-4-kismet-and-python/

# Set a SUID for kismet for security
sudo usermod --append --groups kismet $USER
