# Face Detection with OpenCV

This Python script uses OpenCV to detect faces in an image using Haar cascades.

## Requirements

* Python 3.x
* OpenCV

## Installation

To install OpenCV, you can use the following command:

###  pip install opencv-python


## Usage

To use the script, simply run it with the path to the image file and the name of the Haar cascade file as arguments:

python detect_image.py <image_path> <haar_cascade_name>

### For example:

`python detect_image.py PhotoExample\Example.jpg haarcascade_frontalface_default
`


The script will display the image with rectangles drawn around the detected faces.

## Code

The main function in the script is `detect_image()`, which takes two arguments: the path to the image file and the name of the Haar cascade file.

The script first creates a `cv2.CascadeClassifier` object using the Haar cascade file. It then reads the image file and converts it to grayscale.

The `detectMultiScale()` function is called on the grayscale image to detect faces. The function returns a list of rectangles that enclose the detected faces.

The script then draws rectangles around the detected faces using the `cv2.rectangle()` function.

Finally, the image is displayed using the `cv2.imshow()` function.

## Haar Cascades

The script uses Haar cascades to detect faces. Haar cascades are a type of machine learning algorithm that can be trained to recognize specific features in images.

The script includes a Haar cascade file for detecting frontal faces, which is located in the `HaarCascadeFiles` directory. You can add more Haar cascade files to the directory to detect other features, such as eyes or mouths. More `HaarCascadeFiles` can be found here https://github.com/opencv/opencv/tree/master/data/haarcascades