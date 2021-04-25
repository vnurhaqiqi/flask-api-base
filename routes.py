from app import app
from flask import request

from services import *

headers = request.headers
payload = request.get_json()
params = request.args


@app.route('/', methods=['GET'])
def index():
    res = service.get_data()

    return res
