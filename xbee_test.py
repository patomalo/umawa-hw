import serial

ser = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=3.0)

ser.open()
string = 'Hello from Raspberry Pi'
print 'INIT MESSAGE: "%s"' % string
ser.open()
# ser.write('%s\n' % string)
try:
   while True:
       incoming = ser.readline().strip()
       if len(incoming)>0:
           print 'Received %s' % incoming
       else:
           print 'Nothing received'
except:
    ser.close()


