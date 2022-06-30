import mysql.connector
from mysql.connector import Error

conexion = mysql.connector.connect(
    user="root",
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
        
        """ cursor.execute("INSERT INTO libros (null,nombre,autor,fechaPublicacion) VALUES ")
        conexion.commit() #confirma la accion que ejecutamos
        print("registro insertado") """
except Error as ex:
    print("Error durante la conexion: ", ex)
finally:
    if conexion.is_connected():
        conexion.close() #siempre va el cierre de conexión
        print("La conexión terminó")


#primero hay que usar un cursor. objeto relacionado para lectura de datos e inserciones
#  