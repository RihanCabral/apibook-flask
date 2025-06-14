from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from flask import request, jsonify

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)

# Model - 
class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str]

class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    author: Mapped[str]
    genre: Mapped[str]
    year: Mapped[int]
    title: Mapped[str]

# Criação da tabela no banco
with app.app_context():
    db.create_all()
    
# POST
@app.route("/books",methods=["POST"])
def add_book():
    data=request.get_json()
    new_book = Book(author=data["author"], genre=data["genre"], year=data["year"],title=data["title"]
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify({"message": "Livro adicionado com sucesso!"}), 201

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/teste")
def rota_teste():
    return "<p>Rota, teste!</p>"


# {
	#"author": "Tester",
	#"genre": "Livro de Testes",
	#"year": "2025",
	#"title": "Uma Introdução ao Teste" }