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

class ParteDiario(db.Model):
    __tablename__ = "parte_diario"

    id_parte = db.Column(db.Integer, primary_key=True)
    nrid = db.Column(db.Integer, db.ForeignKey("formulas.nrid"), nullable=False)
    hora_inicio = db.Column(db.Time, nullable=False)
    hora_fin = db.Column(db.Time, nullable=False)
    toneladas = db.Column(db.Integer, nullable=False)
    destino = db.Column(db.String(10), nullable=False)
    nro_zaranda = db.Column(db.String(20), nullable=False)
    producto_lb = db.Column(db.String(20), nullable=False)
    peso_lb = db.Column(db.Integer, nullable=False)

    def __init__(self, nrid, hora_inicio, hora_fin, toneladas, destino, nro_zaranda, producto_lb, peso_lb):
        self.nrid = nrid
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.toneladas = toneladas
        self.destino = destino
        self.nro_zaranda = nro_zaranda
        self.producto_lb = producto_lb
        self.peso_lb = peso_lb

class Formulas(db.Model):
    __tablename__ = 'formulas'
    nrid = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(10), nullable=False)
    nombre = db.Column(db.String, nullable=False)
    vt = db.Column(db.Integer, nullable=False)
    
    @staticmethod
    def get_formula_names():
        return [formula.nombre for formula in Formulas.query.all()]