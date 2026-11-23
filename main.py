# Archivo principal del blog por consola

from blog.datos import cargar_posts, guardar_posts, crear_autor_principal
from blog.menu import mostrar_menu, pedir_texto, pedir_datos_post
from blog.modelos import Blog
from blog.validaciones import validar_todos


# Bloque principal
if __name__ == "__main__":
    # Se cargan los posts desde posts.json y se crea el objeto Blog
    posts = cargar_posts()
    blog = Blog(posts)
    autor = crear_autor_principal()

    while True:
        opcion = mostrar_menu()
        if opcion is None:
            continue

        if opcion == 1:
            print("Posts disponibles:")
            if len(blog.obtener_posts()) == 0:
                print("No hay posts cargados.")
            else:
                blog.listar_posts()

        elif opcion == 2:
            termino = pedir_texto("Buscar por titulo: ")
            if termino == "":
                print("No ingresaste ninguna palabra.")
            else:
                resultados = blog.buscar_por_titulo(termino)
                if len(resultados) > 0:
                    print(f"Se encontraron {len(resultados)} post(s):")
                    blog.listar_posts(resultados)
                else:
                    print("No se encontraron posts con esa palabra.")

        elif opcion == 3:
            tag = pedir_texto("Filtrar por tag: ")
            if tag == "":
                print("No ingresaste ningun tag.")
            else:
                resultados = blog.filtrar_por_tag(tag)
                if len(resultados) > 0:
                    print(f"Posts con el tag {tag} ({len(resultados)} encontrados):")
                    blog.listar_posts(resultados)
                else:
                    print("No se encontraron posts con ese tag.")

        elif opcion == 4:
            titulo, contenido, tags, estado = pedir_datos_post()
            post = blog.crear_post(titulo, contenido, autor, tags, estado)
            print(f"Post creado con id {post.id}. Se guarda con la opcion 6 o al salir.")

        elif opcion == 5:
            validar_todos(blog.obtener_posts())

        elif opcion == 6:
            guardar_posts(blog.a_lista_diccionarios())

        elif opcion == 7:
            guardar_posts(blog.a_lista_diccionarios())
            print("Gracias por usar el sistema del blog. Hasta luego!")
            break

        else:
            print("Opcion invalida, intenta de nuevo")