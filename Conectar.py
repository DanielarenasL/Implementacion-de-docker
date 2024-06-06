

if __name__ == '__main__':

    miConexion = pymysql.connect(host='172.17.0.3', user='admin', passwd='admin', db='proyecto')
    cur = miConexion.cursor()

    # Crear la tabla 'Pais' si no existe
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Pais (
        Id_Pais INT PRIMARY KEY NOT NULL,
        Nombre_Pais VARCHAR(20)
    )
    ''')

    # Crear la tabla 'Departamento' si no existe
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Departamento (
        Id_Departamento INT PRIMARY KEY NOT NULL,
        Nombre_Departamento VARCHAR(20),
        Id_Pais INT,
        FOREIGN KEY(Id_Pais) REFERENCES Pais(Id_Pais)
    )
    ''')

    # Crear la tabla 'Municipio' si no existe
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Municipio (
        Id_municipio INT PRIMARY KEY NOT NULL,
        Nombre_municipio VARCHAR(20),
        Id_departamento INT,
        FOREIGN KEY(Id_departamento) REFERENCES Departamento(Id_Departamento)
    )
    ''')
    
    # Crear la tabla 'Producto' si no existe
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Producto (
        Id_Producto INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
        Nombre_Producto VARCHAR(40) NOT NULL,
        Descripcion_Producto VARCHAR(60) NOT NULL,
        Precio_Producto INT NOT NULL,
        Tipo_Producto VARCHAR(20) NOT NULL,
        Talla_Producto VARCHAR(30) NOT NULL,
        Color_Producto VARCHAR(30) NOT NULL,
        Cantidad INT
    )
    ''')

    # Crear la tabla 'Usuarios' si no existe
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Usuarios (
        Correo_Electronico VARCHAR(255) PRIMARY KEY NOT NULL,
        Nombre VARCHAR(255) NOT NULL,
        Apellido VARCHAR(255) NOT NULL,
        Telefono INT NOT NULL,
        Contrasena VARCHAR(255) NOT NULL,
        Pais_Nacimiento INT NOT NULL,
        Departamento_Nacimiento INT NOT NULL,
        Municipio_Nacimiento INT NOT NULL,
        Admin BOOLEAN DEFAULT FALSE NOT NULL,
        FOREIGN KEY(Pais_Nacimiento) REFERENCES Pais(Id_Pais),
        FOREIGN KEY(Departamento_Nacimiento) REFERENCES Departamento(Id_Departamento),
        FOREIGN KEY(Municipio_Nacimiento) REFERENCES Municipio(Id_municipio)
    )
    ''')


    # Insertar datos en la tabla 'Pais' si está vacía
    cur.execute('SELECT COUNT(*) FROM Pais')
    if cur.fetchone()[0] == 0:
        cur.execute('''
        INSERT INTO Pais (Id_Pais, Nombre_Pais) VALUES
        (4,'Afganistan'),
        (276,'Alemania'),
        (32, 'Argentina'),
        (56, 'Belgica'),
        (68, 'Bolivia'),
        (634, 'Qatar'),
        (156, 'China'),
        (192, 'Cuba'),
        (170, 'Colombia'),
        (250, 'Francia')
        ''')

    # Insertar datos en la tabla 'Departamento' si está vacía
    cur.execute('SELECT COUNT(*) FROM Departamento')
    if cur.fetchone()[0] == 0:
        cur.execute('''
        INSERT INTO Departamento (Id_Departamento, Nombre_Departamento, Id_Pais) VALUES
        (92,'Kabul', 4), (93,'Kandaharl', 4), (94,'Herat', 4),
        (37,'Berlin', 276), (36,'Hamburgo', 276), (35,'Munich', 276),
        (32,'Buenos Aires', 32), (33,'Cordoba', 32), (34,'Rosario', 32),
        (57,'Bruselas', 56), (58,'Gent', 56), (59,'Namur', 56),
        (69,'Sucre', 68), (70,'La paz', 68), (71,'Tarija', 68),
        (635,'Doha', 634), (636,'Al Khor', 634), (157,'Pekin', 156),
        (158,'Shangai', 156), (193,'La habana', 192), (194,'Santa Clara', 192),
        (171,'Bogota', 170), (172,'Amazonas', 170), (173,'Pereira', 170),
        (251,'Paris', 250)
        ''')

    # Insertar datos en la tabla 'Municipio' si está vacía
    cur.execute('SELECT COUNT(*) FROM Municipio')
    if cur.fetchone()[0] == 0:
        cur.execute('''
        INSERT INTO Municipio (Id_municipio, Nombre_municipio, Id_departamento) VALUES
        (1,'Dashti Barchi',92), (2,'Kartey Sakhi',92),
        (3,'Ghorak',93), (4,'Daman',93),
        (5,'Shar Noe',94), (6,'Fargha',94),
        (7,'Mitte',37), (8,'Pankow',37),
        (9,'Tomesh',36), (10,'Appen',36),
        (11,'Aying',35), (12,'Brunnthal',35),
        (13,'Florencio',32), (14,'Varela',32),
        (15,'Alicia',33), (16,'Alma Fuerte',33),
        (17,'Perez',34), (18,'Funes',34),
        (19,'Jette',57), (20,'Forest',57),
        (21,'Lederberg',58), (22,'Afsnee',58),
        (23,'Ardenas',59), (24,'Condroz',59),
        (25,'San Lucas',69), (26,'Monteagudo',69),
        (27,'Laja',70), (28,'Pucarani',70),
        (29,'Bermejo',71), (30,'San lorenzo',71),
        (31,'Al Wakrah',635), (32,'Al Daayen ',635),
        (33,'Beijing',157), (34,'Distrito de Xicheng',157),
        (35,'Tianjin',158), (36,'Provincia de Jilin',158),
        (37,'Habana del este',193), (38,'Habana Vieja',193),
        (39,'Ranchuelo',194), (40,'Santo Domingo',194),
        (41,'Teusaquillo',171), (42,'Fontibon',171),
        (43,'Leticia',172), (44,'Puerto Alegria',172),
        (45,'Guatica',173), (46,'Belen de Umbria',173),
        (47,'Le Marais',251), (48,'Campos eliseos',251)
        ''')

    # Crear la tabla 'Comentarios' si no existe
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Comentarios (
        Id_Comentario INT AUTO_INCREMENT PRIMARY KEY,
        Id_Producto INT NOT NULL,
        Correo_Usuario VARCHAR(50) NOT NULL,
        Comentario VARCHAR(500) NOT NULL,
        Fecha DATETIME,
        FOREIGN KEY(Id_Producto) REFERENCES Producto(Id_Producto),
        FOREIGN KEY(Correo_Usuario) REFERENCES Usuarios(Correo_Electronico)
    )
    ''')

    # Crear la tabla 'Carrito' si no existe
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Carrito (
        Id_Carrito INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
        Correo_Usuario VARCHAR(50) NOT NULL,
        FOREIGN KEY(Correo_Usuario) REFERENCES Usuarios(Correo_Electronico)
    )
    ''')

    # Crear la tabla 'Items_Carrito' si no existe
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Items_Carrito (
        Id_Item INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
        Id_Carrito INT,
        Id_Producto INT,
        Cantidad_Producto INT,
        FOREIGN KEY(Id_Carrito) REFERENCES Carrito(Id_Carrito),
        FOREIGN KEY(Id_Producto) REFERENCES Producto(Id_Producto)
    )
    ''')

    # Crear la tabla 'Valoraciones_Productos' si no existe
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Valoraciones_Productos (
        Id_Valoracion INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
        Id_Producto INT NOT NULL,
        Correo_Usuario VARCHAR(50) NOT NULL,
        Valoracion INT,
        FOREIGN KEY(Id_Producto) REFERENCES Producto(Id_Producto),
        FOREIGN KEY(Correo_Usuario) REFERENCES Usuarios(Correo_Electronico)
    )
    ''')

    cur.execute('''
    INSERT INTO Usuarios (Correo_Electronico, Nombre, Apellido, Telefono, Contrasena, Pais_Nacimiento, Departamento_Nacimiento, Municipio_Nacimiento, Admin)
    VALUES('b.uribe@utp.edu.co', 'Brahyan', 'Uribe', 1234567890, 'Oconer49', 170, 171, 25, TRUE)
    ON DUPLICATE KEY UPDATE Correo_Electronico=Correo_Electronico
    ''')

    # Hacer commit para guardar los cambios
    miConexion.commit()

    # Mostrar los datos de las tablas 'Usuarios' y 'Producto'
    cur.execute('SELECT * FROM Usuarios')
    print("Usuarios:")
    for usuario in cur.fetchall():
        print(usuario)

    cur.execute('SELECT * FROM Producto')
    print("\nProductos:")
    for producto in cur.fetchall():
        print(producto)

    # Cerrar la conexión
    miConexion.close()

    #app.run(debug=True)
    app.run(host='0.0.0.0', port=5001, debug = True)
