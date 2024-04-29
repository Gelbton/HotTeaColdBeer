from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy data for transportation options
transportation_options = {
    "car": {
        "duration": 3
    },
    "bus": {
        "duration": 5
    },
    "train": {
        "duration": 2
    }
}

# Function to calculate and return route
def return_route(transportation_type, from_city, to_city):
    if transportation_type in transportation_options:
        route = {
            "from": from_city,
            "to": to_city,
            "transportation_type": transportation_type,
            "duration": transportation_options[transportation_type]["duration"]
        }
        return jsonify(route)
    else:
        return jsonify({"error": "Invalid transportation type"}), 400

# Endpoint for getting transportation options
@app.route('/route', methods=['GET'])
def get_route():
    # Get parameters from request
    transportation_type = request.args.get('transportation_type')
    from_city = request.args.get('from_city')
    to_city = request.args.get('to_city')

    # Call function to return route
    return return_route(transportation_type, from_city, to_city)

# Homepage
@app.route('/')
def home():
    return ("Homepage of API")

if __name__ == '__main__':
    app.run(debug=True)
