from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from .models.models import Adulto, Usuario, Contenido, Actividad, Progreso, Recomendacion, Resena
from .routes.usuario import user_bp
from .database import db

def create_app():
  app = Flask(__name__)
  CORS(app, resources={r"/*": {"origins": "*"}})
  app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost:5432/pixed'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  # Cambiar esto a algo seguro en producción
  app.config['JWT_SECRET_KEY'] = 'super-secret'

  JWTManager(app)
  
  db.init_app(app)
  app.register_blueprint(user_bp)

  with app.app_context():
    db.create_all()
  
  return app