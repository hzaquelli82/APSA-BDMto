from flask import Flask
from extensiones import db  # Importar `db` desde extensiones.py

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://apsa:Apsa2812p.@192.168.0.12:5432/db_mto'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'supersecreto'

db.init_app(app)  # Inicializar SQLAlchemy con la app

# Importar Blueprints después de inicializar `db`
from routes.usuarios import usuarios_bp
app.register_blueprint(usuarios_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crear tablas si no existen
    app.run(debug=True)
