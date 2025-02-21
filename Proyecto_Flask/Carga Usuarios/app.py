from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://apsa:Apsa2812p.@192.168.0.12:5432/db_mto'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'supersecreto'

db = SQLAlchemy(app)

# Definir el modelo de la tabla usuarios
class Usuario(db.Model):
    __tablename__ = 'usuarios' 
    id_usuario = db.Column(db.SmallInteger, primary_key=True)
    apellido = db.Column(db.String(15), nullable=False)
    nombre = db.Column(db.String(30), nullable=False)
    usuario = db.Column(db.String(10), unique=True, nullable=False)
    passwd = db.Column(db.String(10), nullable=False)

# Ruta para mostrar el formulario
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nuevo_usuario = Usuario(
            apellido=request.form['apellido'],
            nombre=request.form['nombre'],
            usuario=request.form['usuario'],
            passwd=request.form['passwd']
        )
        db.session.add(nuevo_usuario)
        db.session.commit()
        return redirect(url_for('index'))

    usuarios = Usuario.query.all()
    return render_template('index.html', usuarios=usuarios)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crea la tabla si no existe
    app.run(debug=True)
