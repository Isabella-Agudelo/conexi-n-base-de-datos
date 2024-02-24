import mysql.connector


# Establecer la conexión

conexion = mysql.connector.connect(

    host="localhost",

    user="root",

    password="",

    database="escuela"

)


# Crear un objeto cursor para interactuar con la base de datos

cursor = conexion.cursor()

# Ejecutar una consulta

consulta = "SELECT * FROM estudiantes"

cursor.execute(consulta)

# Obtener los resultados

resultados = cursor.fetchall()

# Imprimir los resultados

print(resultados)

for resultado in resultados:

    print(resultado)


# Cerrar el cursor y la conexión


print("isable solo quiere a juan\n")
print(resultados[0])

cursor.close()

conexion.close()