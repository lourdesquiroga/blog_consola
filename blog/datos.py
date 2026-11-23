# Datos base del blog y persistencia con JSON

import json

from blog.modelos import autor_desde_diccionario, post_desde_diccionario

ARCHIVO_POSTS = "posts.json"

perfil_autor = {
    "nombre": "Lourdes Quiroga",
    "bio": "Estudiante de desarrollo web y aprendiendo Python",
    "especialidad": "Python y desarrollo backend",
    "redes_sociales": ["@lou_dev", "@lourdes_python", "@lou_code"]
}
estados_post = ("borrador", "publicado", "archivado")
etiquetas_blog = {"Python", "Django", "Web", "Backend", "Python"}

# Posts que se usan si posts.json no existe o no se puede leer
posts_iniciales = [
    {
        "id": 1,
        "titulo": "Primeros pasos con Python",
        "contenido": "En este post veremos como empezar a programar con Python.",
        "autor": perfil_autor,
        "tags": ["Python", "Principiantes"],
        "estado": "publicado"
    },
    {
        "id": 2,
        "titulo": "Qué es Django",
        "contenido": "Django es un framework web creado con Python.",
        "autor": perfil_autor,
        "tags": ["Python", "Django", "Web"],
        "estado": "borrador"
    },
    {
        "id": 3,
        "titulo": "Organizando datos con diccionarios",
        "contenido": "Las listas permiten guardar varios elementos en una sola variable.",
        "autor": perfil_autor,
        "tags": ["Python", "Diccionarios"],
        "estado": "archivado"
    },
    # Post con errores a proposito, para probar las validaciones
    {
        "id": 4,
        "titulo": "",
        "contenido": "",
        "autor": perfil_autor,
        "tags": "Python",
        "estado": "pendiente"
    }
]


# Crea el objeto Autor principal del blog
def crear_autor_principal():
    return autor_desde_diccionario(perfil_autor)


# Convierte los posts iniciales (diccionarios) en objetos Post
def crear_posts_iniciales():
    posts = []
    for datos in posts_iniciales:
        posts.append(post_desde_diccionario(datos))
    return posts


# Lee posts.json y retorna una lista de objetos Post
def cargar_posts(ruta=ARCHIVO_POSTS):
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
    except FileNotFoundError:
        print(f"No se encontro el archivo {ruta}. Se cargan los posts iniciales.")
        return crear_posts_iniciales()

    if contenido.strip() == "":
        print(f"El archivo {ruta} esta vacio. Se cargan los posts iniciales.")
        return crear_posts_iniciales()

    try:
        lista = json.loads(contenido)
    except json.JSONDecodeError:
        print(f"El archivo {ruta} tiene contenido invalido. Se cargan los posts iniciales.")
        return crear_posts_iniciales()

    if not isinstance(lista, list):
        print(f"El archivo {ruta} no tiene una lista de posts. Se cargan los posts iniciales.")
        return crear_posts_iniciales()

    # Cada diccionario se convierte en un objeto Post
    posts = []
    for datos in lista:
        try:
            posts.append(post_desde_diccionario(datos))
        except ValueError as error:
            print(f"No se pudo cargar un post: {error}")

    print(f"Se cargaron {len(posts)} post(s) desde {ruta}.")
    return posts


# Guarda una lista de diccionarios en posts.json
def guardar_posts(lista_diccionarios, ruta=ARCHIVO_POSTS):
    # Primero se arma el texto JSON: si hay un objeto sin convertir, falla aca
    try:
        texto = json.dumps(lista_diccionarios, indent=4, ensure_ascii=False)
    except TypeError:
        print("Error: hay datos que no se pueden guardar en JSON. "
              "Los objetos tienen que convertirse a diccionario antes de guardarse.")
        return False

    try:
        with open(ruta, "w", encoding="utf-8") as archivo:
            archivo.write(texto)
    except OSError:
        print(f"Error: no se pudo escribir el archivo {ruta}.")
        return False

    print(f"Se guardaron {len(lista_diccionarios)} post(s) en {ruta}.")
    return True