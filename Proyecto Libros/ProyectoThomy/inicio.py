

global libross
libross = ("id_lib","nombre_lib","autor_lib","fechaPub_lib")

class Biblioteca:
    def __init__(self):
        pass        
    def presentacion(self,libreria_nom=""):
        self.libreria = libreria_nom = input("Nombre de la libreria? ")
        return libreria_nom
    
    def retorno_nombre(self, libreria_nom):

        print("Bienvenido a la libreria ", Biblioteca.presentacion()) 
    
    def agregar_libro(self,nombre,autor,fecha):
        self.nombre = nombre = input("Cual es el nombre del libro que desea ingresar? ")
        self.autor= input("Ingrese autor")
        self.fecha = input("Fecha de publicación: YYYY/MES/DIA")
        libross.append([nombre,autor,fecha]) #as fechaPub_lib como que se guarde ahi)

    def consultar_libro(self, id):
        self.id = id
        print(libross.id, libross.nombre)

    def quitar_libro(self, id):
        libross.pop(id)        
    
    def menu(self):
        eleccion=0
        while eleccion!=5:
            eleccion = input("Seleccione la opción que quiere ingresar: 1-Nombre biblioteca, 2-Agregar libros a la biblioteca, 3-Consultar los libros disponibles, 4- Eliminar libro existente, 5-Cerrar programa")
            if eleccion =="1":
                Biblioteca.retorno_nombre
            elif eleccion =="2":
                Biblioteca.agregar_libro
            elif eleccion=="3":
                #llamar a los libros 
                print(libross.id,"-",libross.nombre, "-", libross.autor, "-",libross.fechaPub)
            elif eleccion=="4":
                #sacar por id o nombre de la biblioteca, que formato ??
                Biblioteca.quitar_libro
            elif eleccion =="5":
                print("Hasta luego ! ")
                break
        

    """   def libros(self,):
        self.nombre_libro = nombre_lib
        self.autor_lib = autor_lib
        self.fechaPub = fechaPub_lib """
    
biblioteca = Biblioteca()
biblioteca.presentacion()


biblioteca.menu()




        



    
    


    






 