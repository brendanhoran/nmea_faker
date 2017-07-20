# nmea_faker
Restful nmea sentences

Work in progress.

Get a GPRMC NMEA sentence via a REST api    

Eg :   

```
curl -X put -H "Content-Type: application/json" -d '{"lat": "123","lon": "456"}' http://localhost:5000/api/v1/nmea_faker/sentence
```
