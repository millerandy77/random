from back import random_int_generator
from flask import Flask
from flask_cors import CORS


# instantiate the app
application = Flask(__name__)

# enable CORS
CORS(application, resources={r'/*': {'origins': '*'}})

# sanity check route
@application.route('/', methods=['GET'])
def get_random_int():
    return str(random_int_generator())

if __name__ == '__main__':
    application.run(port=8000)
