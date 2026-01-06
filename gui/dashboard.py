# gui/dashboard.py
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk # This tests if Pillow is installed
import config

class PitikDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title(config.APP_NAME)
        self.root.geometry(f"{config.WINDOW_WIDTH}x{config.WINDOW_HEIGHT}")
        
        # Main Layout: 3 Columns (Schematic, Breadboard, Feedback)
        # Matches the description in Section 3.3.3.3.1
        self.setup_ui()

    def setup_ui(self):
        # 1. Top Header
        header = tk.Label(self.root, text="PITIK-SIM: Waiting for Input...", 
                          font=("Arial", 16, "bold"), bg="#333", fg="white")
        header.pack(fill=tk.X, side=tk.TOP, ipady=10)

        # 2. Main Content Area
        content_frame = tk.Frame(self.root)
        content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Left Panel: Schematic View (Placeholder)
        self.schematic_panel = tk.Label(content_frame, text="[Schematic Feed]", 
                                        bg="lightgray", width=40)
        self.schematic_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)

        # Center Panel: Controls
        control_frame = tk.Frame(content_frame, width=200, bg="#eee")
        control_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5)
        
        btn_scan = tk.Button(control_frame, text="SCAN CIRCUITS", 
                             bg="green", fg="white", font=("Arial", 12, "bold"))
        btn_scan.pack(pady=20, fill=tk.X, padx=10)

        # Right Panel: Breadboard View (Placeholder)
        self.breadboard_panel = tk.Label(content_frame, text="[Breadboard Feed]", 
                                         bg="lightgray", width=40)
        self.breadboard_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)

    def load_test_image(self):
        """
        Temporary function to test Pillow library.
        Ideally, this will load the sample images you saved on Day 1.
        """
        print("System Ready. Waiting for camera hardware...")