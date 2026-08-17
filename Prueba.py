import mysql.connector
contador = 0

def visualizar_datos():
    cnx = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Cdttm01*",
        database="estudiantes"
    )
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM Estudiantes")
    for fila in cursor.fetchall():
        print(fila)
    cnx.close()


def agregar_datos():
    Name = input("Digite el nombre de la persona: ").capitalize()
    Apellido = input("Digite el apellido de la persona: ").capitalize()
    Fecha_nacimiento = input("Digite la fecha de nacimiento (YYYY-MM-DD): ")
    Profesion = input("Digite la profesión: ").capitalize()

    cnx = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Cdttm01*",
        database="estudiantes"
    )
    cursor = cnx.cursor()

    sql = "INSERT INTO Estudiantes (name, apellido, fecha_nacimiento, profesion) VALUES (%s, %s, %s, %s)"
    valores = (Name, Apellido, Fecha_nacimiento, Profesion)

    cursor.execute(sql, valores)
    cnx.commit()
    print("Registro insertado correctamente.")

    cursor.execute("SELECT * FROM Estudiantes")
    for fila in cursor.fetchall():
        print(fila)

    cnx.close()


def eliminar_datos():
    id_eliminar = int(input("Digite el id del valor a eliminar: "))
    cnx = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Cdttm01*",
        database="estudiantes"
    )
    cursor = cnx.cursor()
    sql = "DELETE FROM Estudiantes WHERE id = %s"
    cursor.execute(sql, (id_eliminar,))
    cnx.commit()
    print("Registro eliminado correctamente.")
    cnx.close()

def cerrar_programa():
    global contador
    print("Programa cerrado.")
    contador = 1

# 👉 Menú interactivo
menu = {
    1: visualizar_datos,
    2: agregar_datos,
    3: eliminar_datos,
    4: cerrar_programa
}
while contador == 0:
    print("------------------------------")
    print("Digite 1 para visualizar datos")
    print("Digite 2 para agregar datos")
    print("Digite 3 para eliminar datos")
    print("Digite 4 para cancelar el programa")
    print("------------------------------")

    opcion = int(input("Seleccione una opción: "))
    if opcion in menu:
        menu[opcion]()
    else:
        print("Opción inválida, Por favor selecciones una opción válida.")
