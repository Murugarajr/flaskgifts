from app import app
from db_setup import init_db, db_session
from forms import ProdForm
from flask import flash, render_template, request, redirect
from models import Album, Artist
from tables import Results, Buy
import json

init_db()


@app.route('/index.html')
def index():
    return render_template('index.html', the_title='Wedding Gifts')


@app.route('/', methods=['GET', 'POST'])
@app.route('/new_gift.html')
def new_gift():
    """
        Add a new product/gift
        """
    form = ProdForm(request.form)

    if request.method == 'POST' and form.validate():
        # save the album
        album = Album()
        save_changes(album, form, new=True)
        flash('Album created successfully!')
        return redirect('/')

    return render_template('new_gift.html', the_title='New Gift', form=form)


@app.route('/gift_list.html')
def gift_list():
    with open('catalog.json') as json_file:
        results = json.load(json_file)
    table = Results(results)
    table.border = True
    return render_template('gift_list.html', the_title='Gift List', table=table)


def save_changes(album, form, new=False):
    """
    Save the changes to the database
    """
    # Get data from form and assign it to the correct attributes
    # of the SQLAlchemy table object
    artist = Artist()
    artist.name = form.artist.data

    album.artist = artist
    album.title = form.title.data
    album.release_date = form.release_date.data
    album.publisher = form.publisher.data
    album.media_type = form.media_type.data

    if new:
        # Add the new album to the database
        db_session.add(album)

    # commit the data to the database
    db_session.commit()


@app.route('/rm_gift.html')
def rm_gift():
    """
    remove gift items
    :return: return gift table
    """
    return render_template('rm_gift.html', the_title='Remove Gift')


@app.route('/buy_gift.html')
def buy_gift():
    with open('catalog.json') as json_file:
        results = json.load(json_file)
    table = Results(results)
    table.border = True
    return render_template('buy_gift.html', the_title='Purchase Gift', table=table)


@app.route('/report.html')
def report():
    with open('catalog.json') as json_file:
        results = json.load(json_file)
    table = Results(results)
    table.border = True
    return render_template('report.html', the_title='Report', table=table)


if __name__ == '__main__':
    app.run(debug=True)
