# Paquetizacion de entorno de desarrollo
Tecnologias HTML, CSS, Python, Flask, MySQL y linux Ubuntu 22.04

# Integrantes
-Daniel Arenas  
-Camilo Ceballos  
-Brahyan Uribe  
-Felipe Castillo

# Marco teorico

## Docker

### ¿Que es?
El término "Docker" se aplica a diferentes conceptos, entre los que se incluyen un proyecto de la comunidad open source y sus herramientas; Docker Inc., la principal empresa promotora del proyecto; y las herramientas que la empresa respalda formalmente. El hecho de que las tecnologías y la compañía compartan el mismo nombre puede ser confuso.  

Con Docker, puede utilizar los contenedores como máquinas virtuales muy livianas y modulares, y obtiene la flexibilidad necesaria para crearlos, implementarlos, copiarlos y trasladarlos de un entorno a otro, lo cual le permite optimizar las aplicaciones para la nube.

### ¿Cómo funciona?
La tecnología Docker utiliza el kernel de Linux y sus funciones, como los grupos de control y los espacios de nombre, para dividir los procesos y ejecutarlos de manera independiente. El propósito de los contenedores es ejecutar varios procesos y aplicaciones por separado para que se pueda aprovechar mejor la infraestructura y, al mismo tiempo, conservar la seguridad que se obtendría con los sistemas individuales.


## Python
Python es un lenguaje de programación de alto nivel, interpretado y de propósito general. Su filosofía hace hincapié en la legibilidad del código, utilizando una sintaxis que se asemeja al lenguaje natural y evitando el uso excesivo de paréntesis y llaves. Es un lenguaje multiparadigma, lo que significa que admite varios estilos de programación, incluyendo la pro
gramación orientada a objetos, la imperativa y la funcional.

## HTML (lenguaje de marcado de hipertexto)
La función de HTML como lenguaje de marcado es definir la estructura del contenido de la página web. Esto incluye especificaciones para elementos como títulos, párrafos, enlaces, imágenes y formularios, entre otros, que componen una página: su representación visual y código subyacente.

## CSS
CSS es un lenguaje de diseño que se utiliza principalmente para diseñar páginas web creadas con HTML. Permite al usuario definir propiedades como colores, márgenes, tamaños de fuente y diseños de página; Estos se pueden configurar de manera diferente para cambiar el aspecto de un sitio web y hacerlo más atractivo visualmente.

 ## Flask
 Flask es un marco de Python que resulta útil en la creación de páginas web. No solo cumple la función de crear rutas, sino que también gestiona sesiones y autentica a los usuarios fácilmente ofreciendo herramientas y bibliotecas. El principio que sigue Flask es lo que se conoce como "microframework". Es minimalista y flexible, lo que significa que los desarrolladores tienen la libertad de elegir sus herramientas y bibliotecas preferidas mientras trabajan en sus proyectos con Flask.

 ## MySQL
 MySQL es la base de datos de código abierto más popular del mercado. Según DB-Engines, MySQL se clasifica como la segunda base de datos más popular, detrás de Oracle Database. MySQL potencia muchas de las aplicaciones más accesibles, como Facebook, Twitter, Netflix, Uber, Airbnb, Shopify y Booking.com. 

 Dado que MySQL es de código abierto, incluye numerosas funciones desarrolladas en estrecha colaboración con los usuarios durante más de 25 años. Por lo tanto, es muy probable que su aplicación o lenguaje de programación favorito sea compatible con MySQL Database.

### MySQL es un sistema de gestión de bases de datos relacionales
Las bases de datos son el repositorio de datos esencial para todas las aplicaciones de software. Por ejemplo, cada vez que alguien realiza una búsqueda en Internet, inicia sesión en una cuenta o completa una transacción, un sistema de base de datos está almacenando la información para poder acceder a ella en el futuro.

Una base de datos relacional almacena los datos en tablas separadas en lugar de poner todos los datos en un gran almacén. La estructura de la base de datos se organiza en archivos físicos optimizados para una mayor agilidad. El modelo de datos lógico, con objetos como tablas de datos, vistas, filas y columnas, ofrece un entorno de programación flexible. Se establecen reglas que rigen las relaciones entre los distintos campos de datos, como uno a uno, uno a muchos, únicos, obligatorios u opcionales, y "punteros" entre distintas tablas. La base de datos aplica estas reglas de modo que, con una base de datos bien diseñada, tu aplicación nunca ve datos incoherentes, duplicados, huérfanos, desfasados o ausentes.

## Metodología para el Desarrollo de la Página Web:

Para desarrollar la página web propuesta, se seguirá una metodología estructurada que abarca desde la configuración inicial del entorno de desarrollo hasta la implementación de la base de datos y la creación de contenido. A continuación, se detallan los pasos a seguir:

## 1. Configuración del Entorno de Desarrollo

Para comenzar, es necesario configurar el entorno de desarrollo. Esto incluye la instalación de herramientas y la preparación del sistema para el desarrollo web. Los pasos a seguir son los siguientes:

