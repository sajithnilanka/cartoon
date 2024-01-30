import cv2
import numpy as np

def pencil_art(image_path, output_path):
    # Read the image
    img = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Invert the grayscale image
    inverted = cv2.bitwise_not(gray)

    # Apply GaussianBlur to the inverted image
    blurred = cv2.GaussianBlur(inverted, (111, 111), 0)

    # Invert the blurred image
    inverted_blurred = cv2.bitwise_not(blurred)

    # Sketch effect: Divide the grayscale image by the inverted blurred image
    sketch = cv2.divide(gray, inverted_blurred, scale=256.0)

    # Save the pencil art image
    cv2.imwrite(output_path, sketch)

    # Display the original and pencil art images
    cv2.imshow("Original", img)
    cv2.imshow("Pencil Art", sketch)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Specify the input and output image filenames
input_image = 'input.jpg'
output_image = 'pencil_art_output.jpg'

# Call the pencil_art function with the input and output image filenames
pencil_art(input_image, output_image)
