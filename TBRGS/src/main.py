import sys
from data_processing import process_scats_data

import tkinter as tk
from gui.dashboard import TBRGSApp

import time

REQUIRED_PYTHON_VERSION = (3, 11, 11)
MINMUM_PYTHON_VERSION = (3, 10, 0)
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
    if current_version > MINMUM_PYTHON_VERSION  and current_version != REQUIRED_PYTHON_VERSION:
        print("❌ This program requires Python 3.11.11")
        print(f"You are using Python {'.'.join(map(str, current_version))}")
        sys.exit(1)
    else:
        print(f"✅ Runing Python version : {current_version[0]}.{current_version[1]}.{current_version[2]}")


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