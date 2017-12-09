import network
import sys
import time

print("Wifi setup beginning")
wlan = network.WLAN(network.STA_IF); wlan.active(True)
wlan.active(True)
wlan.connect("SSID", "PASSWORD")
time.sleep(5)

if wlan.isconnected() == False:
  print("WiFi not connected")
  wlan.disconnect()
else:
  print("Wifi connected")
  print(wlan.ifconfig())
