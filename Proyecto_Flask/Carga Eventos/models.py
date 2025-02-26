from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id_usuario = db.Column(db.Integer, primary_key=True)
    apellido = db.Column(db.String(15), nullable=False)
    nombre = db.Column(db.String(30), nullable=False)
    usuario = db.Column(db.String(10), unique=True, nullable=False)
    passwd = db.Column(db.String(10), nullable=False)

class Sector(db.Model):
    __tablename__ = 'sectores'
    id_sector = db.Column(db.SmallInteger, primary_key=True)
    nombre = db.Column(db.String, nullable=False)
    descripcion = db.Column(db.String)

class Evento(db.Model):
    __tablename__ = 'eventos'
    id_evento = db.Column(db.Integer, primary_key=True)
    fecha_hora_inicio = db.Column(db.DateTime, nullable=False)
    fecha_hora_fin = db.Column(db.DateTime)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'), nullable=False)
    id_sector = db.Column(db.Integer, db.ForeignKey('sectores.id_sector'), nullable=False)
    motivo = db.Column(db.String, nullable=False)
    descripcion_m = db.Column(db.String(30))

    usuario = db.relationship('Usuario', backref='eventos')
    sector = db.relationship('Sector', backref='eventos')
