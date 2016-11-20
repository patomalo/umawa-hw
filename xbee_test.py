import serial

ser = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=3.0)
string = 'Hello from Raspberry Pi'
print 'Sending "%s"' % string
ser.write('%s\n' % string)

while True:
    incoming = ser.readline().strip()
    print 'Received %s' % incoming
    ser.write('RPi Received: %s\n' % incoming)
