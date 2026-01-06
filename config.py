# config.py
import os

# --- SYSTEM CONSTANTS ---
APP_NAME = "PITIK-SIM Tutoring System"
WINDOW_WIDTH = 1024  # Standard size for the Pi 7-inch Touch Screen (Section 3.4.1.3)
WINDOW_HEIGHT = 600

# --- FILE PATHS ---
# We use os.path to ensure this works on both Mac (your sim) and Linux (the Pi)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
TEST_IMAGES_DIR = os.path.join(BASE_DIR, 'tests', 'test_images')

# --- CAMERA SETTINGS (Section 3.2.1) ---
# The Pi HQ Camera supports high resolutions, but for processing speed,
# we often resize down during the CV analysis.
CAMERA_RESOLUTION = (1280, 720)
FRAMERATE = 30

# --- FIDUCIAL MARKERS (Section 3.1.3) ---
# These are the HSV color ranges for the "Colored Beads" on your components.
# We will calibrate these later, but these are good placeholders.
COMPONENT_COLORS = {
    "RESISTOR_TAG": ((0, 100, 100), (10, 255, 255)),   # Example: Red tag
    "CAPACITOR_TAG": ((100, 100, 100), (120, 255, 255)) # Example: Blue tag
}

# --- SPICE SETTINGS ---
# Path to the ngspice executable we installed via Homebrew
SPICE_EXECUTABLE = "ngspice"