from flask import Flask, render_template
from extensiones import db  # Importar `db` desde extensiones.py

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://apsa:Apsa2812p.@192.168.0.12:5432/db_mto'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'supersecreto'

db.init_app(app)  # Inicializar SQLAlchemy con la app

# Importar Blueprints después de inicializar `db`
from routes.usuarios import usuarios_bp
app.register_blueprint(usuarios_bp)
from routes.sectores import sectores_bp
app.register_blueprint(sectores_bp)

# Ruta para la página principal
@app.route('/')
def index():
    return render_template('index.html')  # Asegúrate de tener index.html en /templates


if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crear tablas si no existen
    app.run(debug=True)
