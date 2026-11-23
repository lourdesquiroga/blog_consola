# Funciones principales del blog


# Muestra el titulo, el autor y el estado de cada post de la lista
def listar_posts(lista):
    for post in lista:
        if "titulo" in post:
            titulo = post["titulo"]
        else:
            titulo = "(sin titulo)"

        if "autor" in post and "nombre" in post["autor"]:
            nombre = post["autor"]["nombre"]
        else:
            nombre = "(autor desconocido)"

        if "estado" in post:
            estado = post["estado"]
        else:
            estado = "(sin estado)"

        print(f"- {titulo} | Autor: {nombre} | Estado: {estado}")


# Retorna los posts cuyo titulo contiene el termino buscado
def buscar_por_titulo(lista, termino):
    resultados = []
    for post in lista:
        titulo = post.get("titulo", "")
        if termino.lower() in titulo.lower():
            resultados.append(post)
    return resultados


# Retorna los posts que tengan el tag indicado
def filtrar_por_tag(lista, tag):
    resultados = []
    for post in lista:
        tags = post.get("tags", [])
        if isinstance(tags, list):
            tags_minuscula = []
            for t in tags:
                tags_minuscula.append(t.lower())
            if tag.lower() in tags_minuscula:
                resultados.append(post)
    return resultados
