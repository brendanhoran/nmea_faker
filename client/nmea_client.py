import urequests
import time

print("NMEA client beginning")
print("REPL prompt will not spawn")

task_start_time = time.time()
while True:
  sentence = urequests.put('http://nmea:5000/api/v1/nmea_faker/sentence',
    json={'lat': '123','lon': '456'},
    headers={'content-type': 'application/json'})
  print(sentence.text)
  time.sleep(60.0 - ((time.time() - task_start_time) % 60.0))

