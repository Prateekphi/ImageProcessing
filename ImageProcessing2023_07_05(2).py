import os
import cv2
import numpy as np

# Set the paths to your directories containing positive and negative images
positive_directory = "D:\\Research\\ComputerVision\\positiveImages"
negative_directory = "D:\\Research\\ComputerVision\\negativeImages"

# Load the positive images
positive_files = sorted(os.listdir(positive_directory))
positive_images = [cv2.imread(os.path.join(positive_directory, file)) for file in positive_files]

# Load the negative images
negative_files = sorted(os.listdir(negative_directory))
negative_images = [cv2.imread(os.path.join(negative_directory, file)) for file in negative_files]

# Define the maximum width and height
max_width = 1400
max_height = 750


# Resize images to a maximum width of 1600 pixels
# Resize the images while preserving aspect ratio
def resize_images(images):
    resized_images = []
    for image in images:
        # Get the original image dimensions
        height, width = image.shape[:2]

        # Calculate the aspect ratio
        aspect_ratio = width / float(height)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Determine the new dimensions based on the maximum width or height
        if width > max_width:
            width = max_width
            height = int(width / aspect_ratio)
        if height > max_height:
            height = max_height
            width = int(height * aspect_ratio)

        # Resize the image
        resized_image = cv2.resize(gray, (width, height))

        resized_images.append(resized_image)

    return resized_images


# Perform defect detection using blob detection
def detect_defects(images):
    total_defects_detected = 0
    for image in images:
        # Convert grayscale image to 3-channel image
        color_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

        # Perform thresholding to obtain binary image
        _, binary = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

        # Set up the blob detector parameters
        params = cv2.SimpleBlobDetector_Params()

        # Modify parameters as needed
        params.minThreshold = 1  # Minimum threshold value to consider a pixel as part of a blob
        params.maxThreshold = 25  # Maximum threshold value to consider a pixel as part of a blob
        params.filterByArea = True  # Filter blobs based on area
        params.minArea = 80  # Minimum blob area in pixels
        params.maxArea = 280  # Maximum blob area in pixels
        params.filterByCircularity = True  # Filter blobs based on circularity
        params.minCircularity = 0.4  # Minimum circularity value (0.0 - 1.0)
        params.filterByConvexity = True  # Filter blobs based on convexity
        params.minConvexity = 0.85  # Minimum convexity value (0.0 - 1.0)
        params.filterByInertia = True  # Filter blobs based on inertia
        params.minInertiaRatio = 0.2

        # Create the blob detector
        detector = cv2.SimpleBlobDetector_create(params)

        # Detect blobs in the binary image
        keypoints = detector.detect(binary)
        if len(keypoints) > 0:
            total_defects_detected += 1

        # Draw detected blobs on the color image
        image_with_keypoints = cv2.drawKeypoints(color_image, keypoints, np.array([]), (0, 0, 255),
                                                 cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

        # Display or save the image with detected blobs
        # cv2.imshow("Defect Detection", image_with_keypoints)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

    return total_defects_detected


# Calculate accuracy of defect detection
def calculate_accuracy(total_defects_detected, total_images):
    accuracy = (total_defects_detected / total_images) * 100
    return accuracy


# Resize positive images to a maximum width of 1600 pixels
positive_images_resized = resize_images(positive_images)

# Resize negative images to a maximum width of 1600 pixels
negative_images_resized = resize_images(negative_images)

# Detect defects in positive images
positive_defects_detected = detect_defects(positive_images_resized)
positive_defects_accuracy = positive_defects_detected/len(positive_images_resized)*100

# Detect defects in negative images
negative_defects_detected = detect_defects(negative_images_resized)
negative_defects_accuracy = (1 - negative_defects_detected/len(negative_images_resized))*100

# Calculate total number of images
# total_images = len(positive_images_resized) + len(negative_images_resized)

# Calculate total defects detected
# total_defects_detected = positive_defects_detected + negative_defects_detected

# Calculate accuracy
# accuracy = calculate_accuracy(total_defects_detected, total_images)

print("Positive Defect Detection Accuracy: {:.2f}%".format(positive_defects_accuracy))
print("Negative Defect Detection Accuracy: {:.2f}%".format(negative_defects_accuracy))
