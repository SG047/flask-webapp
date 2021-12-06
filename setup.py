from flask import Flask, render_template,request,redirect,url_for
#from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__) #name of the module or package

#app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql+psycopg2://postgres:Monday09@localhost/quotes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db = SQLAlchemy(app)

class Favquotes(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	author = db.Column(db.String(30))
	quote = db.Column(db.String(2000))


@app.route("/")
def index():
    return render_template("index.html")

@app.route('/web')
def web():
    return render_template("web.html")


@app.route('/process',methods=['POST'])
def process():
    author=request.form['author']
    quote=request.form['quote']
    return redirect(url_for("index.html"))



#@app.route("/list")
#def list():
#    fruits=["apple","mango","grapes", "oranges"]
#    return render_template("index.html", fruits=fruits)


