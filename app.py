from flask import Flask, render_template, request, redirect, url_for, Response
from transfer import trans_model
from image_process import preprocess_image, postprocess_image
import pandas as pd
import numpy as np
import os
from PIL import Image
import base64
import re
from io import BytesIO
import datetime

UPLOAD_FOLDER = './static/images'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
IMAGE_SIZE = (512, 512)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html', result=False)

@app.route('/', methods=['POST'])
def upload_file():
    
    # !! lack: handle errer, post before update image 
    uploaded_file = request.files['file']
    complete_fname = uploaded_file.filename

    if complete_fname != '':
        file_name = complete_fname.split(".")[0]
        path = os.path.join(app.config['UPLOAD_FOLDER'],complete_fname)
   
    else:
        camera_b64 = request.form['camera']
        camera_data = re.sub('^data:image/.+;base64,', '', camera_b64)

        uploaded_file = Image.open(BytesIO(base64.b64decode(camera_data))) #PIL file
        current_time = datetime.datetime.now()
        
        file_name = f'camera-{current_time}'
        complete_fname = f'{file_name}.jpeg'
        path = os.path.join(app.config['UPLOAD_FOLDER'], complete_fname)

    uploaded_file.save(path)
    image = preprocess_image(path, IMAGE_SIZE)
    output = trans_model(image)
    postprocess_image(output, file_name)
    return render_template('index.html', resource = f'images/{complete_fname}', result = f'images/{file_name}-tranfered.jpeg') 

if __name__=='__main__':
    app.run(port=5000,debug=True)