import subprocess
import cv2
import time
import os

print("--------------------------------------------------")
print("   PITIK-SIM: Hardware Abstraction Layer")
print("   Mode: CLI Wrapper (Bookworm Compatible)")
print("--------------------------------------------------")

def take_picture(filename="test_image.jpg"):
    # We use the official 'rpicam-jpeg' tool which is pre-installed on Bookworm
    # This bypasses any Python library path issues.
    cmd = [
        "rpicam-jpeg",
        "-o", filename,               
        "-t", "1000",                 
        "--width", "640",             
        "--height", "480",            
        "--nopreview",                
        "--autofocus-mode", "manual", 
        "--lens-position", "3.33"      # Locked focus for a 30cm rig height
    ]
    
    try:
        print(f"[1/3] Capturing via hardware command...")
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        if os.path.exists(filename):
            print(f"[2/3] Image saved to disk: {filename}")
            
            # Load into OpenCV to prove we can use it for the thesis
            img = cv2.imread(filename)
            print(f"[3/3] Loaded into OpenCV! Shape: {img.shape}")
            return img
        else:
            print("ERROR: Command ran but no file was created.")
            return None
            
    except Exception as e:
        print(f"CRITICAL ERROR: {e}")
        print("Tip: Run 'rpicam-hello' in terminal to check if camera is connected.")
        return None

if __name__ == "__main__":
    take_picture()