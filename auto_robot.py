import tkinter as tk
from tkinter import ttk, messagebox
import pyautogui
import threading
import time
from datetime import datetime

class AutoRobot:
    def __init__(self, root):
        self.root = root
        self.root.title("Miner's Haven - Click & Keyboard Macro")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        # Configure pyautogui settings
        pyautogui.FAILSAFE = True  # Move mouse to corner to stop
        pyautogui.PAUSE = 0.1  # Small pause between actions
        
        # Variables
        self.is_running = False
        self.countdown_thread = None
        self.macro_thread = None
        
        self.setup_ui()
        
    def setup_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E
        , tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(main_frame, text="Miner's Haven Rebirth Macro", font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Countdown settings
        countdown_frame = ttk.LabelFrame(main_frame, text="Countdown Settings", padding="10")
        countdown_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 20))
        
        ttk.Label(countdown_frame, text="Countdown (seconds):").grid(row=0, column=0, sticky=tk.W)
        self.countdown_var = tk.StringVar(value="5")
        countdown_entry = ttk.Entry(countdown_frame, textvariable=self.countdown_var, width=10)
        countdown_entry.grid(row=0, column=1, padx=(10, 0))
        
        # Status display
        status_frame = ttk.LabelFrame(main_frame, text="Status", padding="10")
        status_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 20))
        
        self.status_label = ttk.Label(status_frame, text="Ready to start", font=("Arial", 10))
        self.status_label.grid(row=0, column=0, sticky=tk.W)
        
        self.countdown_label = ttk.Label(status_frame, text="", font=("Arial", 12, "bold"))
        self.countdown_label.grid(row=1, column=0, sticky=tk.W, pady=(5, 0))
        
        # Control buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=3, column=0, columnspan=2, pady=(0, 20))
        
        self.start_button = ttk.Button(button_frame, text="Start Macro", command=self.start_macro)
        self.start_button.grid(row=0, column=0, padx=(0, 10))
        
        self.stop_button = ttk.Button(button_frame, text="Stop Macro", command=self.stop_macro, state="disabled")
        self.stop_button.grid(row=0, column=1, padx=(0, 10))
        
        self.reset_button = ttk.Button(button_frame, text="Reset", command=self.reset_macro, state="disabled")
        self.reset_button.grid(row=0, column=2)
        
        # Macro description
        desc_frame = ttk.LabelFrame(main_frame, text="Macro Actions", padding="10")
        desc_frame.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E))
        
        desc_text = """1. Press 'M' key
2. Click at (1214, 366)
3. Click at (1000, 379)
4. Press 'l' key
5. Click at (1333, 280)
6. Wait 2 seconds
7. Press 'l' key again
8. Wait 24 seconds
9. Repeat entire process"""
        
        desc_label = ttk.Label(desc_frame, text=desc_text, justify=tk.LEFT)
        desc_label.grid(row=0, column=0, sticky=tk.W)
        
        # Instructions
        instructions_frame = ttk.LabelFrame(main_frame, text="Instructions", padding="10")
        instructions_frame.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(20, 0))
        
        instructions_text = """• Set countdown time above
• Click 'Start Macro'
• Switch to target application
• Use 'Stop' to pause, 'Reset' to start fresh
• Move mouse to corner to stop"""
        
        instructions_label = ttk.Label(instructions_frame, text=instructions_text, justify=tk.LEFT)
        instructions_label.grid(row=0, column=0, sticky=tk.W)
        
    def update_status(self, message):
        self.status_label.config(text=message)
        self.root.update_idletasks()
        
    def update_countdown(self, seconds):
        if seconds > 0:
            self.countdown_label.config(text=f"Starting in {seconds} seconds...")
        else:
            self.countdown_label.config(text="Running macro...")
        self.root.update_idletasks()
        
    def countdown_timer(self, seconds):
        for i in range(seconds, 0, -1):
            if not self.is_running:
                return
            self.update_countdown(i)
            time.sleep(1)
        self.update_countdown(0)
        
    def perform_macro(self):
        try:
            while self.is_running:
                # Step 1: Press 'M' key
                self.update_status("Pressing 'M' key...")
                pyautogui.press('m')
                time.sleep(0.2)  # 200ms delay
                
                # Step 2: Click at (1214, 366)
                self.update_status("Clicking at (1214, 366)...")
                pyautogui.click(1214, 366)
                time.sleep(0.2)  # 200ms delay
                
                # Step 3: Click at (1000, 379)
                self.update_status("Clicking at (1000, 379)...")
                pyautogui.click(1000, 379)
                time.sleep(0.2)  # 200ms delay
                
                # Step 4: Press 'l' key
                self.update_status("Pressing 'l' key...")
                pyautogui.press('l')
                time.sleep(1)  # 1s delay
                
                # Step 5: Click at (1333, 280)
                self.update_status("Clicking at (1333, 280)...")
                pyautogui.click(1333, 280)
                time.sleep(2)  # 2 second delay
                
                # Step 6: Press 'l' key again
                self.update_status("Pressing 'l' key again...")
                pyautogui.press('l')
                
                # Step 7: Wait 24 seconds before repeating
                self.update_status("Waiting 24 seconds before next cycle...")
                for i in range(24, 0, -1):
                    if not self.is_running:
                        return
                    self.update_status(f"Waiting {i} seconds before next cycle...")
                    time.sleep(1)
                    
        except Exception as e:
            self.update_status(f"Error: {str(e)}")
            self.stop_macro()
            
    def start_macro(self):
        try:
            countdown_seconds = int(self.countdown_var.get())
            if countdown_seconds < 0:
                messagebox.showerror("Error", "Countdown must be a positive number")
                return
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for countdown")
            return
            
        self.is_running = True
        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")
        self.reset_button.config(state="disabled")
        
        # Start countdown in separate thread
        self.countdown_thread = threading.Thread(target=self.countdown_timer, args=(countdown_seconds,))
        self.countdown_thread.daemon = True
        self.countdown_thread.start()
        
        # Start macro after countdown
        def start_macro_after_countdown():
            time.sleep(countdown_seconds)
            if self.is_running:
                self.macro_thread = threading.Thread(target=self.perform_macro)
                self.macro_thread.daemon = True
                self.macro_thread.start()
                
        macro_start_thread = threading.Thread(target=start_macro_after_countdown)
        macro_start_thread.daemon = True
        macro_start_thread.start()
        
    def stop_macro(self):
        self.is_running = False
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")
        self.reset_button.config(state="normal")
        self.update_status("Macro stopped")
        self.countdown_label.config(text="")
        
    def reset_macro(self):
        """Reset the macro to initial state"""
        self.is_running = False
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")
        self.reset_button.config(state="disabled")
        self.update_status("Ready to start")
        self.countdown_label.config(text="")

def main():
    root = tk.Tk()
    app = AutoRobot(root)
    root.mainloop()

if __name__ == "__main__":
    main() 