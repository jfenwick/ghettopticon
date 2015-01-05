import serial
import time

arduino = serial.Serial('/dev/tty.usbmodem14141',9600)

import struct

fi = open('testdata', 'r')
for line in fi:
	values = line.strip().split(',')
	arduino.write(struct.pack('>B', 255))
	for i in values:
		arduino.write(struct.pack('>B', i))
		time.sleep(1)