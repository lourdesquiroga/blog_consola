# Blog por consola

## Qué hace el sistema

Es un blog que funciona desde la terminal. Permite ver los posts, buscarlos por título, filtrarlos por tag y validar que estén bien cargados.

## Cómo ejecutarlo

Abrir una terminal en la carpeta blog_consola y ejecutar:

    python main.py

## Qué contiene cada archivo

    main.py                 Archivo principal. Importa las funciones del paquete blog y maneja el menú.
    blog/__init__.py        Hace que la carpeta blog sea un paquete.
    blog/datos.py           Los datos del blog: perfil_autor, estados_post, etiquetas_blog y posts.
    blog/menu.py            Muestra el menú y pide los datos al usuario.
    blog/operaciones.py     Listar, buscar por título y filtrar por tag.
    blog/validaciones.py    Revisa que los posts tengan la estructura correcta.

## Funcionalidades del menú

1. Ver todos los posts: muestra título, autor y estado.
2. Buscar por titulo: muestra los posts que contienen la palabra buscada.
3. Filtrar por tag: muestra los posts que tienen ese tag.
4. Validar posts: indica qué posts son válidos y cuáles tienen errores.
5. Salir: cierra el programa.
