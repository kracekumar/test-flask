from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/json', methods=['POST', 'GET'])
def return_json():
	return jsonify({'msg': 'Python'})

app.run('0.0.0.0', port=8888, debug=True)

