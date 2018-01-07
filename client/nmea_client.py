# Author Brendan Horan
# License : BSD 3-Clause
# Description : Get a NMEA setence from the NMEA faker sever

import urequests
import time
from machine import UART

class NMEA_Base:
  def __init__(self,rx_pin, tx_pin,server_address):
    uart = UART(1, 4800, timeout=0)
    uart.init(4800, bits=8, parity=None, stop=1, rx=rx_pin, tx=tx_pin)
    self.uart = uart
    self.server_address = server_address

class NMEA_client(NMEA_Base):
  def get_sentence(self):
    sentence = urequests.put('http://'+self.server_address+'/api/v1/nmea_faker/sentence',
    json={'lat': '123','lon': '456'},
    headers={'content-type': 'application/json'})
    self.uart.write(sentence.text)
    return(sentence.text)
