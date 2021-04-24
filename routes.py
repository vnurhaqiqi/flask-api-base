from app import app
from flask import request

from services import *


@app.route('/', methods=['GET'])
def index():
    res = service.get_data()

    return res
