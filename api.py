from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

signals = {
    'right' : False,
    'left' : False
}

class GetSignals(Resource):
    def get(self):
        return {
            'right' : signals['right'],
            'left' : signals['left']
        }

class PutSignal(Resource):
    def get(self, signal):
        signals[signal] = not signals[signal]
        return "Pinga"

api.add_resource(GetSignals, '/')
api.add_resource(PutSignal, '/<string:signal>')

if __name__ == '__main__':
    app.run(debug=True, threaded=True)