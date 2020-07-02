from flask import Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'My_Super_Secert_Key'
from . import views