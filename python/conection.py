from firebase import firebase
fb = firebase.FirebaseApplication('https://demeter-siade.firebaseio.com/', None)
# select/get
result = fb.get('/Sensores/contenedorDos', None)
print(result)
# update/post
contenedor1 = 'contenedorTres'
contenedor2 = '/Sensores/' + contenedor1
print (contenedor2)
result2 = fb.put(contenedor2, 'cantidad', 7)
print(result2)

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
