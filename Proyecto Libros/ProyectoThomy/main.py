import json

def mostrar_libros():
    with open ('libros.json',"r") as libros:
        dif_libros = json.load(libros)
        for libr in dif_libros:             
            print(libr, '\n')
        opciones_bib()

def agregar_libro():
    libro = {}
    nombre = input('Ingrese el título a registrar: ')
    autor = input('Ingrese el nombre del autor: ')
    fecha_publicacion = input('Ingrese la fecha de publicación del libro: ')
    libro['nombre'] = nombre
    libro['autor'] = autor
    libro['fecha_publicacion'] = fecha_publicacion
    with open('libros.json','w'):
        json.dumps(libro)
        print('Libro agregado con exito !')
        print(libro)
    opciones_bib()
def retirarse():
    print('----------------')
    print("Gracias por la visita, vuelva pronto ! ")  
    print('----------------')  
    
def opciones_bib():
    opciones = 0
    while (opciones <5):
        opt = input('Que desea hacer? \n 1- Agregar un libro a la biblioteca \n 2- Consultar los libros disponibles. \n 3- Retirarse ? \n')
        if opt == '1':
            agregar_libro()
        if opt == '2':
            mostrar_libros()
        if opt == '3':
            retirarse()
        else:
            print('Gracias')

opciones_bib()

if __name__ == '__main__':
    print('Bienvenido a la libreria ! ')
    