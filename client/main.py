# Author Brendan Horan
# License : BSD 3-Clause
# Description : Get a NMEA setence from the NMEA faker sever

import wifi_setup
import nmea_client
import time
wifi_setup = wifi_setup.WIFI_setup('YOUR_SSID','YOUR_PASSWORD')
wifi_setup.connect()

# format is, RX pin, TX pin, IP address and port of server
nmea_client = nmea_client.NMEA_client(25,26,'127.0.0.1:5000')

time.sleep(10)
print("Starting NMEA client, REPL will not spawn")
task_start_time = time.time()
while True:
  nmea_client.get_sentence()
  time.sleep(60.0 - ((time.time() - task_start_time) % 60.0))
