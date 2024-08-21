from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Flask app creation and db connection initialization
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost:5432/testdb'

# Connecting database to app
db = SQLAlchemy(app)

class Person(db.Model):
   __tablename__ = 'person'
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String, nullable=False)

db.create_all()

@app.route('/')
def index():
  return "Hello World"

#always include this at the bottom of your code 
if __name__ == '__main__':
   app.run(host="0.0.0.0")