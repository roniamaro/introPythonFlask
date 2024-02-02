#importação
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
db = SQLAlchemy(app)

#modelagem de dados
#produto (id, name, price, description)
class Product(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), nullable=False)
  price = db.Column(db.Float, nullable=False)
  description = db.Column(db.String(120), nullable=True)

#definir uma rota raiz (página inicial) e a função que será executada ao requisitar
@app.route('/')
def hello_world():
  return 'Hello World'

if __name__ == "__main__":
  app.run(debug=True)