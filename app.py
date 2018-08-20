from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bourdain.db'
db = SQLAlchemy(app)

class Bourdain(db.Model):
 __tablename__ = 'bourdain'
 __table_args__ = {
   'autoload': True,
   'autoload_with': db.engine
 }
 index = db.Column(db.Integer, primary_key=True)
 #primnary_key is a unique field in your database

@app.route("/")
def hello():
	places = Bourdain.query.all()
	return render_template("list.html", places = places)

@app.route("/places/")
def schools():
	places = Bourdain.query.all()
	return render_template("list.html", places = places)

@app.route("/places/<index>/")
def place(index):
	# talk to database
	place = Bourdain.query.filter_by(index=index).first() # this is like saying SELECT * FROM schools LIMIT one
	return render_template("show.html", place=place)

# @app.route("/search")
# def search():
# 	name = request.args.get('query')
# 	places = Bourdain.query.filter(Bourdain.City.contains(name)).all()
# 	places2 = Bourdain.query.filter(Bourdain.Country.contains(name)).all()
# 	return render_template("list.html", places = places, places2 = places2)


# this is saying, if this is run from the command line, do something:
if __name__ == '__main__':
 app.run(debug=True)


 # Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)  <--- this is local host
 # so go to localhost:5000 in browser