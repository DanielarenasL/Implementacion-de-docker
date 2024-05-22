from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    miConexion = pymysql.connect(host ='localhost',user ='root',passwd ='123daniel...',db = 'ubicaciones')
    cur = miConexion.cursor()

    cur.execute('select Id_Departamento, Nombre_Departamento, Id_Pais from departamento')
    departamentos = cur.fetchall()

    cur.execute('select Nombre_pais, Id_Pais from pais')
    paises = cur.fetchall()

    cur.execute('select Id_municipio, Nombre_municipio, Id_departamento from municipio')
    municipios = cur.fetchall()

    miConexion.close()

    return render_template('index.html', departamentos=departamentos, paises=paises, municipios=municipios)

@app.route('/submit-form', methods=['POST'])
def submit_form():
    miConexion = pymysql.connect(host ='localhost',user ='root',passwd ='123daniel...',db = 'ubicaciones')
    cur = miConexion.cursor()

    email = request.form['email']
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    pais = request.form['paisNacimiento']
    departamento = request.form['deptoNacimiento']
    municipio = request.form['municipioNacimiento']
    telefono = request.form['telefono']
    password = request.form['password']
    confirm_password = request.form['confirm_password']

    if password == confirm_password:
        cur.execute('INSERT INTO registro (Correo_Electronico, Nombre, Apellido, Pais_Nacimiento, Departamento_Nacimiento, Municipio_Nacimiento, Telefono, Contrasena, Confirma_Contrasena) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)', (email, nombre, apellido, pais, departamento, municipio, telefono, password, confirm_password))
        miConexion.commit()

    miConexion.close()

    return 'Formulario enviado con éxito'

if __name__ == '__main__':
    app.run(debug=True)
