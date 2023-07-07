# ImageProcessing
Defect (Blobs) detection using Python in 3D Printed artifacts
This code performs defect detection using blob detection in a collection of positive and negative images, It calculates the accuracy of defect detection based on the number of images where defects were correctly detected.

## Requirements
- Python 3.x
- OpenCV (cv2) library

## Installation
1. Clone the repository or download the code files.
2. Install the required dependencies using pip:


## Usage
1. Prepare your positive and negative images:
- Create two separate directories for positive and negative images.
- Place your positive images in one directory and negative images in the other.

2. Update the code:
- Open the code file in a text editor.
- Update the `positive_directory` and `negative_directory` variables with the paths to your positive and negative image directories.

3. Run the code:
- Execute the code in a Python environment.
- The code will resize the images, perform defect detection using blob detection, and display the images with detected blobs.
- The accuracy of defect detection will be calculated and displayed.

## Customization
You can customize the blob detection parameters by modifying the `params` object in the `detect_defects` function. Adjust the threshold values, area constraints, circularity, convexity, and inertia parameters based on your specific requirements.

## Notes
- The code assumes that the images are in grayscale format. If your images are in color, you may need to adjust the code accordingly.
- The accuracy calculation is based on the number of images where defects were detected. It does not take into account the type or severity of the defects.
