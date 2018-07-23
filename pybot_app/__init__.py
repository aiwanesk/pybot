from flask import Flask
from config import Config

app = Flask(__name__)
# Get the SECRET_KEY
app.config.from_object(Config)

from pybot_app import views