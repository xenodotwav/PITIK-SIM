# tools/generate_template.py
import cv2
import numpy as np
import os

def create_marker_template():
    # Define image size (A4 ratio-ish)
    width, height = 2480, 3508  # ~300 DPI A4
    img = np.ones((height, width, 3), dtype=np.uint8) * 255  # White background

    # Define ArUco dictionary (4x4 squares, 50 possible IDs)
    # This matches common usage for fiducial markers
    aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)

    # Define marker size (pixels) and positions (Corners)
    marker_size = 300
    margin = 100
    
    # Coordinates for 4 corners: TL, TR, BR, BL
    positions = {
        0: (margin, margin),                                      # Top-Left (ID 0)
        1: (width - margin - marker_size, margin),                # Top-Right (ID 1)
        2: (width - margin - marker_size, height - margin - marker_size), # Bottom-Right (ID 2)
        3: (margin, height - margin - marker_size)                # Bottom-Left (ID 3)
    }

    print("Generating Template with ArUco Markers...")
    
    for marker_id, (x, y) in positions.items():
        # Generate the marker image
        marker_img = np.zeros((marker_size, marker_size), dtype=np.uint8)
        cv2.aruco.generateImageMarker(aruco_dict, marker_id, marker_size, marker_img, 1)
        
        # Paste it onto the white canvas
        # Convert grayscale marker to BGR to match canvas
        marker_img_bgr = cv2.cvtColor(marker_img, cv2.COLOR_GRAY2BGR)
        img[y:y+marker_size, x:x+marker_size] = marker_img_bgr
        
        # Label it (optional, for human reading)
        cv2.putText(img, f"ID: {marker_id}", (x, y - 20), 
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 5)

    # Draw a "Drawing Area" box in the middle (where components go)
    cv2.rectangle(img, 
                  (margin + marker_size + 50, margin + 50), 
                  (width - margin - marker_size - 50, height - margin - 50), 
                  (200, 200, 200), 5)
    
    cv2.putText(img, "PITIK-SIM DRAWING AREA", (width//2 - 400, height//2), 
                cv2.FONT_HERSHEY_SIMPLEX, 3, (180, 180, 180), 5)

    # Save
    output_path = "assets/templates/master_template.png"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    cv2.imwrite(output_path, img)
    print(f"Template saved to: {output_path}")

if __name__ == "__main__":
    create_marker_template()