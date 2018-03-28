from firebase import firebase

# select/get
def selectContenedor(contenedor):
    firebase = firebase.FirebaseApplication('https://demeter-siade.firebaseio.com/', None)
    contenedor2 = '/Sensores/' + contenedor
    result = firebase.get(contenedor2, None)
    print(result)
    return result

# update/post
def updateCantidad(contenedor, cantidad):
    firebase = firebase.FirebaseApplication('https://demeter-siade.firebaseio.com/', None)
    contenedor2 = '/Sensores/' + contenedor
    result = firebase.put(contenedor2, 'cantidad', cantidad)
    print(result)
    return result
