#!/usr/bin/python
# License : BSD 3-Clause
# Version :0.0.1
# Author  : Brendan Horan


import pynmea2, time
from flask import Flask
from flask_restful import Resource, Api, reqparse


app = Flask(__name__)
api = Api(app, prefix="/api/v1")


nmea_sentence_parser = reqparse.RequestParser()
nmea_sentence_parser.add_argument("lat", type=float, required=True, help="Input latitude coordinates")
nmea_sentence_parser.add_argument("lon", type=float, required=True, help="Input longitude coordinates")


class server_info(Resource):
    def get(self):
        info = "nmea_faker server"
        return(info, 200)

class nmea_sentence(Resource):
    def put(self):
        coordinates = nmea_sentence_parser.parse_args(strict=True)
        utc_time = time.strftime("%H%M%S", time.gmtime())
        utc_date = time.strftime("%d%m%y", time.gmtime())
 
        nmea_raw = "$GPRMC,{0},A,{2},N,{3},E,0.168,,{1},,,A".format(utc_time, utc_date, coordinates.lat, coordinates.lon)
        nmea_gprmc = pynmea2.parse(nmea_raw)
        nmea_gprmc = str(nmea_gprmc)
        return(nmea_gprmc, 201)

def run_server():
    api.add_resource(server_info, '/nmea_faker')
    api.add_resource(nmea_sentence, '/nmea_faker/sentence')
    app.run(debug=True)

if __name__ == '__main__':
    run_server()
