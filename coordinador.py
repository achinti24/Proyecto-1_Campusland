import json

ARCHIVO_TRAINERS = "TRAINERS.json"
ARCHIVO_CAMPERS = "campers.json"

def crud_trainers():

    try:
        with open(ARCHIVO_TRAINERS, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
    except:
        datos = []

    opcion = ""

    while opcion != "5":

        print("====== CRUD TRAINERS ======")
        print("1. Crear trainer")
        print("2. Mostrar trainers")
        print("3. Actualizar trainer")
        print("4. Eliminar trainer")
        print("5. Volver")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            nombre = input("Nombre del trainer: ")
            horario = input("Horario: ")
            rutas = input("Rutas (separadas por coma): ").split(",")

            nuevo = {
                "nombre": nombre,
                "horario": horario,
                "rutas": [r.strip() for r in rutas]
            }

            datos.append(nuevo)

            with open(ARCHIVO_TRAINERS, "w", encoding="utf-8") as archivo:
                json.dump(datos, archivo, indent=4, ensure_ascii=False)

            print("Trainer creado correctamente")
        elif opcion == "2":
            if not datos:
                print("No hay trainers registrados")
            else:
                for t in datos:
                    print(t)
        elif opcion == "3":
            nombre_buscar = input("Nombre del trainer a actualizar: ").lower()

            encontrado = False

            for t in datos:
                if t["nombre"].lower() == nombre_buscar:
                    encontrado = True
                    print("Trainer encontrado")

                    while True:
                        print(f"¿Qué desea actualizar de {t['nombre']}?")
                        print("1. Cambiar nombre")
                        print("2. Cambiar horario")
                        print("3. Cambiar rutas")
                        print("4. Salir")

                        opcion = input("Seleccione una opción: ")

                        if opcion == "1":
                            t["nombre"] = input("Nuevo nombre: ")

                        elif opcion == "2":
                            t["horario"] = input("Nuevo horario: ")

                        elif opcion == "3":
                            nuevas_rutas = input("Nuevas rutas (separadas por coma): ")
                            t["rutas"] = [r.strip() for r in nuevas_rutas.split(",")]

                        elif opcion == "4":
                            print("Saliendo de edición...")
                            break

                        else:
                            print("Opción no válida")
                            continue
                        with open(ARCHIVO_TRAINERS, "w", encoding="utf-8") as archivo:
                            json.dump(datos, archivo, indent=4, ensure_ascii=False)

                        print("Trainer actualizado correctamente")

                    break

            if not encontrado:
                print("Trainer no encontrado")

        elif opcion == "4":
            nombre_eliminar = input("Nombre del trainer a eliminar: ").lower()

            nuevos = [t for t in datos if t["nombre"].lower() != nombre_eliminar]

            if len(nuevos) == len(datos):
                print("Trainer no encontrado")
            else:
                datos = nuevos
                with open(ARCHIVO_TRAINERS, "w", encoding="utf-8") as archivo:
                    json.dump(datos, archivo, indent=4, ensure_ascii=False)

                print("Trainer eliminado correctamente")
def crud_campers():

    try:
        with open(ARCHIVO_CAMPERS, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
    except:
        datos = {"campers": []}

    opcion = ""

    while opcion != "4":

        print("====== CRUD CAMPERS ======")
        print("1. Mostrar campers")
        print("2. Actualizar camper")
        print("3. Eliminar camper")
        print("4. Volver")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            if not datos["campers"]:
                print("No hay campers registrados")
            else:
                for c in datos["campers"]:
                    print(c)
        elif opcion == "2":
            id_buscar = input("ID del camper a actualizar: ")

            encontrado = False

            for c in datos["campers"]:
                if c["id"] == id_buscar:
                    encontrado = True
                    print("Camper encontrado")

                    while True:
                        print(f"\n¿QUÉ DESEA ACTUALIZAR DE {c['nombre']}?")
                        print("1. Cambiar nombre y apellido")
                        print("2. Cambiar dirección")
                        print("3. Cambiar acudiente")
                        print("4. Cambiar número telefónico")
                        print("5. Cambiar estado")
                        print("6. Cambiar riesgo")
                        print("7. Salir")

                        opcion = input("Seleccione una opción: ")

                        if opcion == "1":
                            c["nombre"] = input("Nuevo nombre: ")
                            c["apellidos"] = input("Nuevos apellidos: ")

                        elif opcion == "2":
                            c["direccion"] = input("Nueva dirección: ")

                        elif opcion == "3":
                            c["acudiente"] = input("Nuevo acudiente: ")

                        elif opcion == "4":
                            c["telefono"] = input("Nuevo teléfono: ")

                        elif opcion == "5":
                            c["estado"] = input("Nuevo estado: ")

                        elif opcion == "6":
                            c["riesgo"] = input("Nuevo riesgo: ")

                        elif opcion == "7":
                            print("Saliendo de edición...")
                            break

                        else:
                            print("Opción no válida")
                            continue
                        with open(ARCHIVO_CAMPERS, "w", encoding="utf-8") as archivo:
                            json.dump(datos, archivo, indent=4, ensure_ascii=False)

                        print("Camper actualizado correctamente")

                    break

            if not encontrado:
                print("Camper no encontrado")
        elif opcion == "3":
            id_eliminar = input("ID del camper a eliminar: ")

            nuevos = [c for c in datos["campers"] if c["id"] != id_eliminar]

            if len(nuevos) == len(datos["campers"]):
                print("Camper no encontrado")
            else:
                datos["campers"] = nuevos

                with open(ARCHIVO_CAMPERS, "w", encoding="utf-8") as archivo:
                    json.dump(datos, archivo, indent=4, ensure_ascii=False)

                print("Camper eliminado correctamente")
