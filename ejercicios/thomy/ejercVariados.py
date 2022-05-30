""" 1. Escribí un programa que solicite al usuario que ingrese su nombre. El nombre se debe almacenar en una variable llamada nombre. A continuación se debe mostrar en pantalla el texto “Ahora estás en la matrix, [usuario]”, donde “[usuario]” se reemplazará por el nombre que el usuario haya ingresado. """

""" def saludo():
    hola= input("Hola, como te llamas? ")
    print ("Ahora estas en la matrix, " ,hola.capitalize(),"." )
saludo() """


""" 2. Escribí un programa que solicite al usuario ingresar un número con decimales y almacenalo en una variable. A continuación, el programa debe solicitar al usuario que ingrese un número entero y guardarlo en otra variable. En una tercera variable se deberá guardar el resultado de la suma de los dos números ingresados por el usuario. Por último, se debe mostrar en pantalla el texto “El resultado de la suma es [suma]”, donde “[suma]” se reemplazará por el resultado de la operación. """


""" decimal = float(input("Ingrese un numero decimal: "))
entero = int(input("Ingrese un número entero: "))
suma = float(decimal + entero)
print(f"La suma de {decimal} mas {entero} es {suma}.") """


""" 3. Escribí un programa que solicite al usuario dos números y los almacene en dos variables. En otra variable, almacená el resultado de la suma de esos dos números y luego mostrá ese resultado en pantalla.
A continuación, el programa debe solicitar al usuario que ingrese un tercer número, el cual se debe almacenar en una nueva variable. Por último, mostrá en pantalla el resultado de la multiplicación de este nuevo número por el resultado de la suma anterior. """

""" def sumaYMultiplicacion():
    num1 = int(input("Ingrese un número: "))
    num2 = int(input("Ingrese otro número: "))
    suma= num1 + num2
    print(suma)
    multi= int(input("Ingrese un número para multiplicar: "))
    multiplicado = suma * multi
    print(f"La suma de los primeros dos números, multiplicado por el tercero es: {multiplicado} .")

sumaYMultiplicacion() """


""" 4 . Escribí un programa que solicite al usuario ingresar la cantidad de kilómetros recorridos por una motocicleta y la cantidad de litros de combustible que consumió durante ese recorrido. Mostrar el consumo de combustible por kilómetro. """

""" def viaje():
    kilometros = int(input("Ingrese la cantidad de KM recorridos"))
    nafta = float(input("Ingrese la cantidad de litros de gasolina"))
    naftaxkm = kilometros/nafta
    print(f"La cantidad de nafta por KM es de : {naftaxkm}.")

viaje() """

""" 5 . 
Escribí un programa que solicite al usuario un número y le reste el 15%, almacenando todo en una única variable. A continuación, mostrar el resultado final en pantalla. """

""" def menos15():
    numero = int((input("Ingrese un número: ")))
    print( "el 15% del número que ingresaste es: " ,numero*0.15)

menos15() """



""" 6. Escribí un programa que solicite al usuario el ingreso de dos palabras, las cuales se guardarán en dos variables distintas. A continuación, almacená en una variable la concatenación de la primera palabra, más un espacio, más la segunda palabra. Mostrá este resultado en pantalla. """

""" def unirPalabras():
    palabra1 = input("Ingrese una palabra: ")
    palabra2 = input("Ingrese otra palabra: ")
    print(palabra1.capitalize() + " " + palabra2)

unirPalabras()
 """
""" 7. Escribí un programa que solicite al usuario el ingreso de un texto y almacene ese texto en una variable. A continuación, mostrar en pantalla la primera letra del texto ingresado. Luego, solicitar al usuario que ingrese un número positivo menor a la cantidad de caracteres que tiene el texto que ingresó (por ejemplo, si escribió la palabra “HOLA”, tendrá que ser un número entre 0 y 4) y almacenar este número en una variable llamada indice.
Mostrar en pantalla el carácter del texto ubicado en la posición dada por indice. """
""" 
texto = input("Ingresá un texto: ")
print("La primera letra de tu texto es: ", texto[0].upper())

numero= int(input("Seleccione un numero: "))
if numero > 0 and numero < len(texto):
    print("El caracter del texto que ingresaste en la posición del número que ingresaste es: ", texto[numero])
else:
    print("Ingresa un número entre 0 y ", len(texto)) """


""" 8. Escribí un programa que solicite al usuario que ingrese cuántos shows musicales ha visto en el último año y almacene ese número en una variable. A continuación mostrar en pantalla un valor de verdad (True o False) que indique si el usuario ha visto más de 3 sh"""

""" cantidadShows = int(input("A cuantos recitales fuiste este año? "))
if cantidadShows >=3:
    print(True)
else: print(False) """


""" 9. Escribí un programa para solicitar al usuario el ingreso de un número entero y que luego imprima un valor de verdad dependiendo de si el número es par o no. Recordar que un número es par si el resto, al dividirlo por 2, es 0. """


""" def numeroPar(num):
    if num % 2 == 0:
        print(num, "Es par")
    else:
        print("Ingrese un número par")

numeroPar(5) """

""" 10 .Escribí un programa que le solicite al usuario su edad y la guarde en una variable. Que luego solicite la cantidad de artículos comprados en una tienda y la guarde en otra variable. Finalmente, mostrar en pantalla un valor de verdad (True o False) que indique si el usuario es mayor de 18 años de edad y además compró más de 1 artículo. """

""" def tienda():
    edad = int(input("Ingrese su edad "))
    articulos = int(input("Ingrese la cantidad de artículos que compró: "))
    if edad >= 18 and articulos>=1:
        print(True)
    else: print(False)

tienda() """


""" 11 .Escribí un programa que, dada una cadena de texto por el usuario, imprima True si la cantidad de caracteres en la cadena es un número impar, o False si no lo es. """

""" textito = input("Ingrese un texto: ")
if len(textito)%2==0:
    print(True)
else: print(False) """


""" 12. Escribí un programa que le pida al usuario ingresar dos palabras y las guarde en dos variables, y que luego imprima True si la primera palabra es menor que la segunda o False si no lo es. """

""" def dosPalabras(): 
    palabra1 = input("Ingrese la primera palabra ")
    palabra2 = input("Ingrese otra palabra ")
    if len(palabra1) > len (palabra2):
        print(True)
    else: print(False)

dosPalabras() """


""" Escribí un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje “Es vocal”. Verificar si el usuario ingresó un string de más de un carácter y, en ese caso, informarle que no se puede procesar el dato. """

""" 
def esVocal():
    letra = input("Ingrese una letra: ")
   
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        print("La letra que elegiste", letra , "es vocal")

    else: print("La letra que elegiste NO es vocal")

esVocal() """