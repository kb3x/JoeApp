# how to use css in python_ flask
# flask render_template example
 
from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from flask_mysqldb import MySQLdb
#missing item----------------------------------------------------------

# Provide template folder name
# The default folder name should be "templates" else need to mention custom folder name
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Skywalker88!'
app.config['MYSQL_DB'] = 'new_schema'

#db=MySQLdb.connector.connect(host="localhost", user="root", password="Skywalker88!",database="new_schema")

mysql = MySQL(app)


# @app.route('/')
# def welcome():
#     return "This is the home page of Flask Application"
 
@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/page2/')
def page2():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM liquors")
    data = cursor.fetchall()
    print (data)
    #return render_template('index.html', data=data)
    return render_template('page2.html', data=data)

@app.route('/addItem/')
def addItem():
    return render_template('addItem.html')

if __name__=='__main__':
    app.run(debug = True)