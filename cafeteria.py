#Importación de librerias en Flask
# Flask: funciones de microframework
#render_template: permite renderizar los HTML en el servidor

from flask import Flask,redirect,url_for,render_template,request
from flask_mail import Mail,Message
# from flask_mail import Mail,Message

#Instancia la aplicación 
app=Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'correo@gmail.com'
app.config['MAIL_PASSWORD'] = 'contraseñade correo'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

#Login
@app.route("/") 
@app.route('/login')
def login():
    return render_template('login.html')

# Definimos el route con el método GET
@app.route('/defusuario', methods=['GET'])
def usuario():
    # Obtenemos la información del parametro "nombreUser"
    # Esto lo hacemos con "request.args.get"
    nombreUser = request.args.get('username')
    passW = request.args.get('password')
    print(nombreUser, file=sys.stderr) 
    print(passW, file=sys.stderr) 
    
    # Retornamos la respuesta
    if nombreUser == "admin" and passW == "nimda":
        return render_template('PaginaInicial_Admin.html')
    elif nombreUser == "cajero" and passW == "orejac":
        return render_template('PaginaInicial_Cajero.html')
    else:
        return render_template('PaginaInicial_Cajero.html')

#Recuperación de Contraseña
@app.route("/olvidaste")
def olvidaste():
    return render_template('RecupContra.html')

@app.route('/send_password',methods=['GET','POST'])
def send_password():
    if request.method == "POST":
        email=request.form['email']
        subject= 'Recuperación contraseña usuario'
        msg = 'Usted ha solicitado la recuperación de la contraseña que es #1231234'
        message = Message(subject,sender='correo@gmail.com',recipients=[email])
        message.body = msg

        mail.send(message)
    return render_template('result.html')
##PAGINA PRINCIPAL DE ADMIN 
@app.route("/paginaPrinAdmin",methods=['GET','POST'])
def paginaPrinAdmin():
    return render_template('PaginaInicial_Admin.html')

##PAGINA PRINCIPAL CAJEROS

@app.route("/paginaPrinCajero",methods=['GET','POST'])
def paginaPrinCajero():
    return render_template('PaginaInicial_Cajero.html')

#Gestión de Cajeros
@app.route('/gescajeros',methods=['GET','POST'])
def gescajero():
    return render_template('GestionCajeros.html')
#generé otra ruta para Actualizar-Eliminar Cajeros desde GESTIONCAJEROS #D3A
@app.route("/actuEliCajero",methods=['GET','POST'])
def actuEliCajero():
    return render_template('ActElimCajeros.html')

#Registro de Productos
@app.route('/regisproducto',methods=['GET','POST'])
def regisproducto():
    return render_template('CrearProducto.html')

#Crear Productos
@app.route('/crearproducto',methods=['GET','POST'])
def crearproducto():
    return render_template('CrearProducto.html')

#Actualizar y Eliminar Producto
@app.route('/actelimproducto',methods=['GET','POST'])
def actelimproducto():
    return render_template('ActualizarEliminarProducto.html')

#Gestión de Ventas
@app.route('/gestionventas',methods=['GET','POST'])
def gestionventas():
    return render_template('GestionDeVentas.html')

#Buscar Producto
@app.route('/buscarproducto',methods=['GET','POST'])
def buscarproducto():
    return render_template('Buscar.html')

if __name__ == '__main__':
    #Lanzar el servidor
    app.run(port=5000,debug=True)