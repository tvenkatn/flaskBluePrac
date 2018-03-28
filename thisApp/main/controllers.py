from flask import Blueprint

main = Blueprint('main', __name__)

main.route('/abc')
def index():
	return "Main page"
