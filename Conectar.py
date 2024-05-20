import pymysql

miConexion = pymysql.connect(host ='localhost',user ='root',passwd ='123daniel...',db = 'ubicaciones')
cur = miConexion.cursor()

cur.execute('select Id_Departamento, Nombre_Departamento from departamento')
for Id_Departamento, Nombre_Departamento in cur.fetchall():
    print(Id_Departamento," / ",Nombre_Departamento)

cur.execute('select Nombre_pais, Id_Pais from pais')
for  Nombre_pais, Id_Pais in cur.fetchall():
    print(Nombre_pais," / ",Id_Pais)


miConexion.close()