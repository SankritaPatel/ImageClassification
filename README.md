# Image Classifier GUI

This is a simple graphical user interface (GUI) for classifying images using a pre-trained convolutional neural network (CNN) model. The GUI allows users to select an image file from their file system and provides predictions on the content of the image.

## Dataset Information

The model used in this project is trained on the CIFAR-10 dataset. CIFAR-10 is a well-known dataset commonly used for image classification tasks. It consists of 60,000 32x32 color images in 10 classes, with 6,000 images per class. The classes are as follows:

1. Airplane
2. Automobile
3. Bird
4. Cat
5. Deer
6. Dog
7. Frog
8. Horse
9. Ship
10. Truck

The dataset is divided into 50,000 training images and 10,000 test images.

## Requirements

- Python 3.x
- TensorFlow
- PIL (Python Imaging Library)
- Taipy library for GUI
- Image files for testing

## Installation

1. Install Python 3.x from [Python's official website](https://www.python.org/).
2. Install required dependencies using pip:

    ```
    pip install -r requirements.txt
    ```

3. Ensure you have some sample images for testing placed in the project directory.

## Usage

1. Run the `main.py` script.
2. The GUI window will open.
3. Use the file selector to choose an image from your file system.
4. The GUI will display the selected image and provide a prediction on its content.
5. The prediction will be shown along with the probability of the prediction.

## Screenshots
![wireframe](https://github.com/SankritaPatel/ImageClassification/assets/161813782/9968ef3b-7f33-4648-a02d-1a620f049634)
![Result1](https://github.com/SankritaPatel/ImageClassification/assets/161813782/f4315cec-d8ea-46bc-ab43-870115bad3d8)



## Credits

- The GUI is built using the Taipy library.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
