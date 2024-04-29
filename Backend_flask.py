from flask import Flask, request, jsonify
import geocoding

app = Flask(__name__)

# Endpoint for getting the route data
@app.route('/route', methods=['GET'])
def get_route():
    # Get parameters from request
    transportation_type = request.args.get('transportation_type')
    from_city = request.args.get('from_city')
    to_city = request.args.get('to_city')

    # Call function to return route
    return geocoding(transportation_type, from_city, to_city)

# Homepage
@app.route('/')
def home():
    return ("Homepage of API")

if __name__ == '__main__':
    app.run(debug=True)
