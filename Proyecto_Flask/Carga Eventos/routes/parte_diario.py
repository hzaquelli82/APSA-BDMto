from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, ParteDiario
from datetime import datetime

parte_diario_bp = Blueprint("parte_diario", __name__)

@parte_diario_bp.route("/parte_diario", methods=["GET", "POST"])
def agregar_parte_diario():
    if request.method == "POST":
        try:
            nrid = request.form["nrid"]
            hora_inicio = datetime.strptime(request.form["hora_inicio"], "%H:%M").time()
            hora_fin = datetime.strptime(request.form["hora_fin"], "%H:%M").time()
            toneladas = int(request.form["toneladas"])
            destino = request.form["destino"]
            nro_zaranda = request.form["nro_zaranda"]
            producto_lb = request.form["producto_lb"]
            peso_lb = int(request.form["peso_lb"])

            nuevo_parte = ParteDiario(nrid, hora_inicio, hora_fin, toneladas, destino, nro_zaranda, producto_lb, peso_lb)
            db.session.add(nuevo_parte)
            db.session.commit()
            flash("Parte diario agregado correctamente", "success")
            return redirect(url_for("parte_diario.agregar_parte_diario"))

        except Exception as e:
            flash(f"Error: {str(e)}", "danger")
            return redirect(url_for("parte_diario.agregar_parte_diario"))

    return render_template("parte_diario.html")

@app.route('/agregar_parte_diario', methods=['GET', 'POST'])
def agregar_parte_diario():
    if request.method == 'POST':
        # Get data from the form
        nrid = request.form.get('nrid') #This will be populated from the dropdown
        hora_inicio = request.form.get('hora_inicio')
        hora_fin = request.form.get('hora_fin')
        toneladas = request.form.get('toneladas')
        destino = request.form.get('destino')
        nro_zaranda = request.form.get('nro_zaranda')
        producto_lb = request.form.get('producto_lb')
        peso_lb = request.form.get('peso_lb')

        #Error Handling
        if not nrid:
            flash('Debe seleccionar una formula', 'error')
            return redirect(url_for('parte_diario.agregar_parte_diario'))

        try:
            new_parte_diario = ParteDiario(nrid=int(nrid), hora_inicio=hora_inicio, hora_fin=hora_fin, toneladas=int(toneladas), destino=destino, nro_zaranda=nro_zaranda, producto_lb=producto_lb, peso_lb=int(peso_lb))
            db.session.add(new_parte_diario)
            db.session.commit()
            flash('Parte diario agregado correctamente', 'success')
            return redirect(url_for('parte_diario.agregar_parte_diario')) #Redirect to the same page to avoid resubmission
        except Exception as e:
            db.session.rollback()
            flash(f'Error al agregar parte diario: {e}', 'error')
            return redirect(url_for('parte_diario.agregar_parte_diario'))

    formula_names = Formulas.get_formula_names()
    return render_template('parte_diario.html', formula_names=formula_names)