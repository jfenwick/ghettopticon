import serial
import time

arduino = serial.Serial('/dev/tty.usbmodem14131',9600)
#time.sleep(3)

import struct
valueToWrite = 0
arduino.write(struct.pack('>B', valueToWrite))
arduino.write(struct.pack('>B', valueToWrite))
arduino.write(struct.pack('>B', valueToWrite))

time.sleep(3)

valueToWrite = 180
arduino.write(struct.pack('>B', valueToWrite))
arduino.write(struct.pack('>B', valueToWrite))
arduino.write(struct.pack('>B', valueToWrite))


#arduino.write(b'1')
#arduino.close()