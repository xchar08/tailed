import cv2
from matplotlib import pyplot as plt
import numpy as np

# Function to create a pixel art representation similar to the uploaded example
def create_pixel_art_grid(image_path, output_path, grid_size=(8, 8)):
    # Read the input image
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    if image is None:
        print("Error: Could not read the image.")
        return
    
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply GaussianBlur to reduce noise and improve edge detection
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
    
    # Apply the Canny edge detection with adjusted thresholds to make edges more prominent
    edges = cv2.Canny(blurred_image, threshold1=50, threshold2=150)
    
    # Fill the edges with white to make them more prominent
    filled_edges = cv2.dilate(edges, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)))

    # Create a blank grid with each cell being the size specified in `grid_size`
    rows, cols = filled_edges.shape
    grid_image = np.zeros_like(filled_edges)
    
    # Fill in the grid cells based on the edge detection result
    for y in range(0, rows, grid_size[0]):
        for x in range(0, cols, grid_size[1]):
            # If there's a detected edge in the current cell, fill the cell
            if np.any(filled_edges[y:y+grid_size[0], x:x+grid_size[1]]):
                grid_image[y:y+grid_size[0], x:x+grid_size[1]] = 255
    
    # Save the result to the output path
    cv2.imwrite(output_path, grid_image)
    
    # Display the original, filled edge-detected, and grid pixel art images
    plt.figure(figsize=(15, 5))
    
    plt.subplot(1, 2, 1)
    plt.imshow(filled_edges, cmap='gray')
    plt.title('Enhanced Edge Detection (Filled)')
    plt.axis('off')
    
    plt.subplot(1, 2, 2)
    plt.imshow(grid_image, cmap='gray')
    plt.title('Grid Pixel Art')
    plt.axis('off')
    
    plt.show()

# Example usage
input_image_path = 'input.jpg'
output_image_path = 'output.jpg'

create_pixel_art_grid(input_image_path, output_image_path)
