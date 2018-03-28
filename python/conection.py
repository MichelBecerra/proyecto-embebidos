from firebase import firebase

# select/get
def selectContenedor(contenedor):
    fb = firebase.FirebaseApplication('https://demeter-siade.firebaseio.com/', None)
    contenedor2 = '/Sensores/' + contenedor
    result = fb.get(contenedor2, None)
    print(result)
    return result

# update/post
def updateCantidad(contenedor, cantidad):
    fb = firebase.FirebaseApplication('https://demeter-siade.firebaseio.com/', None)
    contenedor2 = '/Sensores/' + contenedor
    result = fb.put(contenedor2, 'cantidad', cantidad)
    print(result)
    return result
