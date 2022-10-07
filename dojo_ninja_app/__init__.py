from flask import Flask
from dojo_ninja_app.model.ninja import Ninja
from dojo_ninja_app.model.dojo import Dojo 
app = Flask(__name__)
app.secret_key = "MAKE IT MAKE SENSE"