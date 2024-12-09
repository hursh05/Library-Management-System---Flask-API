from flask import Blueprint, request, jsonify
from extensions import db, bcrypt, jwt
from models import Member


auth_bp = Blueprint('auth_bp', __name__)



@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_member = Member(
        name=data['name'],
        email=data['email'],
        password=hashed_password,
    )
    db.session.add(new_member)
    db.session.commit()
    return jsonify({"message": "User registered successfully!"}), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = Member.query.filter_by(email=data['email']).first()
    if user and bcrypt.check_password_hash(user.password, data['password']):
        token = jwt.create_access_token(identity=user.id)
        return jsonify({"token": token}), 200
    return jsonify({"message": "Invalid credentials"}), 401
