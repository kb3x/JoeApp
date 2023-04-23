# how to use css in python_ flask
# flask render_template example
from flask import Flask,render_template, request, flash, redirect
from flask_mysqldb import MySQL
import mysql.connector
from mysql import connector    #, request
import json
from flask import jsonify

# Provide template folder name
# The default folder name should be "templates" else need to mention custom folder name
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'ThaoDuong*6'
app.config['MYSQL_DB'] = 'new_schema'

db=mysql.connector.connect(host="localhost", user="root", password="ThaoDuong*6",database="new_schema")

# sqlConnect = mysql.connect()

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

#@app.route('/EditItem/')
#def EditItem():
 #   return render_template('EditItem.html')

@app.route('/search/')
def search():
   cursor = db.cursor()
   cursor.execute("SELECT name, information, address, notes FROM contact")
   data = cursor.fetchall()
   cursor.close()
   return render_template('search.html', data=data)

@app.route('/searchResults/')
def searchResults():
   cursor = db.cursor()
   cursor.execute("SELECT name, information, address, notes FROM contact")
   data = cursor.fetchall()
   cursor.close()
   return render_template('searchResults.html', data=data)



@app.route('/contact/')
def contact():
   cursor = db.cursor()
   cursor.execute("SELECT name, information, address, notes FROM contact")
   data = cursor.fetchall()
   cursor.close()
   return render_template('contact.html', data=data)

@app.route('/contactdata')
def get_contact_data():
    cur = mysql.connection.cursor()
    cur.execute("SELECT name, information, address, notes FROM contact")
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

@app.route('/addContact/', methods=['GET', 'POST'])
def addContact():
    if request.method == "POST":
      inputDetails = request.form
      number = inputDetails['phoneNum']
      name = inputDetails['SupplierName']
      address = inputDetails['address']
      notes = inputDetails['notes']
      cur = mysql.connection.cursor()
      cur.execute(f"INSERT INTO contact(information, name, address, notes) VALUES(%s, %s, %s, %s)", (number, name, address, notes))
      try:
            mysql.connection.commit()
            cur.close()
            return "Success!"
      except:
            return "There was an error adding the information."
    else:
          return render_template('addContact.html')

@app.route('/rmvContact/', methods=['GET', 'POST'])
def rmvContact():
    dropdownCur = db.cursor()
    dropdownCur.execute('SELECT name FROM contact')
    namelist = dropdownCur.fetchall()
    dropdownCur.close()
    
    
    if request.method == "POST":
    
      cursor = mysql.connection.cursor()
      inputDetails = request.form
      column_value = inputDetails['contactName']
      column_name = 'name'
      cursor.execute("DELETE FROM {} WHERE {} = %s".format(contact, column_name), (column_value,))
      try:
         mysql.connection.commit()

         
         cursor.close()
         return 'Row deleted successfully'
      except:
         return 'There was an error deleting this data'
         
    else:
      return render_template('rmvContact.html', namelist=namelist)


#tabs/pages route below---------------------------
@app.route('/beerdata')
def get_beer_data():
    cur = mysql.connection.cursor()
    cur.execute("SELECT brand, stock FROM beer")
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

@app.route('/beer/')
def beer():
   cursor = db.cursor()
   cursor.execute("SELECT brand, stock FROM beer")
   data = cursor.fetchall()
   return render_template('tabs/beer.html', data=data)
   #return render_template('tabs/beer.html')

@app.route('/wine/')
def wine():
   cursor = db.cursor()
   cursor.execute("SELECT brand, stock FROM wine")
   data = cursor.fetchall()
   return render_template('tabs/wine.html', data=data)
   #return render_template('tabs/wine.html')

@app.route('/vodka/')
def vodka():
   cursor = db.cursor()
   cursor.execute("SELECT brand, stock FROM vodka")
   data = cursor.fetchall()
   return render_template('tabs/vodka.html', data=data)
   #return render_template('tabs/vodka.html')

@app.route('/rum/')
def rum():
   cursor = db.cursor()
   cursor.execute("SELECT brand, stock FROM rum")
   data = cursor.fetchall()
   return render_template('tabs/rum.html', data=data)
   #return render_template('tabs/rum.html')

@app.route('/whiskey/')
def whiskey():
   cursor = db.cursor()
   cursor.execute("SELECT brand, stock FROM whiskey")
   data = cursor.fetchall()
   return render_template('tabs/whiskey.html', data=data)
   #return render_template('tabs/whiskey.html')

@app.route('/tequila/')
def tequila():
   cursor = db.cursor()
   cursor.execute("SELECT brand, stock FROM tequila")
   data = cursor.fetchall()
   return render_template('tabs/tequila.html', data=data)
   #return render_template('tabs/tequila.html')

