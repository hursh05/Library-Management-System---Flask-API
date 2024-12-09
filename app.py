from flask import Flask
from extensions import db, bcrypt, jwt
from routes.auth import auth_bp
from routes.books import books_bp


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'supersecretkey'

db.init_app(app)
bcrypt.init_app(app)
jwt.init_app(app)

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(books_bp, url_prefix="/books")


with app.app_context():
    db.create_all()
    print("Database initialized!")


if __name__ == "__main__":
    app.run(debug=True)
