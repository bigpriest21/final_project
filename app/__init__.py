from flask import Flask
from config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)

app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")


from app.routes import *