from flask import Blueprint, render_template

sectores_bp = Blueprint('sectores', __name__)

@sectores_bp.route('/sectores')
def sectores():
    return render_template('sectores.html')
