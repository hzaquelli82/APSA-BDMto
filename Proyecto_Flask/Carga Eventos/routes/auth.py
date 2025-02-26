from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models import db, Usuario

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        passwd = request.form['passwd']
        user = Usuario.query.filter_by(usuario=usuario, passwd=passwd).first()

        if user:
            session['user_id'] = user.id_usuario
            return redirect(url_for('eventos.agregar_evento'))
        else:
            flash("Credenciales incorrectas", "danger")
    
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('auth.login'))
