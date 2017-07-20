import urequests

print("nmea client beginning")

sentence = urequests.put('http://nmea:5000/api/v1/nmea_faker/sentence',  json={'lat': '123','lon': '456'}, headers={'content-type': 'application/json'})
print(sentence.text)

