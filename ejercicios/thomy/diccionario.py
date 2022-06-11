
primerDiccionario = {"nombre": "Thomas", "apellido": "Gonzalez", "edad": 26, "localidad": "Villa Adelina"}
segundoDiccionario = {"nombre": "Alessandra", "apellido":"Godoy", "edad": 27, "localidad": "Villa Urquiza"}
tercerDiccionario = {"nombre": "Luana", "apellido":"Acosta", "edad": 20, "localidad": "Capital"}

print(primerDiccionario["nombre"])

for key in primerDiccionario:
    print (primerDiccionario[key])

print("----------")

for key in segundoDiccionario:
    print(segundoDiccionario[key])

print("----------")

for key in tercerDiccionario:
    print(tercerDiccionario[key])

print("----------")
def ponerNombre(dicc):
    arrNombres = []
    nombre = dicc["nombre"]    
    arrNombres.append(nombre)
    return arrNombres


nombre = ponerNombre(primerDiccionario)
nombre2 = ponerNombre(segundoDiccionario)


    


