from config_singleton import Configuracion

def mostrar_menu():
    config = Configuracion()
    while True:
        print("\n--- PANEL DE CONFIGURACIÓN ---")
        print("1. Ver configuración actual")
        print("2. Cambiar idioma")
        print("3. Cambiar tema (claro/oscuro)")
        print("4. Ajustar volumen")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            print("\nConfiguración actual:")
            for clave, valor in config.mostrar_todo().items():
                print(f"{clave.capitalize()}: {valor}")

        elif opcion == "2":
            nuevo_idioma = input("Nuevo idioma: ")
            config.set("idioma", nuevo_idioma)
            print("Idioma actualizado.")

        elif opcion == "3":
            nuevo_tema = input("Tema (claro/oscuro): ")
            if nuevo_tema in ["claro", "oscuro"]:
                config.set("tema", nuevo_tema)
                print("Tema actualizado.")
            else:
                print("Tema no válido.")

        elif opcion == "4":
            try:
                nuevo_volumen = int(input("Volumen (0 a 100): "))
                if 0 <= nuevo_volumen <= 100:
                    config.set("volumen", nuevo_volumen)
                    print("Volumen actualizado.")
                else:
                    print("Volumen fuera de rango.")
            except ValueError:
                print("Ingresa un número válido.")

        elif opcion == "5":
            print("Saliendo del panel de configuración...")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")
