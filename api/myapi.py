from flask_restx import Api
import hashlib

authorizations = {
    "basicAuth": {
        "type": "basic"
    }
}

# insecure, only for learning purposes public
user_auth = {
    "username": "apiuser",
    "password": "my-key",
    "hashed_password": hashlib.sha256(b"my-key").hexdigest()
}


def authorize(request):
    req_auth = request.authorization
    return req_auth \
           and req_auth.username == user_auth["username"] \
           and hashlib.sha256(req_auth.password.encode()).hexdigest() == user_auth["hashed_password"]


api = Api(version="0.1", title="My Demo API", description="Please modify this API to your needs.",
          authorizations=authorizations)


@api.errorhandler
def std_handler(e):
    return {"message": "An unexpected error has occurred. Please contact the support."}, 500
