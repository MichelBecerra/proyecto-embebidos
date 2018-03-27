import serial
import serial.tools.list_ports as listPorts
BAUD = 9600
TIMEOUT = 1

class Sensor():
    def __init__(self, *args, **kwargs):
        '''Init sensor'''
        self.serial = ''

    def port_names(self):
        '''Return portname'''
        pnames = []
        for port in listPorts.comports():
            if "ttyAMA" in port[0]:
                continue
            else:
                pnames.append(port[0])
        return pnames

    def init_sensor(self):
        '''Create serial'''
        self.serial = serial.Serial(self.port_names(self), BAUD, TIMEOUT)

    def read_data(self):
        '''Read data from sensors
        data[0] --> sensor 1
        data[1] --> sensor 2
        data[2] --> sensor 3'''
        data = ''
        while(self.serial.inWaiting() > 0):
            data = self.srl.readline().decode('utf-8')
        data = self.srl.readline().decode('utf-8')
        print(data)
        data_1 = data.split(' ')[0]
        data_2 = data.split(' ')[1]
        data_3 = data.split(' ')[2]
        return data_1, data_2, data_3

def main():
    srl = Sensor()
    srl.init_sensor()
    while True:
        data_1, data_2, data_3 = srl.read_data()
        print ("Distance 1: {}\nDistance 2: {}\nDistance 3: {}\n\n").format(data_1, data_2, data_3)
    pass

if __name__ == '__main__':
    main()