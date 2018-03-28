from firebase import firebase

class Connections():
    def __init__(self):
        #vacio

    # select/get
    def selectContenedor(self, contenedor):
        firebase = firebase.FirebaseApplication('https://demeter-siade.firebaseio.com/', None)
        contenedor2 = '/Sensores/' + contenedor
        result = firebase.get(contenedor2, None)
        print(result)
        return result

    # update/post
    def updateCantidad(self, contenedor, cantidad):
        firebase = firebase.FirebaseApplication('https://demeter-siade.firebaseio.com/', None)
        contenedor2 = '/Sensores/' + contenedor
        result = firebase.put(contenedor2, 'cantidad', cantidad)
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
