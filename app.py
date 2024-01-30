import cv2
import numpy as np

def cartoonize(input_path, output_path):
    # Read the input image
    img = cv2.imread(input_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply median blur to reduce noise
    gray = cv2.medianBlur(gray, 5)

    # Detect edges using adaptive thresholding
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

    # Apply bilateral filter to smooth out colors while preserving edges
    color = cv2.bilateralFilter(img, 9, 300, 300)

    # Combine the edges and smoothed color image
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    # Save the cartoonized image
    cv2.imwrite(output_path, cartoon)

    # Display the original and cartoon images
    cv2.imshow("Original", img)
    cv2.imshow("Cartoon", cartoon)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Specify the input and output image filenames
input_image = 'input.jpg'
output_image = 'output.jpg'

# Call the cartoonize function with the input and output image filenames
cartoonize(input_image, output_image)

