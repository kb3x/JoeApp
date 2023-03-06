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

if __name__=='__main__':
    app.run(debug = True)