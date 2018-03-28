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
