from flask import Blueprint, render_template, request, redirect, url_for
from extensiones import db

sectores_bp = Blueprint('sectores', __name__)

class Sector(db.Model):
    __tablename__ = 'sectores'
    id_sector = db.Column(db.SmallInteger, primary_key=True, nullable=False)
    nombre = db.Column(db.String, nullable=False)  # character varying
    descripcion = db.Column(db.String, nullable=True)  # Puede ser nulo

# 📌 Ruta para agregar un sector
@sectores_bp.route('/sectores', methods=['GET', 'POST'])
def sectores():
    if request.method == 'POST':
        nuevo_sector = Sector(
            nombre=request.form['nombre'],
            descripcion=request.form.get('descripcion', None)  # Opcional
        )
        db.session.add(nuevo_sector)
        db.session.commit()
        return redirect(url_for('sectores.sectores'))
    
    sectores = Sector.query.all()
    return render_template('sectores.html', sectores=sectores)
