from models import *
from helpers import response

response_obj = response.CustomResponse()


def get_data():
    response_obj.set_status(200)
    response_obj.set_content("Hello World")

    return response_obj.get_response()
