from flask import Flask, render_template
from flask_restplus import Resource, Api
import sys
from flask import request

from get_distance import calculate_distance
from get_emissions import calculate_emissions
url = "https://distanceto.p.rapidapi.com/get"


app = Flask(__name__)
api = Api(app)


@api.route('/calculate')
class EmissionsCalculator(Resource):
    def get(self):
        origin = request.args.get('origin')
        destination = request.args.get('dest')
        mass = request.args.get('cargo')
        mode = request.args.get('mode')
        dist = calculate_distance(origin, destination)
        emissions = calculate_emissions(dist, mode, mass)
        print('Hello world! '+emissions, file=sys.stderr)
        return emissions


if __name__ == '__main__':
    app.run(debug=True)