@app.route('/gin/')
def gin():
   cursor = db.cursor()
   cursor.execute("SELECT brand, stock FROM gin")
   data = cursor.fetchall()
   return render_template('tabs/gin.html', data=data)
    #return render_template('tabs/gin.html')

@app.route('/brandy/')
def brandy():
   cursor = db.cursor()
   cursor.execute("SELECT brand, stock FROM brandy")
   data = cursor.fetchall()
   return render_template('tabs/brandy.html', data=data)
   # return render_template('tabs/brandy.html')

@app.route('/mezcal/')
def mezcal():
   cursor = db.cursor()
   cursor.execute("SELECT brand, stock FROM mezcal")
   data = cursor.fetchall()
   return render_template('tabs/mezcal.html', data=data)
   #return render_template('tabs/mezcal.html')

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


# @app.route('/EditItem/', methods=['POST', 'GET'])
# def EditItem():
#     if request.method == "POST":

#        cursor = mysql.connection.cursor()

      
#        column_name = 'brand'
#        column2_name = 'stock'
#        column_value = request.form.get('itemName')
#        column2_value = request.form.get('itemUnits')
#        liquor = request.form.get('beverage2')
#        input = request.form.get('beverage3')
#        input2 = request.form.get('itemUnits')
#        input3 = request.form.get('thresholdAmount')
#        query = """
#          SELECT TABLE_NAME
#          FROM INFORMATION_SCHEMA.COLUMNS
#          WHERE COLUMN_NAME = 'brand'
#          AND TABLE_SCHEMA = 'new_schema'
#          AND TABLE_NAME IN (
#             SELECT TABLE_NAME
#             FROM INFORMATION_SCHEMA.TABLES
#             WHERE TABLE_TYPE = 'BASE TABLE'
#             AND TABLE_SCHEMA = 'new_schema'
#          )
#          AND EXISTS (
#             SELECT *
#               FROM (
#                     SELECT brand
#                     FROM new_schema.beer
#                     UNION ALL
#                     SELECT brand
#                     FROM new_schema.brandy
#                     UNION ALL
#                     SELECT brand
#                     FROM new_schema.gin
#                     UNION ALL
#                     SELECT brand
#                     FROM new_schema.mezcal
#                     UNION ALL
#                     SELECT brand
#                     FROM new_schema.rum
#                     UNION ALL
#                     SELECT brand
#                     FROM new_schema.tequila
#                     UNION ALL
#                     SELECT brand
#                     FROM new_schema.vodka
#                     UNION ALL
#                     SELECT brand
#                     FROM new_schema.wine
#                     UNION ALL
#                     SELECT brand
#                     FROM new_schema.whiskey
#                 ) as t
#                 WHERE brand = '{testin}'
#             )
#         """

#        cursor.execute(query)
#        result = cursor.fetchone()[0]
#        print(result)
#        cursor.execute("UPDATE {} SET brand = %s WHERE brand = %s".format(result), (input, liquor))
#        cursor.execute("UPDATE {} SET stock = %s WHERE brand = %s".format(result), (column2_value, liquor))
#        cursor.execute("UPDATE {} SET warning = %s WHERE brand = %s".format(result), (input3, liquor))
#        try:
#           mysql.connection.commit()

         
#           cursor.close()
#           return 'Data successfully edited.'
#        except:
#          return 'There was an error editing this data'
#     else:
#        return render_template('/EditItem.html')
   

@app.route('/EditItem/', methods=['POST', 'GET'])
def EditItem():
     dropdownCur = db.cursor()
     dropdownCur.execute('SELECT brand FROM beer')
     drinknamelist = dropdownCur.fetchall()
     dropdownCur.close()

     if request.method == "POST":

        cursor = mysql.connection.cursor()

        liquor = request.form.get('beverage')
        brand = request.form.get('beverage2')
        input = request.form.get('beverage3')
        input2 = request.form.get('itemUnits')
        input3 = request.form.get('thresholdAmount')
        cursor.execute("UPDATE {} SET brand = %s WHERE brand = %s".format(liquor), (input, brand))
        cursor.execute("UPDATE {} SET stock = %s WHERE brand = %s".format(liquor), (input2, input))
        cursor.execute("UPDATE {} SET warning = %s WHERE brand = %s".format(liquor), (input3, input))
        try:
           mysql.connection.commit()

         
           cursor.close()
           return 'Data successfully edited.'
        except:
          return 'There was an error editing this data'

     else:
         return render_template('/EditItem.html', drinknamelist=drinknamelist)

      

if __name__=='__main__':
    app.run(debug = True)