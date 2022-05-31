generoMusica = ["rock", "rap", "melodico", "rap conciencia", "reggae"]
generoMusica.append("pop")
print(len(generoMusica))
print(generoMusica.count("pop"))
print(generoMusica.index("melodico"))
generoMusica.pop()
print(generoMusica)
generoMusica.reverse()
print(generoMusica)
generoMusica.sort()
print(generoMusica)
generoMusica.insert(2,"americano")
generoMusica.sort()
print(generoMusica)
print(generoMusica.pop())

print(generoMusica)

print(generoMusica[4])

#tuplas

caracteristicas_celu = ("Camara 100px", "154cm x 15cm", "Pantalla tactil")
print(caracteristicas_celu)

direcciones = "Pedernera 1010", "Cespedes 1515", "Perito Moreno"
print(direcciones)

#diccionario
libros = {"Harry Potte": "La piedra Filosofal", "Harry Potter": "La camara de los secretos", "Harry Pott": "El prisionero de Azkaban"}
print(libros["Harry Potter"]) 



print(libros)


texto = "Acá estamos practicando Phyton"
print(texto.split(" "))
print(texto.upper())
print(texto.lower())
print(texto.capitalize())

num1 = 550
num2 = 350
num3 = 1000

print(max(num1,num2,num3))

""" print(elMayor(5,10)) """



""" print(mayorDeTres(3,10,63)) """

temperaturaCen = 35
temperaturaSur = 12
temperaturaNor = 28
#Funciones:
def tiempo(temp):
    if temp<12:
        print("Hace frio")
    elif temp >12 and temp <24:
        print("Está templado")
    elif temp>24 and temp<40:
        print("Hace mucho calor, hidratate")
    else:
        print("Probablemente te mueras de calor :c")

tiempo() 

def elMayor (a, b):
    return max(a,b)

def mayorDeTres(a, b, c):
    return max(a,b,c)




