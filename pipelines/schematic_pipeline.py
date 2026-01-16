# pipelines/schematic_pipeline.py
import cv2
import numpy as np

class SchematicPipeline:
    def __init__(self):
        # Initialize ArUco detector
        self.aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
        self.aruco_params = cv2.aruco.DetectorParameters()
        
        # Create the detector (New Syntax for OpenCV 4.7+)
        self.detector = cv2.aruco.ArucoDetector(self.aruco_dict, self.aruco_params)
        
        # Target size for the "flattened" image (e.g., 1000x1400 pixels)
        self.output_size = (1000, 1414) # Approx A4 Aspect Ratio

    def process_image(self, image_path):
        """
        Main function to load, detect, and warp the schematic.
        """
        # 1. Load Image
        frame = cv2.imread(image_path)
        if frame is None:
            return None, "Error: Image not found."

        # 2. Detect Markers
        corners, ids, rejected = self.detector.detectMarkers(frame)
        
        if ids is None or len(ids) < 4:
            return frame, "Error: Could not find all 4 ArUco markers."

        # 3. Organize Markers (We need to know which corner is which)
        # We assume ID 0=TopLeft, 1=TopRight, 2=BottomRight, 3=BottomLeft
        # Flatten the list of IDs
        ids = ids.flatten()
        
        # Map ID to its center coordinate
        centers = {}
        for i, corner in zip(ids, corners):
            # 'corner' is shape (1, 4, 2). We want the center of the marker.
            c = corner[0]
            center_x = int(np.mean(c[:, 0]))
            center_y = int(np.mean(c[:, 1]))
            centers[i] = (center_x, center_y)

        # Check if we have all 4 IDs
        if not all(id in centers for id in [0, 1, 2, 3]):
             return frame, "Error: Missing one of the specific Corner IDs (0-3)."

        # 4. Define Source Points (The detected corners)
        src_points = np.array([
            centers[0], # TL
            centers[1], # TR
            centers[2], # BR
            centers[3]  # BL
        ], dtype=np.float32)

        # 5. Define Destination Points (Where we want them to go)
        # We want them perfectly in the corners of our output size
        dst_points = np.array([
            [0, 0],                                      # TL
            [self.output_size[0], 0],                    # TR
            [self.output_size[0], self.output_size[1]],  # BR
            [0, self.output_size[1]]                     # BL
        ], dtype=np.float32)

        # 6. Calculate the Transform Matrix
        matrix = cv2.getPerspectiveTransform(src_points, dst_points)

        # 7. Warp the Image (The Magic Step)
        warped_img = cv2.warpPerspective(frame, matrix, self.output_size)

        return warped_img, "Success: Perspective Corrected."