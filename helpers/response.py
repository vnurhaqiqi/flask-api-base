from flask import jsonify, make_response, Response
import json

RESPONSE = {
    200: "OK", 201: "Created", 400: "Bad Request", 401: "Unauthorized", 403: "Forbidden", 404: "Not Found",
    405: "Method Not Allowed", 408: "Request Timeout", 500: "Internal Server Error", 502: "Bad Gateway"
}


class CustomResponse(Response):
    def __init__(self):
        super().__init__()
        self.status_code = False
        self.message = ""
        self.data_response = {
            'data': [],
            'status_code': False,
            'message': ""
        }

    def set_status(self, code):
        self.status_code = code
        self.data_response['status_code'] = self.status_code
        self.set_message()

    def set_message(self):
        self.message = RESPONSE[self.status_code]
        self.data_response['message'] = self.message

    def set_additional_message(self, message):
        self.message = message
        self.data_response['message'] = self.message

    def set_content(self, content):
        self.data_response['data'] = content

    def get_response(self):
        response = Response(
            response=json.dumps(self.data_response),
            status=self.status_code,
            mimetype='application/json'
        )

        return response
