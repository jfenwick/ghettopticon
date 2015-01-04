import serial
import time

arduino = serial.Serial('/dev/tty.usbmodem14141',9600)

import struct

values = [255, 0, 180]
for i in values:
	arduino.write(struct.pack('>B', i))

time.sleep(1)

values = [255, 180, 0]
for i in values:
	arduino.write(struct.pack('>B', i))