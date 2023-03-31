from flask import Blueprint

bp = Blueprint('forum', __name__)

@bp.route('/')
def home():
	return '<h1>You did it!</h1>'