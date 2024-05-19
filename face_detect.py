import cv2

def set_image_size(image, set_height = None, set_width = None):
    # Calculate the aspect ratio of the original image
    height, width, _ = image.shape
    aspect_ratio = width / height

    if set_height:
        height = set_height
        width = int(height * aspect_ratio)
    elif set_width:
        width = set_width
        height = int(width / aspect_ratio)

    resized_image = cv2.resize(image, (width, height))
    return resized_image , width, height

def detect_image(imagePath,haarCascadePart):
    # Create the haar cascade
    cascPath = "HaarCascadeFiles/"+haarCascadePart+".xml"
    faceCascade = cv2.CascadeClassifier(cascPath)

    # Read the image
    image = cv2.imread(imagePath)
    image, image_width, image_height = set_image_size(image, set_height = 500)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )

    print("Found {0} faces!".format(len(faces)))

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Show Image with detected Faces
    cv2.namedWindow('Faces found', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Faces found', image_width, image_height)
    cv2.imshow("Faces found", image)
    cv2.waitKey(0)

if __name__ == '__main__':
    detect_image('PhotoExample\Example.jpg',"haarcascade_frontalface_default")