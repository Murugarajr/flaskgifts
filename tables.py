from flask_table import Table, Col, LinkCol


class Results(Table):
    id = Col('Id', show=False)
    name = Col('Name')
    brand = Col('Brand')
    price = Col('Price')
    in_stock_quantity = Col('In_stock_quantity')
    # media_type = Col('Media')
    # edit = LinkCol('Edit', 'edit', url_kwargs=dict(id='id'))


class Buy(Table):
    id = Col('Id', show=False)
    name = Col('Name')
    brand = Col('Brand')
    price = Col('Price')
    in_stock_quantity = Col('In_stock_quantity')
    buy_now = Col('yes')
