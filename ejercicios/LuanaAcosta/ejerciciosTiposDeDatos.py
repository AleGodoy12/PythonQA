#Declara una variable por cada tipo de dato (numerico, cadena de texto, booleano)

#numero
numerito=3
print(type(numerito))
#string
cadenita="Cadenita"
print(type(cadenita))
#booleano
bulean=True 
#los buleanos van con mayuscula en la primera
print(type(bulean))

#Ejercicios 2
#Realiza una suma, una resta y una multiplicacion con dos variables numericas
numerito1=2
numerito2=3
sumaDeNumeritos=numerito1+numerito2
multiplicacionDeNumeritos=numerito1*numerito2
print(sumaDeNumeritos,multiplicacionDeNumeritos)

#Ejercicio 3
#Realiza una concatenacion de dos variables, la primera con un valor "Hola" y la segunda con valor "numero"
cadenita1="Blue"
cadenita2="flame"
laCadenaFinal=cadenita1+cadenita2
print(laCadenaFinal)

#Ejercicios 23/5/2022
arreglo2=[numerito1,numerito2,cadenita1,cadenita2]
print(arreglo2)

arreglo2.insert(3, "Vladi")
print(arreglo2)

arreglo2.append("Blue")
print(arreglo2)

print(arreglo2.count("2022"))

arreglo2.remove("Vladi")
#elimina la primera coincidencia
print(arreglo2)

