import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import cv2
import config
from pipelines.schematic_pipeline import SchematicPipeline

class PitikDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title(config.APP_NAME)
        self.root.geometry(f"{config.WINDOW_WIDTH}x{config.WINDOW_HEIGHT}")
        
        # Initialize the pipeline
        self.pipeline = SchematicPipeline()

        # Main Layout
        self.setup_ui()

    def setup_ui(self):
        # 1. Top Header
        header = tk.Label(self.root, text="PITIK-SIM: Waiting for Input...", 
                          font=("Arial", 16, "bold"), bg="#333", fg="white")
        header.pack(fill=tk.X, side=tk.TOP, ipady=10)

        # 2. Main Content Area
        content_frame = tk.Frame(self.root)
        content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # --- LEFT PANEL: Schematic View ---
        self.schematic_label = tk.Label(content_frame, text="[Schematic View]", 
                                        bg="gray", width=40)
        self.schematic_label.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)

        # --- CENTER PANEL: Controls ---
        control_frame = tk.Frame(content_frame, width=200, bg="#eee")
        control_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5)

        # Button: Load & Process
        btn_test = tk.Button(control_frame, text="Load & Process Image", 
                             command=self.run_test_scan,
                             bg="#007bff", fg="white", font=("Arial", 12))
        btn_test.pack(pady=20, fill=tk.X, padx=10)

        # Status Label
        self.status_label = tk.Label(control_frame, text="Ready", wraplength=150, bg="#eee")
        self.status_label.pack(pady=10)

        # --- RIGHT PANEL: Breadboard View (Placeholder) ---
        self.breadboard_label = tk.Label(content_frame, text="[Breadboard View]", 
                                         bg="lightgray", width=40)
        self.breadboard_label.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)

    def run_test_scan(self):
        """
        Opens a file dialog, runs the pipeline, and updates the UI.
        """
        # 1. Ask user to pick an image
        file_path = filedialog.askopenfilename(
            initialdir=config.TEST_IMAGES_DIR,
            title="Select Test Image",
            filetypes=(("images", "*.jpg *.png"), ("all files", "*.*"))
        )
        
        if not file_path:
            return

        # 2. Run the Pipeline
        processed_img, message = self.pipeline.process_image(file_path)
        
        # 3. Update Status
        self.status_label.config(text=message)

        # 4. Show Image in GUI
        if processed_img is not None:
            # OpenCV is BGR, Tkinter needs RGB
            img_rgb = cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB)
            
            # Resize for display (keep aspect ratio relative to a fixed height)
            h, w, _ = img_rgb.shape
            display_h = 400
            display_w = int(w * (display_h / h))
            img_resized = cv2.resize(img_rgb, (display_w, display_h))
            
            # Convert to ImageTk
            img_tk = ImageTk.PhotoImage(Image.fromarray(img_resized))
            
            # Update Label
            self.schematic_label.config(image=img_tk, text="")
            self.schematic_label.image = img_tk  # Keep reference!