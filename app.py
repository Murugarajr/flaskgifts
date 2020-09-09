from flask import Flask, render_template, jsonify, request, redirect
from forms import ProdForm
from flask_sqlalchemy import SQLAlchemy
import requests
import json


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mymusic.db'
app.secret_key = "flask rocks!"

db = SQLAlchemy(app)


# @app.route('/index.html')
# def index():
#     return render_template('index.html', the_title='Wedding Gifts')
#
#
# @app.route('/', methods=['GET', 'POST'])
# @app.route('/new_gift.html')
# def new_gift():
#     """
#         Add a new album
#         """
#     form = AlbumForm(request.form)
#
#     if request.method == 'POST' and form.validate():
#         # save the album
#         album = Album()
#         save_changes(album, form, new=True)
#         flash('Album created successfully!')
#         return redirect('/')
#
#     return render_template('new_gift.html', the_title='New Gift')
#
#
# @app.route('/gift_list.html')
# def gift_list():
#     url = "http://127.0.0.1:5000/gift_list.html"
#     data = {'sender': 'Alice', 'receiver': 'Bob', 'message': 'We did it!'}
#     headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
#     r = requests.post(url, data=json.dumps(data), headers=headers)
#     return render_template('gift_list.html', the_title='Gift List')
#
#
# @app.route('/rm_gift.html')
# def rm_gift():
#     return render_template('rm_gift.html', the_title='Remove Gift')
#
#
# @app.route('/buy_gift.html')
# def buy_gift():
#     return render_template('buy_gift.html', the_title='Purchase Gift')
#
#
# @app.route('/report.html')
# def report():
#     return render_template('report.html', the_title='Report')
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
