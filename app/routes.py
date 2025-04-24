from flask import Blueprint
import os

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return "Hello from a real project!"

@main.route('/env')
def show_env():
    return os.getenv("MESSAGE", "No message set")
