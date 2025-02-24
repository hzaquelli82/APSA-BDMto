from flask import Blueprint, render_template, request, redirect, url_for
from extensiones import db  # Importar `db` desde extensiones.py

usuarios_bp = Blueprint('usuarios', __name__)

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id_usuario = db.Column(db.SmallInteger, primary_key=True)
    apellido = db.Column(db.String(15), nullable=False)
    nombre = db.Column(db.String(30), nullable=False)
    usuario = db.Column(db.String(10), unique=True, nullable=False)
    passwd = db.Column(db.String(10), nullable=False)

@usuarios_bp.route('/usuarios', methods=['GET', 'POST'])
def usuarios():
    if request.method == 'POST':
        nuevo_usuario = Usuario(
            apellido=request.form['apellido'],
            nombre=request.form['nombre'],
            usuario=request.form['usuario'],
            passwd=request.form['passwd']
        )
        db.session.add(nuevo_usuario)
        db.session.commit()
        return redirect(url_for('usuarios.usuarios'))  # Redirige a la misma página

    usuarios = Usuario.query.all()
    return render_template('usuarios.html', usuarios=usuarios)
