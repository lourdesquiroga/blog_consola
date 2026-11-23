# Reglas de validacion del blog

from blog.datos import estados_post


# Revisa la estructura de un post y retorna True o un mensaje de error
def validar_post(post):
    if not isinstance(post, dict):
        return "el post no es un diccionario"
    claves = ["id", "titulo", "contenido", "autor", "tags", "estado"]
    for clave in claves:
        if clave not in post:
            return f"falta la clave '{clave}'"
    if post["titulo"] == "":
        return "el titulo esta vacio"
    if post["contenido"] == "":
        return "el contenido esta vacio"
    if not isinstance(post["autor"], dict):
        return "el autor no es un diccionario"
    if "nombre" not in post["autor"]:
        return "el autor no tiene la clave 'nombre'"
    if not isinstance(post["tags"], list):
        return "los tags no son una lista"
    if post["estado"] not in estados_post:
        return f"el estado '{post['estado']}' no es valido"
    return True


# Recorre la lista y muestra que posts son validos y cuales no
def validar_todos(lista):
    print("Validacion de posts:")
    for post in lista:
        numero = post.get("id", "?")
        resultado = validar_post(post)
        if resultado is True:
            print(f"Post {numero}: valido")
        else:
            print(f"Post {numero}: error - {resultado}")
