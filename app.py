from flask import Flask, render_template, request
from tensorflow.keras import models
from PIL import Image
import numpy as np

app = Flask(__name__)

# Load the Keras model and define class names
model = models.load_model("baseline.keras")
class_names = {
    0: 'airplane',
    1: 'automobile',
    2: 'bird',
    3: 'cat',
    4: 'deer',
    5: 'dog',
    6: 'frog',
    7: 'horse',
    8: 'ship',
    9: 'truck',
}

# Function to predict image
def predict_image(path_to_img):
    img = Image.open(path_to_img)
    img = img.convert("RGB")
    img = img.resize((32, 32))
    data = np.asarray(img)
    data = data / 255
    probs = model.predict(np.array([data])[:1])
    top_probs = probs.max()
    top_pred = class_names[np.argmax(probs)]

    return top_probs, top_pred

@app.route('/', methods=['GET', 'POST'])
def index():
    content = ""
    img_path = "/static/images/placeholder_image.png"
    prob = 0
    pred = ""

    if request.method == 'POST':
        if 'file' in request.files:
            file = request.files['file']
            if file.filename != '':
                img_path = "static/images/" + file.filename
                file.save(img_path)
                prob, pred = predict_image(img_path)
                prob = round(prob * 100)
                pred = "This is a " + pred

    return render_template('index.html', content=content, img_path=img_path, prob=prob, pred=pred)

if __name__ == '__main__':
    app.run(debug=True)
