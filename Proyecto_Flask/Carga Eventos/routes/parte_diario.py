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
