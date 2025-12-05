listaEstudiantes = []
def agregar_estudiante():
    print("\nAgregar estudiante")
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = int(input("Ingrese la edad del estudiante: "))
    promedio = float(input("Ingrese su promedio de notas: "))
    listaEstudiantes.append({"nombre": nombre, "edad": edad, "promedio":promedio})
def mostrar_estudiantes():
    if is_lista_vacia(): return
    print("\nLista de estudiantes")
    for e in listaEstudiantes:
        print("-",e["nombre"])
def mostrar_estudiante_mejor_promedio():
    if is_lista_vacia(): return
    mayor = -1
    estudiante = None
    for i in range(len(listaEstudiantes)):
        if listaEstudiantes[i]["promedio"] > mayor:
            mayor = listaEstudiantes[i]["promedio"]
            estudiante = listaEstudiantes[i]
    print("\nEl estudiante con mejor promedio es:")
    print("-",estudiante["nombre"],".Promedio =",estudiante["promedio"])
def mostrar_buscando_nombre():
    if is_lista_vacia(): return
    print()
    busqueda = input("Ingrese el nombre del estudiante a buscar: ")
    for e in listaEstudiantes:
        if (e["nombre"] == busqueda):
            print("Estudiante encontrado.")
            print(f"-{e["nombre"].upper()}")
            print(f"Edad: {e["edad"]}")
            print(f"Promedio: {e["promedio"]}")
            break
    else:
        print("No se logro encontrar dicho estudiante.")
def eliminar_estudiante_nombre():
    if is_lista_vacia(): return
    print()
    busqueda = input("Ingrese el nombre del estudiante a eliminar: ")
    for i in range(len(listaEstudiantes)):
        if (listaEstudiantes[i]["nombre"] == busqueda):
            listaEstudiantes.pop(i)
            print("Se logro eliminar satisfactoriamente.")
            return
def is_lista_vacia():
    if (len(listaEstudiantes) == 0):
        print("Por favor ingresar un alumno antes de realizar esta accion.")
        return True
    return False
print("Bienvenido al registro de estudiantes.")
while True:
    print("Ingrese una opcion: ")
    print("1. Agregar estudiante.")
    print("2. Mostrar estudiantes.")
    print("3. Mostrar estudiante con mejor promedio.")
    print("4. Buscar por nombre.")
    print("5. Eliminar por nombre.")
    print("0. Salir.")
    eleccion = input()
    match eleccion:
        case "1":
            agregar_estudiante()
        case "2":
            mostrar_estudiantes()
        case "3":
            mostrar_estudiante_mejor_promedio()
        case "4":
            mostrar_buscando_nombre()
        case "5":
            eliminar_estudiante_nombre()
        case "0":
            print("Gracias por usar este registro.")
            break
        case _:
            print("Opcion no valida. Por favor volver a ingresar.")
