from flask import Blueprint, request, jsonify, make_response
from app.models.models import Usuario, Adulto
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import create_access_token
from ..database import db

user_bp = Blueprint('usuarios', __name__)

@user_bp.route('/usuario/<int:id>', methods=['GET'])
def get_usuario(id):
    usuario = Usuario.query.get(id)
    if usuario is None:
        return jsonify(error="Usuario no encontrado"), 404
    else:
        return jsonify(usuario=usuario.to_dict())

@user_bp.route('/login', methods=['POST'])
def login():
    if request.method == 'OPTIONS':
        print('Login')
        return _build_cors_preflight_response()
    elif request.method == 'POST':
        email = request.json.get('email', None)
        password = request.json.get('password', None)
        user = Usuario.query.filter_by(email=email).first()
        if user is None or not check_password_hash(user.password, password):
            return jsonify({ login: False}), 401
        access_token = create_access_token(identity=email)
        response = make_response(jsonify(access_token=access_token), 200)
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response

@user_bp.route('/register', methods=['POST'])
def register():
    if request.method == 'OPTIONS':
        print('Register')
        return _build_cors_preflight_response()
    else:
        name = request.json.get('name', None)
        email = request.json.get('email', None)
        password = request.json.get('password', None)
        adult_email = request.json.get('adult_email', None)
        if not email or not password or not adult_email:
            return jsonify(message='Debe ingresar email, contraseña y los datos del adulto responsable'), 400

        hashed_password = generate_password_hash(password)
        adult = Adulto.query.filter_by(email=adult_email).first()
        
        if not adult:
            adult = Adulto(email=adult_email, nombre="Test", fecha_nacimiento="01/01/1989")
            db.session.add(adult)
            db.session.commit()

        new_user = Usuario(nombre=name, email=email, password=hashed_password, id_adulto=adult.id_adulto)
        access_token = create_access_token(identity=email)

        db.session.add(new_user)
        db.session.commit()

        return jsonify(user=new_user.to_dict(), access_token=access_token), 201

def _build_cors_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response

    
# 2209707949A
"""
Etapa 2: Desarrollo de la interfaz de usuario

Diseño de la interfaz de usuario: Diseña la interfaz de usuario de las pantallas utilizando Svelte y Bootstrap o alguna otra biblioteca de estilos. En este punto, podrías centrarte en las pantallas de registro y login.

Integración frontend-backend: Conecta la interfaz de usuario con tu servidor Flask. Asegúrate de que los datos ingresados en los formularios de la interfaz de usuario se envíen correctamente al servidor y que las respuestas del servidor se manejen correctamente.

Etapa 3: Desarrollo del contenido educativo y la retroalimentación del usuario

Desarrollo de contenido educativo: Comienza a desarrollar el contenido educativo, como los juegos de codificación y los tutoriales. Podrías empezar con algo simple, como el juego de tic-tac-toe que mencionaste.

Implementación de la retroalimentación del usuario: Implementa la funcionalidad para que los usuarios puedan calificar el contenido y sus comentarios se guarden en la base de datos.

Etapa 4: Desarrollo del motor de IA

Desarrollo del motor de IA: Comienza a trabajar en el motor de IA utilizando PyTorch. En este punto, podrías centrarte en recopilar y analizar los datos de interacción del usuario que mencionamos antes (tiempo pasado en cada actividad, tasa de finalización, tasa de error, retroalimentación del usuario, etc.).
Etapa 5: Pruebas y despliegue

Pruebas: Realiza pruebas para asegurarte de que todas las partes de la plataforma funcionan como se espera. Aunque mencionaste que inicialmente se harán solo pruebas unitarias, sería beneficioso realizar pruebas de integración y funcionales en el futuro.

Despliegue: Configura el despliegue automático utilizando Github y AWS EC2.

Por supuesto, este es solo un plan inicial y probablemente necesitará ser adaptado a medida que avanza el proyecto. ¿Qué opinas? ¿Hay algún cambio que quieras hacer o algo que quieras priorizar?"""