#continuación de Adaptandome a la sintaxis de python

#pago=0
#while pago<5:
#    pago=pago+1
#    print("Pago:"+str(pago))

#input solo toma strings
entrada=int(input())
if(entrada==15):
    print("Bien")
else:
   print("Mal ingresado") 


fecha=input("Fecha en formato DDMMAAAA: ")
print("La fecha es: " + str(fecha[0])+str(fecha[1]+"/"+str(fecha[2])+str(fecha[3])))

#Escribí un programa que solicite al usuario el ingreso de un texto y almacene ese texto en una variable. A continuación, mostrar en pantalla la primera letra del texto ingresado.
 
#cuerpo
cadena1= input("Ingrese la cadena a evaluar:")
print("El primer dato del string es: " + str(cadena1[0]))
    
#Luego, solicitar al usuario que ingrese un número positivo menor a la cantidad de caracteres que tiene el texto que ingresó (por ejemplo, si escribió la palabra "HOLA", tendrá que ser un número entre 0 y 4) y almacenar este número en una variable llamada indice.

numero=int(input("Ingrese un numero menor a la cantidad de caracteres del texto"))
if numero>0 & numero<=len(cadena1) :
    indice=numero
else:
    print("Ese numero no va...")
print("El caracter en el indice indicado es: "+ cadena1[indice])