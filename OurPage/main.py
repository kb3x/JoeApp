# how to use css in python_ flask
# flask render_template example
from flask import Flask,render_template, request, flash, redirect
from flask_mysqldb import MySQL
import mysql.connector
from mysql import connector    #, request

#missing item----------------------------------------------------------

# Provide template folder name
# The default folder name should be "templates" else need to mention custom folder name
app = Flask(__name__)

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'Skywalker88!'
# app.config['MYSQL_DB'] = 'new_schema'

# db=mysql.connector.connect(host="localhost", user="root", password="Skywalker88!",database="new_schema")

mysql = MySQL(app)

# @app.route('/')
# def welcome():
#     return "This is the home page of Flask Application"
 

@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/page2/')
def page2():
#    cursor = db.cursor()
#    cursor.execute("SELECT nameFoods, stockFoods FROM foods")
#    data = cursor.fetchall()
#    print(data)
   #return render_template('page2.html', data=data)
   return render_template('page2.html')

@app.route('/EditItem/')
def EditItem():
    return render_template('EditItem.html')

@app.route('/rmvItem/')
def rmvItem():
    return render_template('rmvItem.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')


#tabs/pages route below---------------------------

@app.route('/beer/')
def beer():
#    cursor = db.cursor()
#    cursor.execute("SELECT brand, stock FROM beer")
#    data = cursor.fetchall()
   #return render_template('tabs/beer.html', data=data)
   return render_template('tabs/beer.html')

@app.route('/wine/')
def wine():
#    cursor = db.cursor()
#    cursor.execute("SELECT brand, stock FROM wine")
#    data = cursor.fetchall()
   #return render_template('tabs/wine.html', data=data)
   return render_template('tabs/wine.html')

@app.route('/vodka/')
def vodka():
#    cursor = db.cursor()
#    cursor.execute("SELECT brand, stock FROM vodka")
#    data = cursor.fetchall()
   #return render_template('tabs/vodka.html', data=data)
   return render_template('tabs/vodka.html')

@app.route('/rum/')
def rum():
#    cursor = db.cursor()
#    cursor.execute("SELECT brand, stock FROM rum")
#    data = cursor.fetchall()
   #return render_template('tabs/rum.html', data=data)
   return render_template('tabs/rum.html')

@app.route('/whiskey/')
def whiskey():
#    cursor = db.cursor()
#    cursor.execute("SELECT brand, stock FROM whiskey")
#    data = cursor.fetchall()
   #return render_template('tabs/whiskey.html', data=data)
   return render_template('tabs/whiskey.html')

@app.route('/tequila/')
def tequila():
#    cursor = db.cursor()
#    cursor.execute("SELECT brand, stock FROM tequila")
#    data = cursor.fetchall()
   #return render_template('tabs/tequila.html', data=data)
   return render_template('tabs/tequila.html')

@app.route('/gin/')
def gin():
#    cursor = db.cursor()
#    cursor.execute("SELECT brand, stock FROM gin")
#    data = cursor.fetchall()
   #return render_template('tabs/gin.html', data=data)
    return render_template('tabs/gin.html')

@app.route('/brandy/')
def brandy():
#    cursor = db.cursor()
#    cursor.execute("SELECT brand, stock FROM brandy")
#    data = cursor.fetchall()
   #return render_template('tabs/brandy.html', data=data)
    return render_template('tabs/brandy.html')

@app.route('/mezcal/')
def mezcal():
#    cursor = db.cursor()
#    cursor.execute("SELECT brand, stock FROM mezcal")
#    data = cursor.fetchall()
   #return render_template('tabs/mezcal.html', data=data)
   return render_template('tabs/mezcal.html')

@app.route('/addItem/', methods=['GET', 'POST'])
def addItem():
   if request.method == "POST":
      inputDetails = request.form
      brand = inputDetails['itemName']
      stock = inputDetails['Quantity']
      liquor = inputDetails['beverage']
      warning = inputDetails['Threshold']
      warningTrigger = 0
      cur = mysql.connection.cursor()
      cur.execute("INSERT INTO beer(brand, stock, warning, warningTrigger) VALUES(%s, %s, %s, %s)", (brand, stock, warning, warningTrigger))
      try:
            mysql.connection.commit()
            cur.close()
            return "Success!"
      except:
            return "There was an error adding the information."
      
   
      
   else: 
      return render_template('/addItem.html')
   
if __name__=='__main__':
    app.run(debug = True)