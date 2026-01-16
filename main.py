# main.py
import tkinter as tk
import config
from gui.dashboard import PitikDashboard
import sys

def main():
    print(f"Booting {config.APP_NAME}...")
    print(f"Environment: {sys.platform}")
    
    # Initialize the main window
    root = tk.Tk()
    
    # Load our custom dashboard class
    app = PitikDashboard(root)
    
    # Start the GUI event loop
    try:
        root.mainloop()
    except KeyboardInterrupt:
        print("Shutting down...")

if __name__ == "__main__":
    main()

