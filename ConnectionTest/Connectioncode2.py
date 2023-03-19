#Connecting MySQL to Python
from flask import Flask,render_template, request
from flask_mysqldb import MySQL
import mysql.connector
from mysql import connector

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Skywalker88!'
app.config['MYSQL_DB'] = 'new_schema'

db=mysql.connector.connect(host="localhost", user="root", password="Skywalker88!",database="new_schema")

mysql = MySQL(app)




@app.route('/')
def index():
   cursor = db.cursor()
   cursor.execute("SELECT * FROM liquors")
   data = cursor.fetchall()
   print (data)
   return render_template('index.html', data=data)
   
@app.route('/remove', methods = ['DELETE'])
def removepage():
   cursor = db.cursor()
   cursor.execute("SELECT ")
   rmdata = cursor.fetchmany(size=1)
   print (rmdata)
   return render_template('remove.html', rmdata = rmdata)

@app.route('/page2' )
def page2():
   cursor = db.cursor()
   cursor.execute("SELECT nameFoods, stockFoods FROM foods")
   data = cursor.fetchall()
   print(data)
   return render_template('page2.html', data=data)

   
app.run(debug=True)