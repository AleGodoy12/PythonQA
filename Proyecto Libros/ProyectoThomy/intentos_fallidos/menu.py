from io import open

if __name__ == "__menu__":
    print('Bienvenido a la Libreria ')


class Libreria:
    def __init__(self):
        pass
    
    class Libro:
        def __init__(self,nombre,autor,fecha_publicacion):
            self.nombre = nombre
            self.autor = autor
            self.fecha_publicacion = fecha_publicacion

    def agregar_libro(nombre,autor,fecha_publicacion):
        agregar = open (A = 'libros.json')
        print(agregar)
        print()

    def borrar_libro():
        print()

         







