from flask import Flask, render_template, request
import os
from PIL import Image
import tensorflow as tf
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def process_image():
    if 'image' not in request.files:
        return redirect(request.url)

    image = request.files['image']

    if image.filename == '':
        return redirect(request.url)

    # Save the uploaded image
    image_path = os.path.join('static', 'uploads', image.filename)
    image.save(image_path)

    # Process the image (e.g., resize or apply filters)
    processed_image_path = process_image_logic(image_path)

    return render_template('index.html', input_image=image_path, output_image=processed_image_path)

def process_image_logic(input_path):
    inputImage = tf.io.read_file(input_path)
    inputImage = tf.image.decode_png(inputImage, channels = 3)
    inputImage = tf.image.convert_image_dtype(inputImage, tf.float32)
    inputImage = tf.image.resize(inputImage, (256, 256), method = 'nearest')
    inputImage = tf.expand_dims(inputImage, axis = 0)

    unetModel = tf.keras.models.load_model('unet_semanticSegmentationv3.h5', compile = False)
    unetModel.compile(optimizer = 'adagrad', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])
    
    predictedMask = unetModel.predict(inputImage)
    predictedMask = tf.argmax(predictedMask, axis = -1)
    predictedMask = tf.image.resize(predictedMask, (192, 256), method = 'nearest')
    predictedMask = predictedMask[0]
    #predictedMask = tf.image.grayscale_to_rgb(predictedMask)

    processed_image_path = "static/outputs/processed_" + os.path.basename(input_path)
    plt.imsave(processed_image_path, predictedMask)

    
    return processed_image_path

if __name__ == '__main__':
    app.run(debug=True)
