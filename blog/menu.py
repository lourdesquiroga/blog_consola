# Menu e interaccion con el usuario

from blog.datos import estados_post


# Muestra el menu y retorna la opcion elegida
def mostrar_menu():
    print("--- MENU DEL BLOG ---")
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por tag")
    print("4. Crear nuevo post")
    print("5. Validar posts")
    print("6. Guardar posts en JSON")
    print("7. Salir")

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


# Pide un texto y no deja seguir hasta que no este vacio
def pedir_texto_obligatorio(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto == "":
            print("Este campo no puede quedar vacio. Intenta de nuevo.")
        else:
            return texto


# Pide los tags separados por coma y retorna una lista
def pedir_tags():
    while True:
        texto = input("Tags separados por coma (ej: Python, Web): ")
        tags = []
        for tag in texto.split(","):
            tag = tag.strip()
            if tag != "":
                tags.append(tag)
        if len(tags) == 0:
            print("Tenes que ingresar al menos un tag.")
        else:
            return tags


# Pide el estado y no deja seguir hasta que sea uno valido
def pedir_estado():
    while True:
        estado = input("Estado (borrador, publicado o archivado): ").strip().lower()
        if estado in estados_post:
            return estado
        print("Estado invalido. Tiene que ser borrador, publicado o archivado.")


# Pide todos los datos de un post nuevo y los retorna
def pedir_datos_post():
    titulo = pedir_texto_obligatorio("Titulo: ")
    contenido = pedir_texto_obligatorio("Contenido: ")
    tags = pedir_tags()
    estado = pedir_estado()
    return titulo, contenido, tags, estado