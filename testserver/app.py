from flask import Flask
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

@app.route("/")
def helloworld():
    return "HelloWorld"

class testMethod(Resource):
    def get(self):
        return {'id': 30}

api.add_resource(testMethod, '/test')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
