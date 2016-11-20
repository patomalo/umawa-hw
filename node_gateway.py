import serial
import requests
import time
import file_utils as utils



def to_real_sensor(values):
    master_id = values[0]
    slave_id = values[1]
    flux = 0.12 * int(values[2])
    light = 0.12 * int(values[0])  # not used?
    env_humidity = 0.12 * int(values[0])
    acum = 0
    for v in values[3:]:
        acum = int(v) + acum
    size = 1.0 * len(values[3:])
    soil_humidity = acum / size
    return [master_id, slave_id, light, env_humidity, flux, soil_humidity]


def build_json(sensors):
    string_sensors = [str(s) for s in sensors]
    print string_sensors
    json = '{ "slaveId":' + string_sensors[0] + ',' + \
           ' "masterId":' + string_sensors[1] + ',' + \
           ' "timestamp":' + str(long(time.time())) + ',' + \
           ' "light":' + string_sensors[2] + ',' + \
           ' "humiditySensorRate":' + string_sensors[3] + ',' + \
           ' "pressionSensorRate":' + string_sensors[4] + ',' + \
           ' "soilHumidityRate":' + string_sensors[5] + '}'

    return json


def init_xbee():
    ser = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=3.0)
    ser.open()
    string = 'Hello from Raspberry Pi'
    print 'INIT MESSAGE: "%s"' % string
    ser.open()
    return ser


def read_xbee(serial):
    try:
        incoming = serial.readline().strip()
        if len(incoming) > 0:
            print 'Received %s' % incoming
        else:
            print 'Nothing received'
    except:
        serial.close()

    return incoming


if __name__ == "__main__":
    msg = "aa123,1231,14,413,122,311,1,12,3,23,123,1,bb"
    host = "192.168.3.110"
    port = '3000'
    end_point = "event"
    a = 1
    url = 'http://' + host + ':' + port + '/' + end_point
    print url
    serial_interface = init_xbee()
    while a == 1:
        msg = read_xbee(serial_interface)
        msg1 = utils.find_between(msg, 'aa','bb')
        print 'parsed  ' + str(msg1)
        try:
            sensors = to_real_sensor(msg1.split(",")[:-1])
        except:
            print 'invalid message  ' + str(msg1)
            time.sleep(1)
            continue

        print sensors
        json = build_json(sensors)
        print json
        # headers = {'content-type': 'application/json'}
        headers = {'Connection ': 'keep-alive',
                   'Content-Length': '170',
                   'Content-Type': 'application/json',
                   'Date ': 'Sun, 20 Nov 2016 11:47:35 GMT',
                   'Location ': '/event/58318d57e80de94fc4888a93',
                   }
        r = requests.post(url, data=json, headers=headers)
        print r.status_code
        print r.text
        time.sleep(1)
