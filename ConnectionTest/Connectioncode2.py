#Connecting MySQL to Python
from flask import Flask,render_template, request
from flask_mysqldb import MySQL
#


app = Flask(__name__, template_folder='templates', static_folder='static')


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'new_schema'

db=mysql.connector.connect(host="localhost", user="root", password="password",database="new_schema")
#db=mysql.connector.connect(host="localhost", user="root", password="Skywalker88!",database="new_schema")

mysql = MySQL(app)




@app.route('/')
def index():
   #cursor = db.cursor()
   #cursor.execute("SELECT * FROM liquors")
   #data = cursor.fetchall()
   #print (data)
   #return render_template('index.html', data=data)
   return render_template('index.html')

@app.route('/page2.html/')   
def page():
   return render_template('page2.html')

app.run(debug=True)