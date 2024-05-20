from flask import Flask, render_template
import pymysql

app = Flask(__name__)

@app.route('/')
def home():
    miConexion = pymysql.connect(host ='localhost',user ='root',passwd ='123daniel...',db = 'ubicaciones')
    cur = miConexion.cursor()

    cur.execute('select Id_Departamento, Nombre_Departamento from departamento')
    departamentos = cur.fetchall()

    cur.execute('select Nombre_pais, Id_Pais from pais')
    paises = cur.fetchall()

    miConexion.close()

    return render_template('index.html', departamentos=departamentos, paises=paises)

if __name__ == '__main__':
    app.run(debug=True)