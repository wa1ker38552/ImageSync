from flask import render_template
from flask import send_file
from flask import request
from flask import Flask
from PIL import Image
import base64
import io

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/sync')
def sync():
  return send_file('static/image.png', mimetype='image/png')

@app.route('/upload', methods=['POST'])
def upload():
  encoded = request.json['image']
  bytes = base64.b64decode(encoded.encode('utf-8'))
  Image.open(io.BytesIO(bytes)).save('static/image.png')
  return {'success': True}
  

app.run(host='0.0.0.0', port=8080)
