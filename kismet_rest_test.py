#!/usr/bin/enc python3

# Source: https://github.com/kismetwireless/python-kismet-rest

import kismet
import kismet_rest

# Legacy functionality (KismetConnector):
conn = kismet_rest.KismetConnector(username="my_user", password="my_pass")
for device in conn.device_summary():
    pprint.pprint(device)

# Alerts since 2019-01-01:
alerts = kismet_rest.Alerts()
for alert in alerts.all(ts_sec=1546300800):
    print(alert)

# Devices last observed since 2019-01-01:
devices = kismet_rest.Devices()
for device in devices.all(ts=1546300800):
    print(device)
