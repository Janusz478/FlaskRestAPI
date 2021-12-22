from flask_restx import Api

api = Api(version="0.1", title="My Demo API", description="Please modify this API to your needs.")

@api.errorhandler
def std_handler(e):
    return {"message": "An unexpected error has occurred. Please contact the support."}, 500
