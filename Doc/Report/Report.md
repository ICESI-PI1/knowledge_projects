# Informe del segundo Sprint


* Jhonatan Castaño
* Juan David Bahamon
* Samuel Hernandez
* David Peñaranda
* Cristian Perafan


 # 1. **Páginas web. (Capturas pantallas)**

## Paginas web admin:

**Tablero**

[![Tablero.jpg](https://i.postimg.cc/GpN6PN2p/Tablero.jpg)](https://postimg.cc/xkvsn6Lr)

**Categorías**

 [![Categorias.jpg](https://i.postimg.cc/nV10pgJQ/Categorias.jpg)](https://postimg.cc/Dm8qcCm2)
 
 **Estados**
 
 [![Estados.jpg](https://i.postimg.cc/TY4jPXHh/Estados.jpg)](https://postimg.cc/dLGZWgFK)
 
 **Proyectos**
 
 [![Proyectos.jpg](https://i.postimg.cc/V6f0R7H3/Proyectos.jpg)](https://postimg.cc/WDy4p7Vn)
 
 ## Paginas web cliente:
 
 **Galería**
 
 [![imagen-2023-05-12-234307317.png](https://i.postimg.cc/vTzpFmQP/imagen-2023-05-12-234307317.png)](https://postimg.cc/0Kzt7PKm)
 
 **Categoría**
 
 [![Categorias-Cliente.jpg](https://i.postimg.cc/WbTpJDCH/Categorias-Cliente.jpg)](https://postimg.cc/Dmp39z2r)
 
 **Inicio**
 
 [![Home.png](https://i.postimg.cc/QxyPZwQJ/Home.png)](https://postimg.cc/0b7ZptHz)
 
 [![inicio.png](https://i.postimg.cc/2jH9nMKN/inicio.png)](https://postimg.cc/6TvhXjKM)
 
 **Login**
 
 [![Login.png](https://i.postimg.cc/PqhQgQRM/Login.png)](https://postimg.cc/tsS6PWy1)
 
 **Registro**
 
 [![imagen-2023-05-12-232914967.png](https://i.postimg.cc/pXfZqS0d/imagen-2023-05-12-232914967.png)](https://postimg.cc/GHpGpXn0)
 
 **Proyecto**
 
 [![imagen-2023-05-12-235112803.png](https://i.postimg.cc/SRksqV9m/imagen-2023-05-12-235112803.png)](https://postimg.cc/34f7FX9q)
 
 **Información detallada del proyecto**
 
 [![imagen-2023-05-12-233950592.png](https://i.postimg.cc/8CmcYh2M/imagen-2023-05-12-233950592.png)](https://postimg.cc/p9yPhnXL)
 
 **Realizar donación **
 
 [![imagen-2023-05-12-234053570.png](https://i.postimg.cc/bYWy3CZ4/imagen-2023-05-12-234053570.png)](https://postimg.cc/dDRc09m9)
 
 **Donación exitosa**
 
 [![imagen-2023-05-12-234146748.png](https://i.postimg.cc/4xBNbJVQ/imagen-2023-05-12-234146748.png)](https://postimg.cc/684XBxH8)
 
 

## Enlace al figma: 


https://www.figma.com/file/FpqRJSp3uekyJLl5tLrSY6/Knowledge-Project?node-id=0-1&t=Ya69SOgKgMTTVEKJ-0


# 2. **Incorporación pruebas unitarias y de integración.**


* Python manage.py test

[![test.png](https://i.postimg.cc/Dfdt9SDn/test.png)](https://postimg.cc/5jy7v2bR)


* Para los coverage test, primero se realizó el comando python -m coverage run manage.py y luego python -m coverage report

[![coverage.png](https://i.postimg.cc/d0M0WWD5/coverage.png)](https://postimg.cc/DSgF0PrG)

* Base de datos alterna

Para realizar pruebas automáticas utilizando una base de datos alterna debemos en settings.py utilizar las siguientes lineas de codigo:

[![imagen-2023-05-12-235303915.png](https://i.postimg.cc/CLd08WSW/imagen-2023-05-12-235303915.png)](https://postimg.cc/vcRCF21z)

Tambien podemos especificar una base de datos para las pruebas, por ejemplo: 

[![imagen-2023-05-12-235350441.png](https://i.postimg.cc/L4QKmNLv/imagen-2023-05-12-235350441.png)](https://postimg.cc/vDnSz7P6)

y luego:

[![imagen-2023-05-12-235515159.png](https://i.postimg.cc/9FPkrbqv/imagen-2023-05-12-235515159.png)](https://postimg.cc/xcC5ZK5R)

De esta forma, al utilizar *manage.py test* los test haran uso de la base de datos **’test’**.
Django admite varios motores de base de datos, como PostgreSQL, MySQL, SQLite, etc. 
La línea 'ENGINE': 'django.db.backends.postgresql' es donde se especifica el motor de base de datos que se utilizará.

https://docs.djangoproject.com/en/4.2/ref/settings/

# 3.**Dailys**

## Enlace al jira: 


https://mastersofsoftware.atlassian.net/jira/software/projects/KP/boards/3/backlog


### Juan David Bahamon


| Fecha         | ¿Qué hice ayer para avanzar en el proyecto?                                                                                                  | ¿Qué voy a hacer hoy para avanzar en el proyecto?                                                                                                                                                                 | ¿Hay algún impedimento que me esté impidiendo avanzar en el proyecto? |   |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|---|
| Fecha         | ¿Qué hice ayer para avanzar en el proyecto?                                                                                                  | ¿Qué voy a hacer hoy para avanzar en el proyecto?                                                                                                                                                                 | ¿Hay algún impedimento que me esté impidiendo avanzar en el proyecto? |   |
| 26/marzo/2023 | Realicé una investigación sobre los diferentes métodos de pago y las mejores prácticas de diseño web para crear una página de pago efectiva. | Comenzaré a crear el bosquejo de la página de pago y la página de notificación de transacción exitosa.                                                                                                            | No tengo impedimentos por el momento.                                 |   |
| 2/abril/2023  | Comencé a crear el bosquejo de la página de pago y la página de notificación de transacción exitosa.                                         | Empezaré a trabajar en la estructura HTML de la página de pago.                                                                                                                                                   | No tengo impedimentos por el momento.                                 |   |
| 15/marzo/2023 | Ayer continué investigando sobre modelado de datos. Sobre la definición de los atributos y las relaciones y cardinalidad.                    | Hoy me enfocaré en practicar la creación de diagramas de clases utilizando la herramienta de software visual paradigm. Buscaré tutoriales sobre el uso de UML y cómo aplicarlo para representar modelos de datos. | No tengo impedimentos por el momento.                                 |   |
| 9/abril/2023  | Empecé a trabajar en la estructura HTML de la página de pago.                                                                                | Continuaré trabajando en la estructura HTML de la página de pago y agregar el formulario de pago y los diferentes campos necesarios.                                                                              | No tengo impedimentos por el momento.                                 |   |
| 16/abril/2023 | Continué trabajando en la estructura HTML de la página de pago y agregué el formulario de pago y los diferentes campos necesarios.           | Investigaré sobre la validación de los datos ingresados en el formulario de pago.                                                                                                                                 | No tengo impedimentos por el momento.                                 |   |
| 23/abril/2023 | Trabajé en la validación de los datos ingresados en el formulario de pago.                                                                   | Continuaré trabajando en el diseño CSS de la página de pago.                                                                                                                                                      | No tengo impedimentos por el momento.                                 |   |
| 30/abril/2023 |  Continué trabajando en el diseño CSS de la página de pago.                                                                                  | Agregar animaciones CSS a los botones para mejorar la experiencia del usuario. .                                                                                                                                  | No tengo impedimentos por el momento.                                 |   |
| 5/mayo/2023   | Agregué animaciones CSS a los botones para mejorar la experiencia del usuario en la página de pago.                                          | Crearé la página de notificación de transacción exitosa.                                                                                                                                                          | No tengo impedimentos por el momento.                                 |   |
| 6/mayo/2023   | Ayer revisé el diagrama de clases y aún faltaban agregar algunos métodos, realicé la corrección.                                             | Hoy revisaré de nuevo el modelado de datos, en caso de existir algún error corregirlo.                                                                                                                            | No tengo impedimentos por el momento.                                 |   |
| 7/mayo/2023   | Trabajé en la estructura HTML de la página de notificación.                                                                                  | Trabajaré en el diseño CSS de la página de notificación. Realizaré ajustes finales de código innecesario del CSS.                                                                                                 | Hubo problemas con las imágenes de la página.                         |   |


### Jhonatan Castaño


| Fecha         | ¿Qué hice ayer para avanzar en el proyecto?                                                                                                  | ¿Qué voy a hacer hoy para avanzar en el proyecto?                                                                                                                                                                 | ¿Hay algún impedimento que me esté impidiendo avanzar en el proyecto? |   |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|---|
| Fecha         | ¿Qué hice ayer para avanzar en el proyecto?                                                                                                  | ¿Qué voy a hacer hoy para avanzar en el proyecto?                                                                                                                                                                 | ¿Hay algún impedimento que me esté impidiendo avanzar en el proyecto? |   |
| 26/marzo/2023 | Realicé una investigación sobre los diferentes métodos de pago y las mejores prácticas de diseño web para crear una página de pago efectiva. | Comenzaré a crear el bosquejo de la página de pago y la página de notificación de transacción exitosa.                                                                                                            | No tengo impedimentos por el momento.                                 |   |
| 2/abril/2023  | Comencé a crear el bosquejo de la página de pago y la página de notificación de transacción exitosa.                                         | Empezaré a trabajar en la estructura HTML de la página de pago.                                                                                                                                                   | No tengo impedimentos por el momento.                                 |   |
| 15/marzo/2023 | Ayer continué investigando sobre modelado de datos. Sobre la definición de los atributos y las relaciones y cardinalidad.                    | Hoy me enfocaré en practicar la creación de diagramas de clases utilizando la herramienta de software visual paradigm. Buscaré tutoriales sobre el uso de UML y cómo aplicarlo para representar modelos de datos. | No tengo impedimentos por el momento.                                 |   |
| 9/abril/2023  | Empecé a trabajar en la estructura HTML de la página de pago.                                                                                | Continuaré trabajando en la estructura HTML de la página de pago y agregar el formulario de pago y los diferentes campos necesarios.                                                                              | No tengo impedimentos por el momento.                                 |   |
| 16/abril/2023 | Continué trabajando en la estructura HTML de la página de pago y agregué el formulario de pago y los diferentes campos necesarios.           | Investigaré sobre la validación de los datos ingresados en el formulario de pago.                                                                                                                                 | No tengo impedimentos por el momento.                                 |   |
| 23/abril/2023 | Trabajé en la validación de los datos ingresados en el formulario de pago.                                                                   | Continuaré trabajando en el diseño CSS de la página de pago.                                                                                                                                                      | No tengo impedimentos por el momento.                                 |   |
| 30/abril/2023 | Continué trabajando en el diseño CSS de la página de pago.                                                                                   | Agregar animaciones CSS a los botones para mejorar la experiencia del usuario. .                                                                                                                                  | No tengo impedimentos por el momento.                                 |   |
| 5/mayo/2023   | Agregué animaciones CSS a los botones para mejorar la experiencia del usuario en la página de pago.                                          | Crearé la página de notificación de transacción exitosa.                                                                                                                                                          | No tengo impedimentos por el momento.                                 |   |
| 6/mayo/2023   | Ayer revisé el diagrama de clases y aún faltaban agregar algunos métodos, realicé la corrección.                                             | Hoy revisaré de nuevo el modelado de datos, en caso de existir algún error corregirlo.                                                                                                                            | No tengo impedimentos por el momento.                                 |   |
| 7/mayo/2023   | Trabajé en la estructura HTML de la página de notificación.                                                                                  | Trabajaré en el diseño CSS de la página de notificación. Realizaré ajustes finales de código innecesario del CSS.                                                                                                 | Hubo problemas con las imágenes de la página.                         |   |






### Cristian Felipe Perafan Chilito



| Fecha         | ¿Qué hice ayer para avanzar en el proyecto?                                                                                                  | ¿Qué voy a hacer hoy para avanzar en el proyecto?                                                                                                                                                                 | ¿Hay algún impedimento que me esté impidiendo avanzar en el proyecto? |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| 26/marzo/2023 | Realicé una investigación sobre los diferentes métodos de pago y las mejores prácticas de diseño web para crear una página de pago efectiva. | Comenzaré a crear el bosquejo de la página de pago y la página de notificación de transacción exitosa.                                                                                                            | No tengo impedimentos por el momento.                                 |
| 2/abril/2023  | Comencé a crear el bosquejo de la página de pago y la página de notificación de transacción exitosa.                                         | Empezaré a trabajar en la estructura HTML de la página de pago.                                                                                                                                                   | No tengo impedimentos por el momento.                                 |
| 15/marzo/2023 | Ayer continué investigando sobre modelado de datos. Sobre la definición de los atributos y las relaciones y cardinalidad.                    | Hoy me enfocaré en practicar la creación de diagramas de clases utilizando la herramienta de software visual paradigm. Buscaré tutoriales sobre el uso de UML y cómo aplicarlo para representar modelos de datos. | No tengo impedimentos por el momento.                                 |
| 9/abril/2023  | Empecé a trabajar en la estructura HTML de la página de pago.                                                                                | Continuaré trabajando en la estructura HTML de la página de pago y agregar el formulario de pago y los diferentes campos necesarios.                                                                              | No tengo impedimentos por el momento.                                 |
| 16/abril/2023 | Continué trabajando en la estructura HTML de la página de pago y agregué el formulario de pago y los diferentes campos necesarios.           | Investigaré sobre la validación de los datos ingresados en el formulario de pago.                                                                                                                                 | No tengo impedimentos por el momento.                                 |
| 23/abril/2023 | Trabajé en la validación de los datos ingresados en el formulario de pago.                                                                   | Continuaré trabajando en el diseño CSS de la página de pago.                                                                                                                                                      | No tengo impedimentos por el momento.                                 |
| 30/abril/2023 |  Continué trabajando en el diseño CSS de la página de pago.                                                                                  | Agregar animaciones CSS a los botones para mejorar la experiencia del usuario. .                                                                                                                                  | No tengo impedimentos por el momento.                                 |
| 5/mayo/2023   | Agregué animaciones CSS a los botones para mejorar la experiencia del usuario en la página de pago.                                          | Crearé la página de notificación de transacción exitosa.                                                                                                                                                          | No tengo impedimentos por el momento.                                 |
| 6/mayo/2023   | Ayer revisé el diagrama de clases y aún faltaban agregar algunos métodos, realicé la corrección.                                             | Hoy revisaré de nuevo el modelado de datos, en caso de existir algún error corregirlo.                                                                                                                            | No tengo impedimentos por el momento.                                 |






### David Peñaranda



| Fecha      | Actividades previamente realizadas                                                                                                                                                                                                                                          | Actividades planeadas para hoy                                                                                                                                                                       | Inconvenientes que tengo                                                                          |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| 26/03/2023 |                                                                                                                                                                                                                                                                             | Buscar material sobre css y html. Empezar construcción de template de prueba.                                                                                                                        | Demasiada información.                                                                            |
| 2/04/2023  | Se estudió parte del curso de flexbox de Kevin Powell y algunos tutoriales de html. Se construyó una sección introductoria de prueba para poner en práctica los conceptos.                                                                                                  | Buscar material sobre bootstrap 5 y las clases predefinidas. Añadir el framework al template de prueba.                                                                                              |                                                                                                   |
| 9/04/2023  | Se estudiaron los aspectos esenciales de bootstrap 5. Se incluyó el framework al template de prueba.                                                                                                                                                                        | Investigar sobre Sass y otras herramientas útiles para el desarrollo de la página web. Culminar el estudio del material de css.                                                                      | Enlaces equivocados para conectar librería de font-awesome. Dificultad para compilar sass a css.  |
| 16/04/2023 | Se probaron las funcionalidades de sass. Se interactuó con las librería de fonts-awesome y google-fonts y se añadieron al template de prueba. Se terminó de estudiar el material de css. Se migró el código css a sass en el template de prueba.                            | Investigar sobre javascript y su interacción con html y css. Realizar una barra de navegación básica y añadir redirecciones.                                                                         | Falta de conocimiento sobre sass / lentitud para escribirlo.                                      |
| 19/04/2023 | Se migró el código sass a css por una situación concreta que no se pudo realizar con sass. Se realizó una barra de navegación básica y se añadió al template de prueba.                                                                                                     | Refactorizar la hoja de estilos y el html haciendo uso de las clases preestablecidas de boostrap. Investigar sobre el admin, orm, sqlite y las migraciones en Django.                                |                                                                                                   |
| 23/04/2023 | Se redujo el código css con la ayuda de bootstrap. Se realizó un crud de prueba en django.                                                                                                                                                                                  | Incluir el template de prueba en un proyecto de django. Separar los archivos estáticos. Investigar sobre los templates de django (bucles, condicionales, carga de archivos, extensión de templates). | Problemas con css al extender otro template de html.                                              |
| 26/04/2023 | Se interactuó con el sistema de templating de django y se vinculó una pantalla de prueba a un modelo de la base de datos. Se reemplazaron las vistas basadas en funciones por vistas basadas en clases.                                                                     | Investigar sobre las propiedades que hagan responsive al documento.                                                                                                                                  | Inconvenientes con las media queries de css.                                                      |
| 30/04/2023 | Se culminó el template de prueba.                                                                                                                                                                                                                                           | Iniciar construcción de las dos pantallas asignadas.                                                                                                                                                 |                                                                                                   |
| 6/05/2023  | Se construyó la página de inicio responsive (excepto barra de navegación). Se dejaron listos los enlaces que redirijen a otras urls.                                                                                                                                        | Construir un menú de hamburguesa animado para la vista móvil. Construir la página de categorías.                                                                                                     | Aparentemente se requerirá otro breakpoint para el tamaño de tablets. No se contempla de momento. |
| 7/05/2023  | Se terminó la mayoría de las dos vistas asignadas con los aspectos previstos (responsive, bootstrap, queries de la base de datos, vistas basadas en clases). Falta usar un template como base. Se descubrió un error en los estilos cuando el sistema operativo tiene zoom. | Corregir la hoja de estilos. Vincular la página principal con las funciones de navegación. Crear un template con el contenido necesario en head y la barra de navegación para reutilizar código.     |                                                                                                   |
| 8/05/2023  | Se creó y usó el template base y se redujo la cantidad de html. Se corrigió la hoja de estilos. Se vinculó el sistema de autenticación con la página principal.                                                                                                             |                                                                                                                                                                                                      |                                                                                                   |


