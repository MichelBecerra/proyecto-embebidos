# coding=utf-8
import time
import serial
import serial.tools.list_ports as listPorts
from firebase import firebase
import smtplib

BAUD = 9600
TIMEOUT = 1

USUARIO_GMAIL = 'alan061997@gmail.com'
CONTRASENA_GMAIL = 'Alan4Ever'

DESTINATARIO = 'alan.darksunset@gmail.com'
REMITENTE = 'alan061997@gmail.com'

ASUNTO	= ""
MENSAJE = ""

cycle_counter = 0

class Sensor():
    def __init__(self, *args, **kwargs):
        '''Init sensor'''
        self.serial = None

    def port_names(self):
        '''Return portname'''
        pnames = []
        for port in listPorts.comports():
            if "ttyAMA" in port[0]:
                continue
            else:
                pnames.append(port[0])
        return pnames[0]

    def init_sensor(self):
        '''Create serial'''
        self.serial = serial.Serial(self.port_names(), BAUD, timeout= TIMEOUT)

    def read_data(self):
        '''Read data from sensors
        data[0] --> sensor 1
        data[1] --> sensor 2
        data[2] --> sensor 3'''
        data = ''
        while(self.serial.inWaiting() > 0):
            data = self.serial.readline().decode('utf-8').strip()
        data = self.serial.readline().decode('utf-8').strip()

        data_1 = 26 - float(data.split(' ')[0])
        data_2 = 26 - float(data.split(' ')[1])
        data_3 = 26 - float(data.split(' ')[2])

        return data_1, data_2, data_3


def selectContenedor(contenedor):
    fb = firebase.FirebaseApplication('https://demeter-siade.firebaseio.com/', None)
    address = '/Sensores/' + contenedor
    result = fb.get(address, None)
    print(result)
    return result

# update/post
def updateCantidad(contenedor, cantidad):
    fb = firebase.FirebaseApplication('https://demeter-siade.firebaseio.com/', None)
    address = '/Sensores/' + contenedor
    result = fb.put(address, 'cantidad', cantidad)
    print(result)
    return result

def selectConfig(contenedor):
    fb = firebase.FirebaseApplication('https://demeter-siade.firebaseio.com/', None)
    address = '/Config/' + contenedor
    record = fb.get(address, None)
    diametro = record["diametro"]
    return diametro

def enviar_correo_electronico():
	print("Enviando e-mail")
	smtpserver = smtplib.SMTP("smtp.gmail.com",587)
	smtpserver.ehlo()
	smtpserver.starttls()
	smtpserver.ehlo()
	smtpserver.login(USUARIO_GMAIL, CONTRASENA_GMAIL)
	header	= 'To:		' + DESTINATARIO + '\n'
	header += 'From:	' + REMITENTE	 + '\n'
	header += 'Subject: ' + ASUNTO		 + '\n'
	print (header)
	msg = header + '\n' + MENSAJE + ' \n\n'
	smtpserver.sendmail(REMITENTE, DESTINATARIO, msg)
	smtpserver.close()

def main():
    global cycle_counter
    global ASUNTO
    global MENSAJE
    srl = Sensor()
    srl.init_sensor()
    print ("Leyendo datos ...")
    time.sleep(3)
    while True:
        time.sleep(2)
        data_1, data_2, data_3 = srl.read_data()

        config1 = float(selectConfig("contenedorUno"))
        config2 = float(selectConfig("contenedorDos"))
        config3 = float(selectConfig("contenedorTres"))

        cantidad_1 = abs(round(data_1/config1))
        cantidad_2 = abs(round(data_2/config2))
        cantidad_3 = abs(round(data_3/config3))

        print ("Distance 1: {}\nDistance 2: {}\nDistance 3: {}\n\n".format(cantidad_1, cantidad_2, cantidad_3))

        updateCantidad("contenedorUno", cantidad_1)
        updateCantidad("contenedorDos", cantidad_2)
        updateCantidad("contenedorTres", cantidad_3)
        print("\n\n")

        if cycle_counter == 0 and (( (cantidad_1 <= 1) or (cantidad_2 <= 1) ) or (cantidad_3 <= 1)):
            ASUNTO = ' El '
            if cantidad_1 <= 1:
                ASUNTO	+= " | producto 1 | "
                MENSAJE = " El producto 1 esta por agotarse/esta agotado.\n "
            if cantidad_2 <= 1:
                ASUNTO	+= " | producto 2 | "
                MENSAJE = ' El producto 2 esta por agotarse/esta agotado.\n "
            if cantidad_3 <= 1:
                ASUNTO	+= " | producto 3 | "
                MENSAJE =  " El producto 3 esta por agotarse/esta agotado.\n "
            ASUNTO +=  " esta por agotarse/ esta agotado. "
            enviar_correo_electronico()
            print("\n\n")
            time.sleep(3)

        if cycle_counter > 10:
            cycle_counter = 0
        else:
            cycle_counter += 1



if __name__ == '__main__':
    main()
