# how to use css in python_ flask
# flask render_template example
from flask import Flask,render_template, request, flash, redirect
from flask_mysqldb import MySQL
import mysql.connector
from mysql import connector    #, request
from flask_caching import Cache
import json
from flask import jsonify
#missing item----------------------------------------------------------

# Provide template folder name
# The default folder name should be "templates" else need to mention custom folder name
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Skywalker88!'
app.config['MYSQL_DB'] = 'new_schema'

db=mysql.connector.connect(host="localhost", user="root", password="Skywalker88!",database="new_schema")

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
   cursor.execute("SELECT nameFoods, stockFoods FROM foods")
   data = cursor.fetchall()
   print(data)
   return render_template('page2.html', data=data)

@app.route('/contact/')
def contact():
    return render_template('contact.html')


#tabs/pages route below---------------------------
@app.route('/beerdata')
def get_beer_data():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM beer ")
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

@app.route('/beer/')
def beer():
   cursor = db.cursor()
   cursor.execute("SELECT brand, stock FROM beer")
   data = cursor.fetchall()
   cursor.close()
   return render_template('tabs/beer.html', data=data)

@app.route('/winedata')
def get_wine_data():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM wine ")
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

@app.route('/wine/')
def wine():
   cursor = db.cursor()
   cursor.execute("SELECT brand, stock FROM wine")
   data = cursor.fetchall()
   return render_template('tabs/wine.html', data=data)

@app.route('/vodkadata')
def get_vodka_data():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM vodka ")
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

@app.route('/vodka/')
def vodka():
   cursor = db.cursor()
   cursor.execute("SELECT brand, stock FROM vodka")
   data = cursor.fetchall()
   return render_template('tabs/vodka.html', data=data)

@app.route('/rumdata')
def get_rum_data():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM rum ")
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

@app.route('/rum/')
def rum():
   cursor = db.cursor()
   cursor.execute("SELECT brand, stock FROM rum")
   data = cursor.fetchall()
   return render_template('tabs/rum.html', data=data)

@app.route('/whiskeydata')
def get_whiskey_data():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM whiskey ")
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

@app.route('/whiskey/')
def whiskey():
   cursor = db.cursor()
   cursor.execute("SELECT brand, stock FROM whiskey")
   data = cursor.fetchall()
   return render_template('tabs/whiskey.html', data=data)

@app.route('/tequiladata')
def get_tequila_data():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM tequila ")
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

@app.route('/tequila/')
def tequila():
   cursor = db.cursor()
   cursor.execute("SELECT brand, stock FROM tequila")
   data = cursor.fetchall()
   return render_template('tabs/tequila.html', data=data)

@app.route('/gindata')
def get_gin_data():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM gin ")
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

@app.route('/gin/')
def gin():
   cursor = db.cursor()
   cursor.execute("SELECT brand, stock FROM gin")
   data = cursor.fetchall()
   return render_template('tabs/gin.html', data=data)

@app.route('/brandydata')
def get_brandy_data():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM brandy ")
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

@app.route('/brandy/')
def brandy():
   cursor = db.cursor()
   cursor.execute("SELECT brand, stock FROM brandy")
   data = cursor.fetchall()
   return render_template('tabs/brandy.html', data=data)

@app.route('/mezcaldata')
def get_mezcal_data():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM mezcal ")
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

@app.route('/mezcal/')
def mezcal():
   cursor = db.cursor()
   cursor.execute("SELECT brand, stock FROM mezcal")
   data = cursor.fetchall()
   return render_template('tabs/mezcal.html', data=data)


@app.route('/addItem/', methods=['GET', 'POST'])
def addItem():
   if request.method == "POST":
      dict = {'beer':'beer', 'vodka':'vodka', 'mezcal':'mezcal', 'brandy':'brandy', 'gin':'gin', 'tequila':'tequila', 'whiskey':'whiskey', 'rum':'rum', 'wine':'wine'}
      inputDetails = request.form
      brand = inputDetails['itemName']
      stock = inputDetails['Quantity']
      liquor = inputDetails['beverage']
      warning = inputDetails['Threshold']
      warningTrigger = 0
      cur = mysql.connection.cursor()
      cur.execute(f"INSERT INTO {dict[liquor]}(brand, stock, warning, warningTrigger) VALUES(%s, %s, %s, %s)", (brand, stock, warning, warningTrigger))
      try:
            mysql.connection.commit()
            cur.close()
            return "Success!"
      except:
            return "There was an error adding the information."
      
   
      
   else: 
      return render_template('/addItem.html')
   
@app.route('/rmvItem', methods=['GET'])  
def rmvItemPage():
    return render_template('/rmvItem.html') 

@app.route('/rmvItem/', methods=['POST', 'GET'])
def rmvItem():
    if request.method == "POST":
    
      cursor = mysql.connection.cursor()

      
      column_name = 'brand'
      column_value = request.form.get('itemName')
      liquor = request.form.get('beverage')
      cursor.execute("DELETE FROM {} WHERE {} = %s".format(liquor, column_name), (column_value,))
      try:
         mysql.connection.commit()

         
         cursor.close()
         return 'Row deleted successfully'
      except:
         return 'There was an error deleting this data'

      

      
    else: 
       return render_template('/rmvItem.html')


@app.route('/EditItem/', methods=['POST', 'GET'])
def EditItem():
   if request.method == "POST":

      cursor = mysql.connection.cursor()

      
      column_name = 'brand'
      column_value = request.form.get('itemName')
      liquor = request.form.get('beverage')
      input = request.form.get('userInput')
      cursor.execute("UPDATE {} SET {} WHERE {} = %s".format(liquor, input, column_name), (column_value,))
      try:
         mysql.connection.commit()

         
         cursor.close()
         return 'Data successfully edited.'
      except:
         return 'There was an error editing this data'
   else:
      return render_template('/EditItem.html')
   

      
   

if __name__=='__main__':
    app.run(debug = True)