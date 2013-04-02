from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    #request.headers.add('Access-Control-Allow-Origin', '*')
    #raise
    return render_template('index.html')

@app.route('/json', methods=['POST', 'GET'])
def return_json():
	return jsonify({'msg': 'Python'})


@app.after_request
def inject_header(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


app.run('0.0.0.0', port=8888, debug=True)
