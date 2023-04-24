# how to use css in python_ flask
# flask render_template example
from flask import Flask,render_template, request, flash, redirect, url_for
from flask_mysqldb import MySQL
import mysql.connector
from mysql import connector    #, request
import json
from flask import jsonify
from flask_cors import CORS, cross_origin

# Provide template folder name
# The default folder name should be "templates" else need to mention custom folder name
app = Flask(__name__)
CORS(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Skywalker88!'
app.config['MYSQL_DB'] = 'new_schema'

db=mysql.connector.connect(host="localhost", user="root", password="Skywalker88!",database="new_schema")

mysql = MySQL(app)

# @app.route('/')
# def welcome():
#     return "This is the home page of Flask Application"
 

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
      inputDetails = request.form
      username = inputDetails['uname']
      password = inputDetails['psw']
      cursor = mysql.connection.cursor()
      cursor.execute("SELECT name FROM user WHERE name ='"+username+"'")
      user = cursor.fetchone()
      print (user)
      if user is not None and len(user) is 1:
         cursor.execute("SELECT password FROM user WHERE password = '"+password+"'")
         pword = cursor.fetchone()
         print (pword)
         if pword is not None and len(pword) is 1:
               return redirect('/beer/')
         elif pword is None:
             return "Incorrect password"
         else:
               return "Incorrect password"
      elif user is None:
          return "Incorrect user"
      else:
         return "Incorrect user"
    else:
        return render_template('index.html')
 
@app.route('/page2/')
def page2():
#    cursor = db.cursor()
#    cursor.execute("SELECT nameFoods, stockFoods FROM foods")
#    data = cursor.fetchall()
#    print(data)
   #return render_template('page2.html', data=data)
   return render_template('page2.html')

@app.route('/search/', methods = ['GET', 'POST'])
def search():
   if request.method == "POST":
    search_query = request.form['searchInput']
    cursor = db.cursor()
    query = """
        SELECT *
        FROM beer 
        JOIN brandy ON beer.brand = brandy.brand 
        JOIN gin ON beer.brand = gin.brand 
        JOIN mezcal ON beer.brand = mezcal.brand 
        JOIN rum ON beer.brand = rum.brand 
        JOIN tequila ON beer.brand = tequila.brand 
        JOIN vodka ON beer.brand = vodka.brand 
        JOIN whiskey ON beer.brand = whiskey.brand 
        JOIN wine ON beer.brand = wine.brand 
        WHERE beer.brand LIKE %s 
        OR brandy.brand LIKE %s 
        OR gin.brand LIKE %s 
        OR mezcal.brand LIKE %s 
        OR rum.brand LIKE %s 
        OR tequila.brand LIKE %s 
        OR vodka.brand LIKE %s 
        OR whiskey.brand LIKE %s 
        OR wine.brand LIKE %s
    """
    cursor.execute(query, (
        '%' + search_query + '%',
        '%' + search_query + '%',
        '%' + search_query + '%',
        '%' + search_query + '%',
        '%' + search_query + '%',
        '%' + search_query + '%',
        '%' + search_query + '%',
        '%' + search_query + '%',
        '%' + search_query + '%'
    ))
    results = cursor.fetchall()
    print (results)
    return render_template('results.html', results=results)
   else:
      cursor = db.cursor()
      cursor.execute("SELECT name, information, address, notes FROM contact")
      data = cursor.fetchall()
      cursor.close()
      return render_template('search.html', data=data)
#@app.route('/EditItem/')
#def EditItem():
 #   return render_template('EditItem.html')


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
    cur1 = db.cursor()
    cur1.execute('SELECT name FROM contact')
    namelist = cur1.fetchall()
    cur1.close()
    
    
    if request.method == "POST":
    
      cursor = mysql.connection.cursor()
      inputDetails = request.form
      column_value = inputDetails['namelist']
      print (column_value)
      column_name = 'name'
      cursor.execute("DELETE FROM {} WHERE {} = %s".format('contact', column_name), (column_value,))
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

@app.route('/winedata')
def get_wine_data():
    cur = mysql.connection.cursor()
    cur.execute("SELECT brand, stock FROM wine")
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

@app.route('/wine/')
def wine():
   cursor = db.cursor()
   cursor.execute("SELECT brand, stock FROM wine")
   data = cursor.fetchall()
   return render_template('tabs/wine.html', data=data)
   #return render_template('tabs/wine.html')

@app.route('/vodkadata')
def get_vodka_data():
    cur = mysql.connection.cursor()
    cur.execute("SELECT brand, stock FROM vodka")
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

@app.route('/vodka/')
def vodka():
   cursor = db.cursor()
   cursor.execute("SELECT brand, stock FROM vodka")
   data = cursor.fetchall()
   return render_template('tabs/vodka.html', data=data)
   #return render_template('tabs/vodka.html')

@app.route('/rumdata')
def get_rum_data():
    cur = mysql.connection.cursor()
    cur.execute("SELECT brand, stock FROM rum")
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

@app.route('/rum/')
def rum():
   cursor = db.cursor()
   cursor.execute("SELECT brand, stock FROM rum")
   data = cursor.fetchall()
   return render_template('tabs/rum.html', data=data)
   #return render_template('tabs/rum.html')

@app.route('/whiskeydata')
def get_whiskey_data():
    cur = mysql.connection.cursor()
    cur.execute("SELECT brand, stock FROM whiskey")
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

@app.route('/whiskey/')
def whiskey():
   cursor = db.cursor()
   cursor.execute("SELECT brand, stock FROM whiskey")
   data = cursor.fetchall()
   return render_template('tabs/whiskey.html', data=data)
   #return render_template('tabs/whiskey.html')

@app.route('/tequiladata')
def get_tequila_data():
    cur = mysql.connection.cursor()
    cur.execute("SELECT brand, stock FROM tequila")
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

@app.route('/tequila/')
def tequila():
   cursor = db.cursor()
   cursor.execute("SELECT brand, stock FROM tequila")
   data = cursor.fetchall()
   return render_template('tabs/tequila.html', data=data)
   #return render_template('tabs/tequila.html')

@app.route('/gindata')
def get_gin_data():
    cur = mysql.connection.cursor()
    cur.execute("SELECT brand, stock FROM gin")
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

@app.route('/gin/')
def gin():
   cursor = db.cursor()
   cursor.execute("SELECT brand, stock FROM gin")
   data = cursor.fetchall()
   return render_template('tabs/gin.html', data=data)
    #return render_template('tabs/gin.html')

@app.route('/brandydata')
def get_brandy_data():
    cur = mysql.connection.cursor()
    cur.execute("SELECT brand, stock FROM brandy")
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

@app.route('/brandy/')
def brandy():
   cursor = db.cursor()
   cursor.execute("SELECT brand, stock FROM brandy")
   data = cursor.fetchall()
   return render_template('tabs/brandy.html', data=data)
   # return render_template('tabs/brandy.html')

@app.route('/mezcaldata')
def get_mezcal_data():
    cur = mysql.connection.cursor()
    cur.execute("SELECT brand, stock FROM mezcal")
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

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
      column_value = request.form.get('brand')
      liquor = request.form.get('table')
      cursor.execute("DELETE FROM {} WHERE {} = %s".format(liquor, column_name), (column_value,))
      print(liquor, column_name, column_value)
      try:
         mysql.connection.commit()

         
         cursor.close()
         return 'Row deleted successfully'
      except:
         return 'There was an error deleting this data'

      

      
    else: 
       return render_template('/rmvItem.html')
    
@app.route('/rmvTable/', methods=['GET', 'POST'])
def Column():
    if request.method == 'POST':
        table = request.form.get('table')
        brand = request.form.get('brand')
        return jsonify(table, brand)
    else:
        cursor = db.cursor()
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        cursor.close()
        return render_template('index.html', tables=tables)
    
@app.route('/brands/<table>')
def get_brands(table):
    cursor = db.cursor()
    cursor.execute(f"SELECT DISTINCT brand FROM {table}")
    brands = cursor.fetchall()
    cursor.close()
    return jsonify(brands)


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
         return render_template('/EditItem.html')
     


      

if __name__=='__main__':
    app.run(debug = True)
    