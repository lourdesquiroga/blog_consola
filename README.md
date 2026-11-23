# Blog por consola

## Qué hace el sistema

Es un blog que funciona desde la terminal. Permite ver los posts, buscarlos por título, filtrarlos por tag, crear posts nuevos, validar que estén bien cargados y guardarlos en un archivo posts.json para que no se pierdan al cerrar el programa.

## Cómo ejecutarlo

Abrir una terminal en la carpeta blog_consola y ejecutar:

    python main.py

## Estructura del proyecto

    main.py                 Archivo principal. Carga los posts, crea el objeto Blog y maneja el menú.
    posts.json              Archivo donde se guardan los posts.
    blog/__init__.py        Hace que la carpeta blog sea un paquete.
    blog/modelos.py         Las clases Autor, Post y Blog.
    blog/datos.py           Los datos iniciales y las funciones para cargar y guardar posts.json.
    blog/menu.py            Muestra el menú y pide los datos al usuario.
    blog/validaciones.py    Revisa que los posts tengan datos correctos.

## Clases principales

Autor: representa a la persona que escribe. Guarda nombre, bio, especialidad y redes sociales.

Post: representa una publicación. Guarda id, título, contenido, tags, estado y un autor, que es un objeto de la clase Autor.

Blog: representa el blog completo. Tiene una lista de objetos Post y los métodos para trabajar con ella: listar, buscar por título, filtrar por tag, crear un post nuevo y convertir todos los posts a diccionarios.

## Cómo se guarda y se carga la información

JSON no puede guardar objetos de Python, así que se convierten a diccionarios:

- Para guardar: Autor y Post tienen el método a_diccionario(). Blog usa a_lista_diccionarios() para convertir todos los posts, y la función guardar_posts() de datos.py escribe esa lista en posts.json.
- Para cargar: al iniciar, cargar_posts() lee posts.json y convierte cada diccionario en un objeto Post (con su objeto Autor) usando post_desde_diccionario() y autor_desde_diccionario().

Si posts.json no existe, está vacío o tiene contenido inválido, el programa avisa y arranca con los posts iniciales. Si un post del archivo está incompleto, se avisa cuál es el problema y se carga el resto.

Los posts se guardan con la opción 6 del menú y también automáticamente al salir.

## Funcionalidades del menú

1. Ver todos los posts: muestra título, autor y estado.
2. Buscar por titulo: muestra los posts que contienen la palabra buscada.
3. Filtrar por tag: muestra los posts que tienen ese tag.
4. Crear nuevo post: pide título, contenido, tags y estado, y crea un objeto Post.
5. Validar posts: indica qué posts son válidos y cuáles tienen errores.
6. Guardar posts en JSON: guarda los posts en posts.json.
7. Salir: guarda los posts y cierra el programa.

La búsqueda y el filtro no distinguen mayúsculas de minúsculas.

## Qué cambió respecto a la entrega anterior

- Se agregó blog/modelos.py con las clases Autor, Post y Blog. Los posts ahora son objetos y no diccionarios.
- La lógica de listar, buscar y filtrar pasó de operaciones.py a métodos de la clase Blog, por eso se eliminó operaciones.py.
- datos.py ahora carga y guarda los posts en posts.json.
- El menú tiene dos opciones nuevas: crear post y guardar en JSON.
- main.py crea un objeto Blog y llama a sus métodos.