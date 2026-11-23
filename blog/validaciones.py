# Reglas de validacion del blog

from blog.datos import estados_post
from blog.modelos import Autor, Post


# Revisa un objeto Post y retorna True o un mensaje de error
def validar_post(post):
    if not isinstance(post, Post):
        return "no es un objeto Post"
    if not isinstance(post.titulo, str) or post.titulo.strip() == "":
        return "el titulo esta vacio"
    if not isinstance(post.contenido, str) or post.contenido.strip() == "":
        return "el contenido esta vacio"
    if not isinstance(post.autor, Autor):
        return "el autor no es un objeto Autor"
    if not isinstance(post.autor.nombre, str) or post.autor.nombre.strip() == "":
        return "el autor no tiene nombre"
    if not isinstance(post.tags, list):
        return "los tags no son una lista"
    if post.estado not in estados_post:
        return f"el estado '{post.estado}' no es valido"
    return True


# Recorre la lista y muestra que posts son validos y cuales no
def validar_todos(lista):
    print("Validacion de posts:")
    for post in lista:
        resultado = validar_post(post)
        if resultado is True:
            print(f"Post {post.id}: valido")
        else:
            print(f"Post {post.id}: error - {resultado}")