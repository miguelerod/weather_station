"""

My First Internet of Things

Temperature/Humidity Light monitor using Raspberry Pi, DHT11

Data is displayed at thingspeak.com

2015/06/15

SolderingSunday.com

Based on project by Mahesh Venkitachalam at electronut.in

"""

# Import all the libraries we need to run

import sys

import os

from time import sleep

import Adafruit_DHT

import urllib.request

# Setup the pin we connect to

DHTpin = 4


#Setup our API and delay

myAPI = "aabbcc"

myDelay = 5 #how many seconds between posting data

def getSensorData():

    humidity, tempc = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, DHTpin)

    #Convert from Celius to Farenheit

    tempf = 9/5*tempc+32

    # return dict

    return (str(humidity), str(tempc),str(tempf))

# main() function

def main():

    print('starting...')

    baseURL = 'http://gregory.website/apps/posberry/post.php?token=%s' % myAPI

    print(baseURL)

    while True:

        humidity, tempc, tempf = getSensorData()
        
        url = urllib.request.urlopen(baseURL +

        "&tempc=%s&tempf=%s&humedad=%s&lum=%s" % (tempc, tempf, humidity, 1.00))

        url.read()
        
        print("tempC " + tempc + ", tempF " + tempf+ ", humidity " + humidity)

        sleep(int(myDelay))

# call main

if __name__ == "__main__":

    main()