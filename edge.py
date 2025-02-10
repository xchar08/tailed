import cv2
import numpy as np

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
    
    # Apply Canny edge detection with adjusted thresholds
    edges = cv2.Canny(blurred_image, threshold1=50, threshold2=150)
    
    # Dilate the edges to make them more prominent
    filled_edges = cv2.dilate(edges, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)))
    
    # Create a blank grid with the same dimensions as the filled edge image
    rows, cols = filled_edges.shape
    grid_image = np.zeros_like(filled_edges)
    
    # Fill in grid cells based on the edge detection result
    for y in range(0, rows, grid_size[0]):
        for x in range(0, cols, grid_size[1]):
            # Check if any edge is present in the current grid cell
            if np.any(filled_edges[y:y+grid_size[0], x:x+grid_size[1]]):
                grid_image[y:y+grid_size[0], x:x+grid_size[1]] = 255
    
    # Save the resulting grid pixel art image
    cv2.imwrite(output_path, grid_image)
    
    # Display the enhanced edge detection image and grid pixel art using OpenCV
    cv2.imshow("Enhanced Edge Detection (Filled)", filled_edges)
    cv2.imshow("Grid Pixel Art", grid_image)
    
    # Wait indefinitely until a key is pressed, then close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
input_image_path = 'input.jpg'
output_image_path = 'output.jpg'
create_pixel_art_grid(input_image_path, output_image_path)
