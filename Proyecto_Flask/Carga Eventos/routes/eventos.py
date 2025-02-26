from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models import db, Evento, Sector

eventos_bp = Blueprint('eventos', __name__)

motivos = ["Mecánico", "Tolva Llena", "Falta MP", "Sistema", "Corte de Energía", "Eléctrico tablero"]

@eventos_bp.route('/eventos', methods=['GET', 'POST'])
def agregar_evento():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    sectores = Sector.query.all()
    
    if request.method == 'POST':
        nuevo_evento = Evento(
            fecha_hora_inicio=request.form['fecha_hora_inicio'],
            fecha_hora_fin=request.form['fecha_hora_fin'],
            id_usuario=session['user_id'],
            id_sector=request.form['id_sector'],
            motivo=request.form['motivo'],
            descripcion_m=request.form['descripcion_m']
        )
        db.session.add(nuevo_evento)
        db.session.commit()
        flash("Evento agregado con éxito", "success")
        return redirect(url_for('eventos.agregar_evento'))

    return render_template('agregar_evento.html', sectores=sectores, motivos=motivos)
