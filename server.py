from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculator/greeting', methods=['GET'])
def greeting():
    return "Hello world!", 200

@app.route('/calculator/add', methods=['POST'])
def add_numbers():
    data = request.get_json()
    if not data or 'first' not in data or 'second' not in data:
        return jsonify({'error': 'Both first and second numbers are required'}), 400
    
    try:
        first_number = float(data['first'])
        second_number = float(data['second'])
    except ValueError:
        return jsonify({'error': 'Invalid numbers provided'}), 400
    
    result = first_number + second_number
    return jsonify({'result': result}), 200

@app.route('/calculator/subtract', methods=['POST'])
def subtract_numbers():
    data = request.get_json()
    if not data or 'first' not in data or 'second' not in data:
        return jsonify({'error': 'Both first and second numbers are required'}), 400
    
    try:
        first_number = float(data['first'])
        second_number = float(data['second'])
    except ValueError:
        return jsonify({'error': 'Invalid numbers provided'}), 400
    
    result = first_number - second_number
    return jsonify({'result': result}), 200

if __name__ == '__main__':
    app.run(debug=True)
