import tkinter as tk
from tkinter import messagebox, ttk
import random
import threading
import time

class AntiVirusApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("AtarBals Modern Antivirus")
        self.geometry("800x600")
        self.configure(bg="white")

        self.create_widgets()
        self.current_scan = None

    def create_widgets(self):
        # Menu bên trái
        self.menu_frame = tk.Frame(self, bg="#2c3e50", width=200)
        self.menu_frame.pack(side=tk.LEFT, fill=tk.Y)

        self.buttons = ["Status", "Updates", "Settings", "Share Feedback", "Buy Premium", "Help", "Scan Now"]
        for button in self.buttons:
            btn = tk.Button(self.menu_frame, text=button, font=("Helvetica", 14), 
                            bg="#27ae60" if button == "Scan Now" else "#3498db", 
                            fg="white", command=lambda b=button: self.button_click(b))
            btn.pack(fill=tk.X, pady=5, padx=10)

        # Phần chính bên phải
        self.main_frame = tk.Frame(self, bg="white")
        self.main_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.label_title = tk.Label(self.main_frame, text="Scan", font=("Helvetica", 24, "bold"), bg="white")
        self.label_title.grid(row=0, column=0, columnspan=2, pady=10)

        self.label_premium = tk.Label(self.main_frame, text="Premium will be free forever. You just need to click button.", font=("Helvetica", 12), bg="white")
        self.label_premium.grid(row=1, column=0, columnspan=2, pady=10)

        scan_buttons = [
            ("Quick Scan", self.quick_scan),
            ("Web Protection", self.web_protection),
            ("Quarantine", self.quarantine),
            ("Full Scan", self.full_scan)
        ]

        for i, (text, command) in enumerate(scan_buttons):
            btn = tk.Button(self.main_frame, text=text, font=("Helvetica", 14), 
                            bg="#e74c3c", fg="white", width=15, height=2, command=command)
            btn.grid(row=2 + i//2, column=i%2, padx=10, pady=5)

        self.button_simple_update = tk.Button(self.main_frame, text="Simple Update", font=("Helvetica", 14), 
                                              bg="#f39c12", fg="white", width=15, height=2, command=self.simple_update)
        self.button_simple_update.grid(row=4, column=0, columnspan=2, pady=5)

        self.label_get_premium = tk.Label(self.main_frame, text="Get Premium to Enable: (Web Protection), (Full Scan), (Simple Update)", 
                                          font=("Helvetica", 12), bg="white", fg="#7f8c8d")
        self.label_get_premium.grid(row=5, column=0, columnspan=2, pady=20)

        # Progress bar
        self.progress = ttk.Progressbar(self.main_frame, orient="horizontal", length=300, mode="determinate")
        self.progress.grid(row=6, column=0, columnspan=2, pady=10)

        # Status label
        self.label_status = tk.Label(self.main_frame, text="Ready", font=("Helvetica", 12), bg="white")
        self.label_status.grid(row=7, column=0, columnspan=2, pady=5)

    def button_click(self, button_text):
        messagebox.showinfo("Button Clicked", f"You clicked: {button_text}")

    def quick_scan(self):
        self.start_scan("Quick Scan", 10)

    def web_protection(self):
        messagebox.showinfo("Premium Feature", "Web Protection is a premium feature. Please upgrade to use it.")

    def quarantine(self):
        messagebox.showinfo("Quarantine", "No threats found in quarantine.")

    def full_scan(self):
        messagebox.showinfo("Premium Feature", "Full Scan is a premium feature. Please upgrade to use it.")

    def simple_update(self):
        messagebox.showinfo("Premium Feature", "Simple Update is a premium feature. Please upgrade to use it.")

    def start_scan(self, scan_type, duration):
        if self.current_scan:
            messagebox.showwarning("Scan in Progress", "A scan is already in progress. Please wait.")
            return

        self.current_scan = threading.Thread(target=self.run_scan, args=(scan_type, duration))
        self.current_scan.start()

    def run_scan(self, scan_type, duration):
        self.label_status.config(text=f"{scan_type} in progress...")
        self.progress["value"] = 0
        
        for i in range(101):
            if self.current_scan is None:  # Check if scan was cancelled
                break
            time.sleep(duration / 100)
            self.progress["value"] = i
            self.update_idletasks()

        if self.current_scan:
            self.label_status.config(text=f"{scan_type} completed.")
            messagebox.showinfo("Scan Complete", f"{scan_type} completed. No threats found.")
        
        self.current_scan = None
        self.progress["value"] = 0

    def cancel_scan(self):
        if self.current_scan:
            self.current_scan = None
            self.label_status.config(text="Scan cancelled.")
            self.progress["value"] = 0

if __name__ == "__main__":
    app = AntiVirusApp()
    app.mainloop()
