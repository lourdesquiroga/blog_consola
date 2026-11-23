# Clases principales del blog: Autor, Post y Blog


# Representa a una persona autora del blog
class Autor:
    def __init__(self, nombre, bio, especialidad="", redes_sociales=None):
        self.nombre = nombre
        self.bio = bio
        self.especialidad = especialidad
        if redes_sociales is None:
            redes_sociales = []
        self.redes_sociales = redes_sociales

    # Convierte el autor en un diccionario para poder guardarlo en JSON
    def a_diccionario(self):
        return {
            "nombre": self.nombre,
            "bio": self.bio,
            "especialidad": self.especialidad,
            "redes_sociales": self.redes_sociales
        }


# Representa una publicacion del blog. El autor es un objeto Autor
class Post:
    def __init__(self, id, titulo, contenido, autor, tags, estado):
        self.id = id
        self.titulo = titulo
        self.contenido = contenido
        self.autor = autor
        self.tags = tags
        self.estado = estado

    # Convierte el post en un diccionario (el autor tambien se convierte)
    def a_diccionario(self):
        if isinstance(self.autor, Autor):
            autor = self.autor.a_diccionario()
        else:
            autor = self.autor
        return {
            "id": self.id,
            "titulo": self.titulo,
            "contenido": self.contenido,
            "autor": autor,
            "tags": self.tags,
            "estado": self.estado
        }


# Representa el blog completo: guarda la lista de posts y la maneja
class Blog:
    def __init__(self, posts=None):
        if posts is None:
            posts = []
        self.posts = posts

    # Retorna todos los posts cargados
    def obtener_posts(self):
        return self.posts

    # Muestra titulo, autor y estado de cada post (por defecto, todos)
    def listar_posts(self, lista=None):
        if lista is None:
            lista = self.posts
        for post in lista:
            print(f"- {post.titulo} | Autor: {post.autor.nombre} | Estado: {post.estado}")

    # Retorna los posts cuyo titulo contiene el termino buscado
    def buscar_por_titulo(self, termino):
        resultados = []
        for post in self.posts:
            if termino.lower() in post.titulo.lower():
                resultados.append(post)
        return resultados

    # Retorna los posts que tengan el tag indicado
    def filtrar_por_tag(self, tag):
        resultados = []
        for post in self.posts:
            if isinstance(post.tags, list):
                tags_minuscula = []
                for t in post.tags:
                    tags_minuscula.append(t.lower())
                if tag.lower() in tags_minuscula:
                    resultados.append(post)
        return resultados

    # Calcula el id del proximo post (el mayor id + 1)
    def siguiente_id(self):
        mayor = 0
        for post in self.posts:
            if isinstance(post.id, int) and post.id > mayor:
                mayor = post.id
        return mayor + 1

    # Agrega un objeto Post a la lista del blog
    def agregar_post(self, post):
        self.posts.append(post)

    # Crea un objeto Post nuevo, lo agrega al blog y lo retorna
    def crear_post(self, titulo, contenido, autor, tags, estado):
        post = Post(self.siguiente_id(), titulo, contenido, autor, tags, estado)
        self.agregar_post(post)
        return post

    # Convierte todos los posts en una lista de diccionarios
    def a_lista_diccionarios(self):
        lista = []
        for post in self.posts:
            lista.append(post.a_diccionario())
        return lista


# Crea un objeto Autor a partir de un diccionario
def autor_desde_diccionario(datos):
    if not isinstance(datos, dict):
        raise ValueError("el autor no es un diccionario")
    for clave in ["nombre", "bio"]:
        if clave not in datos:
            raise ValueError(f"al autor le falta la clave '{clave}'")
    return Autor(
        datos["nombre"],
        datos["bio"],
        datos.get("especialidad", ""),
        datos.get("redes_sociales", [])
    )


# Crea un objeto Post a partir de un diccionario
def post_desde_diccionario(datos):
    if not isinstance(datos, dict):
        raise ValueError("el post no es un diccionario")
    claves = ["id", "titulo", "contenido", "autor", "tags", "estado"]
    for clave in claves:
        if clave not in datos:
            raise ValueError(f"al post le falta la clave '{clave}'")
    autor = autor_desde_diccionario(datos["autor"])
    return Post(
        datos["id"],
        datos["titulo"],
        datos["contenido"],
        autor,
        datos["tags"],
        datos["estado"]
    )