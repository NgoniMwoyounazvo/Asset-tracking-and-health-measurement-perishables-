import serial
import time
import string
import os

try:import pynmea2
except:
    print("Installing")
    os.system("pip install pynmea2")
    import pynmea2

while True:
	port="/dev/ttyAMA0"
	ser=serial.Serial(port, baudrate=9600, timeout=0.5)
	dataout = pynmea2.NMEAStreamReader()
	newdata=ser.readline().decode('unicode_escape')

	if newdata[0:6] == "$GPRMC":
		newmsg=pynmea2.parse(newdata)
		lat=newmsg.latitude
		lng=newmsg.longitude
		gps = "Latitude=" + str(lat) + "and Longitude=" + str(lng)
		print(gps)
