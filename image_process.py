import numpy as np
from PIL import Image
import time
import matplotlib.pyplot as plt
from pathlib import Path
from io import BytesIO

FILE_NAME = ""

def preprocess_image(image_path, image_size):
    """
    take the path of uploaded image and return the data ready fot tranfer model (4D) 
    """
    ## ! check if image has only one channel
    image = Image.open(image_path)
    image = image.resize(image_size)
    image = np.asarray(image, dtype="float16")
    image = image / 255.
    image = np.expand_dims(image, axis=0)
    return image

def postprocess_image(output_image, file_name):
    """
    take result of model(4D) and return file path 
    """
    output_image = output_image[0]
    output_image = output_image.numpy()
    output_image = output_image.astype(np.uint8)
    output_image = Image.fromarray(output_image)
    output_image = output_image.convert('L')
    output_path = f'./static/images/{file_name}-tranfered.jpeg'
    output_image.save(output_path)
    return output_path



