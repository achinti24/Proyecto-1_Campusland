import json

with open("TRAINERS.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)

def crear_trainer():
    import json

ARCHIVO = "TRAINERS.JSON"

def crear_trainer():
    
    with open(ARCHIVO, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)


    nombre = input("Nombre del trainer: ")
    horario = input("Horario: ")
    rutas = input("Rutas (separadas por coma): ").split(",")

    
    nuevo_trainer = {
        "nombre": nombre,
        "horario": horario,
        "rutas": [r.strip() for r in rutas]
    }

    
    datos["profesores"].append(nuevo_trainer)

    # Guardar cambios
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

    print("Trainer creado correctamente")

def mostrar_trainers():
    
    with open(ARCHIVO, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

    trainers = datos["profesores"] 

    if not trainers:
        print("No hay trainers disponibles")
        return

    print("=== TRAINERS DISPONIBLES ===")
    for t in trainers:
        print(f"Nombre: {t['nombre']}")
        print(f"Horario: {t['horario']}")
        print(f"Rutas: {', '.join(t['rutas'])}")
        print("----------------------------")

def actualizar_trainer():
    # Leer JSON
    with open(ARCHIVO, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

    trainers = datos["profesores"]  
    nombre_buscar = input("Nombre del trainer a actualizar: ").lower()

    for t in trainers:
        if t["nombre"].lower() == nombre_buscar:
            print("Trainer encontrado")

            nuevo_horario = input("Nuevo horario: ")
            nuevas_rutas = input("Nuevas rutas (separadas por coma): ").split(",")

            t["horario"] = nuevo_horario
            t["rutas"] = [r.strip() for r in nuevas_rutas]

            with open(ARCHIVO, "w", encoding="utf-8") as archivo:
                json.dump(datos, archivo, indent=4, ensure_ascii=False)

            print("Trainer actualizado correctamente")
            return

    print("Trainer no encontrado")
  

def eliminar_trainer():
    
    with open(ARCHIVO, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

    trainers = datos["profesores"] 
    nombre_eliminar = input("Nombre del trainer a eliminar: ").lower()

    
    nuevos_trainers = [
        t for t in trainers
        if t["nombre"].lower() != nombre_eliminar
    ]

    if len(nuevos_trainers) == len(trainers):
        print("Trainer no encontrado")
        return

    datos["profesores"] = nuevos_trainers

    # Guardar cambios
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

    print("Trainer eliminado correctamente")        

opcion = ""

while opcion != "5":
        print("\n====== MENÚ TRAINERS ======")
        print("1. Crear trainer")
        print("2. Mostrar trainers")
        print("3. Actualizar trainer")
        print("4. Eliminar trainer")
        print("5. Salir")
        print("===========================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_trainer()
        elif opcion == "2":
            mostrar_trainers()
        elif opcion == "3":
            actualizar_trainer()
        elif opcion == "4":
            eliminar_trainer()
        elif opcion == "5":
            print(" Saliendo del sistema..")
        else:
            print("Opción inválida")

    