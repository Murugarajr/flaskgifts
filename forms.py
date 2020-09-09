from wtforms import Form, StringField, SelectField, validators


class ProdForm(Form):
    media_types = [('Digital', 'Digital'),
                   ('CD', 'CD'),
                   ('Cassette Tape', 'Cassette Tape')
                   ]
    id = StringField('id')
    name = StringField('Name')
    brand = StringField('Brand')
    price = StringField('Price')
    media_type = SelectField('Media', choices=media_types)
