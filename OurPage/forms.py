# forms.py
from wtforms import Form, StringField, SelectField
class BrandForm(Form):
    brandWhiskey = StringField('Brand')
    stockWhiskey = intField('Stock')
    whiskeyWarning = intField('Warning')