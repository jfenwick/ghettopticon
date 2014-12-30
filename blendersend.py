valueToWrite = 255
arduino.write(struct.pack('>B', valueToWrite))

rot = int(degrees(bones['upperarm'].rotation_axis_angle[0]))
rot
arduino.write(struct.pack('>B', rot))

rot = int(degrees(bones['forearm'].rotation_axis_angle[0]))
rot
arduino.write(struct.pack('>B', rot))

rot = int(degrees(bones['control'].rotation_axis_angle[0]))
rot
arduino.write(struct.pack('>B', rot))