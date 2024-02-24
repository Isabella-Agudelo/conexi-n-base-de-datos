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

def eliminar_seleccionado():
    # Obtener el elemento seleccionado en el Treeview
    selected_item = tree.selection()

    if selected_item:  # Si hay un elemento seleccionado
        # Eliminar el elemento seleccionado
        tree.delete(selected_item)   

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

# tree.pack(expand=True, fill="both") asegura que el widget tree se expanda tanto horizontal como verticalmente para ocupar todo el espacio disponible dentro de la ventana principal ventana
tree.pack(expand=True, fill="both")

# Agregar el botón de mostrar
boton_mostrar = tk.Button(ventana, text="Mostrar", command=mostrar_contenido)
boton_mostrar.pack()

boton_eliminar = tk.Button(ventana, text="Eliminar", command=eliminar_seleccionado)
boton_eliminar.pack()

ventana.mainloop()
