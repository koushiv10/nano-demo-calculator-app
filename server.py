from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculator/greeting', methods=['GET'])
def greeting():
    return "Hello world!", 200

@app.route('/calculator/add', methods=['POST'])
def add_numbers():
    data = request.get_json()
    first_number = data['first']
    second_number = data['second']
    
    result = first_number + second_number
    return jsonify({'result': result}), 200

@app.route('/calculator/subtract', methods=['POST'])
def subtract_numbers():
    data = request.get_json()
    first_number = data['first']
    second_number = data['second']
    
    result = first_number - second_number
    return jsonify({'result': result}), 200

if __name__ == '__main__':
    app.run(debug=True)
