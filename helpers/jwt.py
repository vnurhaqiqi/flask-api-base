import jwt

JWT_KEY = "this-is-jwt-key"


class PythonJWT:
    def encode_token(self, payload):
        return jwt.encode(payload, JWT_KEY, algorithm='HS256')

    def decode_token(self, payload):
        if payload:
            try:
                return jwt.decode(payload, JWT_KEY, algorithm='HS256')
            except Exception as e:
                return False
        else:
            return False
