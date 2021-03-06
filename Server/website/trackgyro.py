import os
from flask import Flask, request
from werkzeug.utils import secure_filename
import time

app = Flask(__name__)

import pickle, time
@app.route('/upload', methods=["POST"])
def upload():
    pickle.dump(request.get_json(), open("uploads/" + str(time.time()), "wb"))
    return ""

@app.route('/imageupload/<float:name>', methods=['POST'])
def imageupload(name):
	filename = secure_filename(str(name) + ".png")
	out = open(os.path.join("image_uploads", filename), "wb")
	out.write(request.data)
	out.close()
	return ''

@app.route('/time')
def time_():
	return str(time.time())

app.run(host='0.0.0.0', port=80)
