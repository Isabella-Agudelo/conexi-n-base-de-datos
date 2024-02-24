import tkinter as tk
from tkinter import ttk
import mysql.connector

def mostrar_contenido():
    # Conectarse a la base de datos
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

    # Limpiar la tabla antes de cargar los nuevos datos
    for row in tree.get_children():
        tree.delete(row)

    # Agregar los datos a las filas
    for resultado in resultados:
        tree.insert("", "end", values=resultado)

    # Cerrar el cursor y la conexión
    cursor.close()
    conexion.close()

ventana = tk.Tk()
ventana.title("Conexion DB")

# Crear el widget Treeview
tree = ttk.Treeview(ventana)

# Configurar las columnas
tree["columns"] = ("ID", "Nombre", "Teléfono")

# Definir los encabezados de las columnas
tree.heading("ID", text="ID")
tree.heading("Nombre", text="Nombre")
tree.heading("Teléfono", text="Teléfono")

# Empacar el widget Treeview
tree.pack(expand=False, fill="both")

# Agregar el botón de mostrar
boton_mostrar = tk.Button(ventana, text="Mostrar", command=mostrar_contenido)
boton_mostrar.pack()

ventana.mainloop()
