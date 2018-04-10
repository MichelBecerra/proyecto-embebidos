from firebase import firebase

# select/get
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

#from firebase import firebase
#from firebase_admin import db
#import threading
#import time

#class Conection(threading.Thread):
#    def __init__(self, cb):
#        threading.Thread.__init__(self)
#        self.callback = cb
#        self.fire = firebase.FirebaseApplication('https://demeter-siade.firebaseio.com/', None)

#ref = db.reference('Sensores/contenedorCuatro')
#users_ref = ref.child('')

#import pyrebase
#config = {
#  "apiKey": "AIzaSyDheOhXfu5CKMWiRMhrmjVWYfGKA7C0ves",
#  "authDomain": "demeter.firebaseapp.com",
#  "databaseURL": "demeter-siade.firebaseapp.com",
#  "storageBucket": "demeter-siade.appspot.com"
  #"serviceAccount": "path/to/serviceAccountCredentials.json"
#}

#firebase = pyrebase.initialize_app(config)

#auth = firebase.auth()
#authenticate a user
#user = auth.sign_in_with_email_and_password("alan061997@gmail.com", "Alan4Ever")
#demeter-siade.child("Sensores").child("contenedorDos").update({"cantidad": "2"}, user['idToken'])
