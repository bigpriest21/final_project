from flask import Flask
from config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)

app.config['246810aeiou'] = os.environ.get("246810aeiou")


from app.routes import *