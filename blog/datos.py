# Datos base del blog

perfil_autor = {
    "nombre": "Lourdes Quiroga",
    "bio": "Estudiante de desarrollo web y aprendiendo Python",
    "especialidad": "Python y desarrollo backend",
    "redes_sociales": ["@lou_dev", "@lourdes_python", "@lou_code"]
}
estados_post = ("borrador", "publicado", "archivado")
etiquetas_blog = {"Python", "Django", "Web", "Backend", "Python"}
posts = [
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
    {
        "id": 4,
        "titulo": "",
        "autor": perfil_autor,
        "tags": "Python",
        "estado": "pendiente"
    }
]
