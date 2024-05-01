from flask import Flask, request
from graphhopper_api import get_route
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# Endpoint for getting the route data
@app.route('/path', methods=['GET'])
def get_path():
    # Get parameters from request
    transportation_type = request.args.get('transportation_type')
    from_city = request.args.get('from_city')
    to_city = request.args.get('to_city')

    # Call function to return route
    return get_route(transportation_type, from_city, to_city)

# Homepage
@app.route('/')
def home():
    return ("Homepage of API")

if __name__ == '__main__':
    app.run(debug=True)
