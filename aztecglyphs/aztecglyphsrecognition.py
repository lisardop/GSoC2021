"""Modify from original file located at
    https://colab.research.google.com/drive/1rUA51e5Wz-VxsuNOXkfwIcD8PPasXMAG
"""

import os
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template, session, json, jsonify
from werkzeug.utils import secure_filename
from flask_executor import Executor
from flask_socketio import SocketIO, emit

import tensorflow.keras
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.imagenet_utils import decode_predictions, preprocess_input
from tensorflow.keras.models import Model  
import numpy as np
import tensorflow as tf
from scipy.spatial import distance
import time

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif', 'tiff'])
UPLOAD_FOLDER = 'static/uploads/'

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['SECRET_KEY'] = 'mySecretKey'

executor = Executor(app)
socketio = SocketIO(app)
base_models = tf.keras.applications.MobileNet()
features = []
images_website = []
feat_extractor = Model(inputs=base_models.input, outputs=base_models.get_layer("reshape_2").output)

@app.route('/')
def index():
	return home()

@app.route('/', methods=['POST'])
def upload_image():
	clientId = request.form.get('client_id')
	
	files = request.files.getlist("file")
		
	meta = json.loads(request.form.get('meta'))
	
	for file in files:
		imageId = meta[file.filename]
		filename = secure_filename(file.filename)
		imagePath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
		file.save(imagePath)
		executor.submit(analyze_image, imagePath, file.filename, clientId, imageId)
	return render_template('blank.html')

def home():
	return render_template('aztecglyphrecognition.html')
	
def extract_features():
	images_path = 'static/samples/'
	image_extensions = ['.jpg', '.png', '.jpeg', '.gif', '.tiff']
	max_num_images = 10000
	images = [os.path.join(dp, f) for dp, dn, filenames in os.walk(images_path) for f in filenames if os.path.splitext(f)[1].lower() in image_extensions]
	images_website.clear()
	images_website.extend([os.path.join(images_path, f) for dp, dn, filenames in os.walk(images_path) for f in filenames if os.path.splitext(f)[1].lower() in image_extensions])
	if max_num_images < len(images):
		images = [images[i] for i in sorted(random.sample(xrange(len(images)), max_num_images))]
	
	print("keeping %d images to analyze" % len(images))
	tic = time.time()
	features.clear()
	for i, image_path in enumerate(images):
		if i % 500 == 0:
			toc = time.time()
			elap = toc-tic;
			print("analyzing image %d / %d. Time: %4.4f seconds." % (i, len(images),elap))
			tic = time.time()
		img, x = load_image(image_path);
		feat = feat_extractor.predict(x)[0]
		features.append(feat)

	print('finished extracting features for %d images' % len(images))
	
def analyze_image(imagePath, originalFileName, clientId, imageId):
	print("analyzing image: %s!" % (imagePath))
	img, x = load_image(imagePath)
	imga = feat_extractor.predict(x)[0]
	results = get_closest_images(imga, 5)
	payload = dict()
	payload['results'] = []
	payload['image_id'] = imageId
	for idx in results:
		payload['results'].append(images_website[idx])

	socketio.emit(clientId, json.dumps(payload))

def load_image(path):
	img = image.load_img(path, target_size=base_models.input_shape[1:3])
	x = image.img_to_array(img)
	x = np.expand_dims(x, axis=0)
	x = preprocess_input(x)
	return img, x

def get_closest_images(imga, num_results=5):
	distances = [ distance.cosine(imga, feat) for feat in features ]
	idx_closest = sorted(range(len(distances)), key=lambda k: distances[k])[1:num_results+1]
	return idx_closest

extract_features()

