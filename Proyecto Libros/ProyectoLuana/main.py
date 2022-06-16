global listaLibros
listaLibros= list()

#Objeto libro
class Libro:
    def __init__(self):
        titulo=""
        autor=""
        editorial=""
        isbn=""

#Metodo agregar libro a la lista
def agregarLibro():
    l=Libro()
    l.titulo=input("Ingrese el titulo: ")
    l.autor=input("Ingrese autor del libro: ")
    l.editorial=input("Ingrese editorial del libro: ")
    l.isbn=int(input("Ingrese el ISBN del libro: "))
    listaLibros.append(l)

#Metodo mostrar libros de la lista
def mostrarLibros():
    l=Libro()
    for l in listaLibros:
        print(l.titulo," ",l.autor," ", l.editorial," ", l.isbn) 

#Metodo para buscar libros
def buscarLibro():
    l=Libro()
    opLibro=int(input("1)Buscar por titulo 2)Buscar por ISBN"))
    if opLibro==1:
        tituloLibro=input("Ingrese el titulo del libro: ")
        for l in listaLibros:
            if l.titulo== tituloLibro:
                print(l.titulo," ",l.autor," ", l.editorial," ", l.isbn) 
    elif opLibro==2:
        isbnLibro=int(input("Ingrese el ISBN del libro"))
        for l in listaLibros:
            if l.isbn== isbnLibro:
               print(l.titulo," ",l.autor," ", l.editorial," ", l.isbn) 
    else:
        print("Ingrese un opcion correcta")

#Metodo para eliminar el libro
def eliminarLibro():
    l=Libro()
    libroEliminar=input("Ingrese el titulo del libro a eliminar")
    for l in listaLibros:
        if libroEliminar==l.titulo:
            listaLibros.remove(libroEliminar);
        else:
            print("El libro no existe")  

#Menu del programa
def menuLibros():
    op=0
    while(op!=4):
        op=int(input("1)Mostrar libros 2)Buscar libro 3)Agregar libro 4)Eliminar libro"))
        if op==1:
            mostrarLibros()
        elif op==2:
            buscarLibro()
        elif op==3:
            agregarLibro()
        elif op==4:
            eliminarLibro()
        else:
            print("Opcion erronea")
    
menuLibros()