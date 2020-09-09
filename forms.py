from wtforms import Form, StringField, SelectField, validators


class ProdForm(Form):
    id = StringField('id')
    name = StringField('Name')
    brand = StringField('Brand')
    price = StringField('Price')

