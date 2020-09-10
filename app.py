from flask import Flask, render_template, jsonify, request, redirect
from forms import ProdForm
from flask_sqlalchemy import SQLAlchemy
import requests
import json


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mymusic.db'
app.secret_key = "flasktest1"

db = SQLAlchemy(app)
