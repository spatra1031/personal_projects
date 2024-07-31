import cv2

# Read the image
image = cv2.imread('parking_lot_no_2.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to create a binary image
_, binary_image = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)

# Display the binary image
cv2.imwrite('binary_image.png', binary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
