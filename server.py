from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculator/greeting', methods=['GET'])
def greeting():
    return "Hello world!", 200

@app.route('/calculator/add', methods=['POST'])
def add():
    data = request.get_json()
    if 'first' in data and 'second' in data:
        first = data['first']
        second = data['second']
        result = first + second
        return jsonify({'result': result}), 200
    else:
        return "Bad Request", 400

@app.route('/calculator/subtract', methods=['POST'])
def subtract():
    data = request.get_json()
    if 'first' in data and 'second' in data:
        first = data['first']
        second = data['second']
        result = first - second
        return jsonify({'result': result}), 200
    else:
        return "Bad Request", 400

if __name__ == '__main__':
    app.run(debug=True)
