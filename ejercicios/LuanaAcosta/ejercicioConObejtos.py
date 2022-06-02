class Alumno:
    #el método init sirve para definir los atributos del objeto
    def __init__(self):
        self.nombre=input("Ingrese su nombre:")
        self.grado=int(input("Ingrese el año en el que está"))
        self.materias=input("Ingrese SI si debe materias y NO si no las debe").upper()
        self.imprimir()
        self.debeMaterias()


    def imprimir(self):
        print("Nombre del alumno: ", self.nombre)
        print("Grado: ", self.grado)

    def debeMaterias(self):
        if self.materias=="SI":
            print("Definitivamente debe materias")
        else:
            print("No las debe")
#finaliza la clase


# para indicar q una clase es una subclase de "class Curso(Alumno):" heredar

  
 

nuevoAlumno=Alumno()
