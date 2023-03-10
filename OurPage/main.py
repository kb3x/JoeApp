# how to use css in python_ flask
# flask render_template example
 
from flask import Flask, render_template    #, request
#missing item----------------------------------------------------------

# Provide template folder name
# The default folder name should be "templates" else need to mention custom folder name
app = Flask(__name__)


# @app.route('/')
# def welcome():
#     return "This is the home page of Flask Application"
 
@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/page2/')
def page2():
    return render_template('page2.html')

@app.route('/addItem/')
def addItem():
    return render_template('addItem.html')

@app.route('/EditItem/')
def EditItem():
    return render_template('EditItem.html')


#tabs/pages route below---------------------------

@app.route('/beer/')
def beer():
    return render_template('tabs/beer.html')

@app.route('/wine/')
def wine():
    return render_template('tabs/wine.html')

@app.route('/vodka/')
def vodka():
    return render_template('tabs/vodka.html')

@app.route('/rum/')
def rum():
    return render_template('tabs/rum.html')

@app.route('/whiskey/')
def whiskey():
    return render_template('tabs/whiskey.html')

@app.route('/tequila/')
def tequila():
    return render_template('tabs/tequila.html')

@app.route('/gin/')
def gin():
    return render_template('tabs/gin.html')

@app.route('/brandy/')
def brandy():
    return render_template('tabs/brandy.html')

@app.route('/mezcal/')
def mezcal():
    return render_template('tabs/mezcal.html')


if __name__=='__main__':
    app.run(debug = True)