Instalación de Herramientas: Se instalarán las herramientas necesarias, como un editor de texto o un entorno de desarrollo integrado y una base de datos, dependiendo de las preferencias del desarrollador.

## 2. Creación de la Base de Datos

Para almacenar y gestionar los datos de la página web, se utilizará MySQL, Los pasos para crear la base de datos son los siguientes:

    1. Se creo la base de datos 'proyecto'  

    2. Se crearon las siguientes tablas:  

        -Producto
        -Usuarios
        -Pais
        -Departamento
        -Municipio
        -Comentarios
        -Carrito
        -Items_Carrito
        -Valoraciones_Productos
        cada una con sus respectivos atributos para que funcione  

    3. Se añadieron nuevos registros a las tablas de Pais, Departamento, Municipio y un usuario administrador a la tabla Usuarios  

    4. por medio de el archivo Conectar.py se realizo la conexion con el siguiente codigo: 

    miConexion = pymysql.connect(host ='172.17.0.3',user ='admin',passwd ='admin',db = 'proyecto')
    cur = miConexion.cursor()

    lo cual crea la conexion local


## 3. Diseño y Desarrollo de la Página Web:

Con el entorno de desarrollo configurado y la base de datos lista, se procederá al diseño y desarrollo de la página web. Esto implica la creación de la estructura HTML, el diseño CSS y la implementación de la lógica del lado del servidor utilizando Flask. Los pasos a seguir fueron los siguientes:

## Diseño de la Interfaz de Regitro: 
Se diseño la interfaz de Registro de la página web utilizando HTML y CSS. Se prestará especial atención a la usabilidad y la experiencia del usuario.
![imagen-2024-06-06-113615855.png](https://i.postimg.cc/ZYrRdJ6D/imagen-2024-06-06-113615855.png)

## Diseño de la Interfaz de Inicio de Sesion:
Se diseño la interfaz de Inicio de Sesion de la pagina web utilizando HTML y CSS. Conectado con la Base de datos para la verificacion de los datos
[![imagen-2024-06-06-113946773.png](https://i.postimg.cc/Qt6JhcSv/imagen-2024-06-06-113946773.png)](https://postimg.cc/Hcyytcqt)

## Diseño de la Interfaz de Inicio:
Se diseño la interfaz de inicio la cual se vera al ingresar los datos correspondientes en el registro esta interfaz esta compuesta de tarjetas de compra una y una barra lateral con opciones.
[![imagen-2024-06-06-114111958.png](https://i.postimg.cc/VvxZM2pj/imagen-2024-06-06-114111958.png)](https://postimg.cc/xNPPVp0C)

## Diseño de la Interfaz de Administrador:
Se diseño una interfaz administrador la cual cuenta con los botones de todas las opciones que tiene el administrador.  
[![imagen-2024-06-06-115456069.png](https://i.postimg.cc/5ySCJRLx/imagen-2024-06-06-115456069.png)](https://postimg.cc/JHtncKpg)

## Diseño de la Interfaz Gestionar descuento:
Se diseño esta interfaz para que el administrador pueda aplicar un descuento a un producto de su tienda.
[![imagen-2024-06-06-115911769.png](https://i.postimg.cc/vHj3N1Y3/imagen-2024-06-06-115911769.png)](https://postimg.cc/3dXXyxDv)

## Diseño de la Interfaz ver stock:
Se diseño esta interfaz con el proposito de facilitar al administrador estar pendiente de cuanto stock le queda de cada producto de su tienda, consiste en una tabla interactiva que verifica la tabla productos de la base de datos para saber cuantos productos tiene y que cantidad hay.
[![imagen-2024-06-06-120334526.png](https://i.postimg.cc/5289HCjr/imagen-2024-06-06-120334526.png)](https://postimg.cc/qNMHSgsc)

## Diseño de la Interfaz Administrar mercancia:
Esta interfaz permite al administrador acceder a un producto mediante su Id y agregar o eliminar cantidades a dicho producto facilitando asi registrar el ingreso de un producto.
[![imagen-2024-06-06-121211400.png](https://i.postimg.cc/5tXNgRtX/imagen-2024-06-06-121211400.png)](https://postimg.cc/8FVSPwMG)

## Diseño de la interfaz Gestionar mercancia:
Permite al administrador agregar un producto nuevo o eliminar uno existente dependiendo de lo que necesite.
[![imagen-2024-06-06-121334938.png](https://i.postimg.cc/vZLK4rwD/imagen-2024-06-06-121334938.png)](https://postimg.cc/FYzpqJRQ)

## Diseño de la Interfaz de carrito
Permite al usuario ver los articulos que tiene en su carrito, asi como comprar un articulo de dicho carrito o eliminarlo.
[![imagen-2024-06-06-121627011.png](https://i.postimg.cc/qvyNy71N/imagen-2024-06-06-121627011.png)](https://postimg.cc/6866NBJK)

