import mysql.connector
from mysql.connector import Error
import inicio


conexion = mysql.connector.connect(
    user="root",
    password="",
    port="3306",
    database="biblioteca" )
print(conexion)

try:
    conexion = mysql.connector.connect(
        host = "localhost",
        port= 3306,
        user = "root",
        password = "",
        db="biblioteca"
    )
    if conexion.is_connected():
        print("Conexion exitosa")
        infoServer = conexion.get_server_info()
        print("Info del servidor: ", infoServer)
        cursor = conexion.cursor()
        cursor.execute("SELECT database();")
        registro = cursor.fetchone() #obtiene un unico registro, ir a buscar y devolver un registro
        print("conectado a la base de base: ", registro)
        cursor.execute("SELECT * FROM libros") #ejecuta la consulta sql
        resultados = cursor.fetchall()
        for filas in resultados:
            print(filas[0],filas[1],filas[2],filas[3])
        
        def agregar_un_libro():
            nombre = input("Ingrese el nombre del libro a registrar: ")
            autor = input("Ingrese el nombre del autor: ")
            fecha_publicacion = input("Ingrese la fecha de publicacion(formato año-mes-dia): ")
            agregar_libro = "INSERT INTO libros (nombre,autor,fecha_publicacion) VALUES ('{1},{2}')".format(nombre,autor,fecha_publicacion)
            cursor.execute(agregar_libro)
            conexion.commit() #confirma la accion que ejecutamos
            print("registro insertado")


except Error as ex:
    print("Error durante la conexion: ", ex)
finally:
    if conexion.is_connected():
        conexion.close() #siempre va el cierre de conexión
        print("La conexión terminó")
agregar_un_libro()

#primero hay que usar un cursor. objeto relacionado para lectura de datos e inserciones
#  