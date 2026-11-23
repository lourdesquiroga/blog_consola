# Menu e interaccion con el usuario


# Muestra el menu y retorna la opcion elegida
def mostrar_menu():
    print("--- MENU DEL BLOG ---")
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por tag")
    print("4. Validar posts")
    print("5. Salir")

    try:
        opcion = int(input("Ingresar opcion: "))
        return opcion
    except ValueError:
        print("Error: tenes que ingresar un numero.")
        return None


# Pide un texto al usuario y lo retorna
def pedir_texto(mensaje):
    texto = input(mensaje)
    return texto
