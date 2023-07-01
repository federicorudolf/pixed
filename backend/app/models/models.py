# models.py
from ..database import db
from datetime import datetime

class Adulto(db.Model):
  __tablename__ = 'adultos'
  id_adulto = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(200), nullable=False)
  nombre = db.Column(db.String(200), nullable=False)
  fecha_nacimiento = db.Column(db.Date, nullable=False)
  usuarios = db.relationship('Usuario', backref='adulto', lazy=True)

class Usuario(db.Model):
  __tablename__ = 'usuarios'
  id_usuario = db.Column(db.Integer, primary_key=True)
  nombre = db.Column(db.String(200), nullable=False)
  email = db.Column(db.String(200), nullable=False)
  password = db.Column(db.String(500), nullable=False)
  fecha_registro = db.Column(db.Date, default=datetime.utcnow)
  autorizado = db.Column(db.Boolean, default=False)
  id_adulto = db.Column(db.Integer, db.ForeignKey('adultos.id_adulto'), nullable=False)

  def to_dict(self):
    return {
      'id_adulto': self.id_adulto,
      'id_usuario': self.id_usuario,
      'nombre': self.nombre,
      'email': self.email,
      'fecha_registro': self.fecha_registro
    }

class Contenido(db.Model):
  __tablename__ = 'contenidos'
  id_contenido = db.Column(db.Integer, primary_key=True)
  titulo = db.Column(db.String(60), nullable=False)
  descripcion = db.Column(db.String(200), nullable=False)
  autor = db.Column(db.String(200), nullable=False)
  dificultad = db.Column(db.Float, nullable=False)
  calificacion = db.Column(db.Float, nullable=False)

class Progreso(db.Model):
  __tablename__ = 'progresos'
  id_progreso = db.Column(db.Integer, primary_key=True)
  id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'), nullable=False)
  id_contenido = db.Column(db.Integer, db.ForeignKey('contenidos.id_contenido'), nullable=False)
  progreso = db.Column(db.Float, nullable=False)
  terminado = db.Column(db.Boolean, default=False)

class Recomendacion(db.Model):
  __tablename__ = 'recomendaciones'
  id_recomendacion = db.Column(db.Integer, primary_key=True)
  id_contenido = db.Column(db.Integer, db.ForeignKey('contenidos.id_contenido'), nullable=False)
  id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'), nullable=False)

class Actividad(db.Model):
  __tablename__ = 'actividades'
  id_actividad = db.Column(db.Integer, primary_key=True)
  fecha = db.Column(db.Date, default=datetime.utcnow)
  id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'), nullable=False)
  id_contenido = db.Column(db.Integer, db.ForeignKey('contenidos.id_contenido'), nullable=False)
  actividad = db.Column(db.String(200), nullable=False)

class Resena(db.Model):
  __tablename__ = 'resenas'
  id_resena = db.Column(db.Integer, primary_key=True)
  id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'), nullable=False)
  id_contenido = db.Column(db.Integer, db.ForeignKey('contenidos.id_contenido'), nullable=False)
  calificacion = db.Column(db.Boolean, default=False)
  completado = db.Column(db.Boolean, default=False)