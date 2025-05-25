import sys
from data_processing import process_scats_data

import tkinter as tk
from gui.dashboard import TBRGSApp

import time

current_version = sys.version_info[:3]

def show_splash():
    splash = tk.Toplevel()
    splash.overrideredirect(True)  # Removes title bar
    splash.configure(bg="white")

    width, height = 400, 300
        
    # Calculate center position
    screen_width = splash.winfo_screenwidth()
    screen_height = splash.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    splash.geometry(f"{width}x{height}+{x}+{y}")

    # Optional: add a loading message or GIF
    label = tk.Label(splash, text="Loading nodes and edges...", font=("Helvetica", 14), bg="white", fg="black", highlightthickness=0)
    label.pack(expand=True)

    return splash

def main():
    if not (
    (current_version[0] == 3 and current_version[1] == 10) or
    (current_version[0] == 3 and current_version[1] == 11)
    ):
        print("❌ This program requires Python 3.10.x or 3.11.x")
        print(f"You are using Python {'.'.join(map(str, current_version))}")
        sys.exit(1)
    else:
        print(f"✅ Running supported Python version: {'.'.join(map(str, current_version))}")

    root = tk.Tk()
    root.withdraw()  # Hide root while loading

    splash = show_splash()
    root.update()
    
    time.sleep(3)  # Simulate loading time, can be removed later
    
    # Make the main graph object
    SCATS_Graph = process_scats_data()

    splash.destroy()
    root.deiconify()  # Show main window
    
    app = TBRGSApp(root, SCATS_Graph)
    
    root.mainloop()
 
    
        
if __name__ == "__main__":
    main()