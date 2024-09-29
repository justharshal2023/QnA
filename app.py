import pytesseract
from PIL import Image
import requests
from io import BytesIO
import numpy as np
import cv2
from google.colab import files

# Function to extract text from image using OCR
def extract_text(image):
    # Convert the image to OpenCV format (BGR)
    img = np.array(image)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    
    # Use pytesseract to extract text
    text = pytesseract.image_to_string(img)
    return text

# Provide options to either upload an image or input a URL
print("Select input method: ")
print("1. Upload Image")
print("2. Enter Image URL")

choice = input("Enter choice (1 or 2): ")

if choice == '1':
    # Upload image
    uploaded = files.upload()
    image_path = list(uploaded.keys())[0]  # Get the uploaded file name
    image = Image.open(image_path)
    
    # Display image
    image.show()

    # Extract text from uploaded image
    extracted_text = extract_text(image)
    print("\nExtracted Text from Uploaded Image:\n")
    print(extracted_text)

elif choice == '2':
    # Input image URL
    url = input("Enter Image URL: ")
    
    try:
        # Fetch image from the URL
        response = requests.get(url)
        image = Image.open(BytesIO(response.content))
        
        # Display image
        image.show()

        # Extract text from image URL
        extracted_text = extract_text(image)
        print("\nExtracted Text from Image URL:\n")
        print(extracted_text)

    except Exception as e:
        print(f"Error fetching image from URL: {e}")
else:
    print("Invalid choice. Please select 1 or 2.")
