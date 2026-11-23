# Archivo principal del blog por consola

from blog.datos import posts
from blog.menu import mostrar_menu, pedir_texto
from blog.operaciones import listar_posts, buscar_por_titulo, filtrar_por_tag
from blog.validaciones import validar_todos


# Bloque principal
if __name__ == "__main__":
    while True:
        opcion = mostrar_menu()
        if opcion is None:
            continue

        if opcion == 1:
            print("Posts disponibles:")
            listar_posts(posts)

        elif opcion == 2:
            termino = pedir_texto("Buscar por titulo: ")
            if termino == "":
                print("No ingresaste ninguna palabra.")
            else:
                resultados = buscar_por_titulo(posts, termino)
                if len(resultados) > 0:
                    print(f"Se encontraron {len(resultados)} post(s):")
                    listar_posts(resultados)
                else:
                    print("No se encontraron posts con esa palabra.")

        elif opcion == 3:
            tag = pedir_texto("Filtrar por tag: ")
            if tag == "":
                print("No ingresaste ningun tag.")
            else:
                resultados = filtrar_por_tag(posts, tag)
                if len(resultados) > 0:
                    print(f"Posts con el tag {tag} ({len(resultados)} encontrados):")
                    listar_posts(resultados)
                else:
                    print("No se encontraron posts con ese tag.")

        elif opcion == 4:
            validar_todos(posts)

        elif opcion == 5:
            print("Gracias por usar el sistema del blog. Hasta luego!")
            break

        else:
            print("Opcion invalida, intenta de nuevo")
