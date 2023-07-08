from flask import Flask, request, jsonify


app = Flask(__name__)


# List to store the posted data
posted_data = []

@app.route('/', methods=['GET'])
def get_data():
    # Perform any necessary logic to retrieve data
    data = {'message': 'This is a GET request'}
    return jsonify(data)

@app.route('/post_data', methods=['POST'])
def post_data():
    # Retrieve data from the request body
    data = request.get_json()

    # Perform any necessary logic with the data
    # ...

    # Append the posted data to the list
    posted_data.append(data)

    # Return a response
    response = {'message': 'This is a POST request', 'data': data}
    return jsonify(response)

@app.route('/all_posted_data', methods=['GET'])
def all_posted_data():
    return jsonify(posted_data)

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
