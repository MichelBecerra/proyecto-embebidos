from firebase import firebase
from firebase_admin import db
import threading
import time

class Conection(threading.Thread):
    def __init__(self, cb):
        threading.Thread.__init__(self)
        self.callback = cb
        self.fire = firebase.FirebaseApplication('https://demeter-siade.firebaseio.com/', None)

ref = db.reference('Sensores/contenedorCuatro')
users_ref = ref.child('')