# nmea_faker
Restful nmea sentences

Get a GPRMC NMEA sentence via a REST api    

## Usage

See the server and client directorys for more details.    

To query the server, you can use the below example:     

```
curl -X put -H "Content-Type: application/json" -d '{"lat": "123","lon": "456"}' http://localhost:5000/api/v1/nmea_faker/sentence
```    

Also supports ESP32 micro as a client.    
The client will sent a REST reqest to the server every 60 seconds and then send the raw GPRMC string out over serial to the device expecting a GPS GPRMC string.    
Thus allowing dumb devices to sync via GPRMC over local networks with no GPS devices,   
