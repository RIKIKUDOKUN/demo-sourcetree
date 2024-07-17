import tkinter as tk
from tkinter import messagebox

class AntiVirusApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("AtarBals Modern Antivirus")
        self.geometry("800x500")
        self.configure(bg="white")

        self.create_widgets()

    def create_widgets(self):
        # Menu bên trái
        self.menu_frame = tk.Frame(self, bg="blue", width=200)
        self.menu_frame.pack(side=tk.LEFT, fill=tk.Y)

        self.buttons = ["Status", "Updates", "Settings", "Share Feedback", "Buy Premium", "Help", "Scan Now"]
        for button in self.buttons:
            btn = tk.Button(self.menu_frame, text=button, font=("Helvetica", 14), bg="green" if button == "Scan Now" else "white", fg="black" if button == "Scan Now" else "black")
            btn.pack(fill=tk.X, pady=5, padx=10)

        # Phần chính bên phải
        self.main_frame = tk.Frame(self, bg="white")
        self.main_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.label_title = tk.Label(self.main_frame, text="Scan", font=("Helvetica", 24), bg="white")
        self.label_title.grid(row=0, column=0, columnspan=2, pady=10)

        self.label_premium = tk.Label(self.main_frame, text="Premium will be free forever. You just need to click button.", font=("Helvetica", 12), bg="white")
        self.label_premium.grid(row=1, column=0, columnspan=2, pady=10)

        self.button_quick_scan = tk.Button(self.main_frame, text="Quick Scan", font=("Helvetica", 14), bg="magenta", fg="black", width=15, height=2)
        self.button_quick_scan.grid(row=2, column=0, padx=10, pady=5)

        self.button_web_protection = tk.Button(self.main_frame, text="Web Protection", font=("Helvetica", 14), bg="magenta", fg="black", width=15, height=2)
        self.button_web_protection.grid(row=2, column=1, padx=10, pady=5)

        self.button_quarantine = tk.Button(self.main_frame, text="Quarantine", font=("Helvetica", 14), bg="magenta", fg="black", width=15, height=2)
        self.button_quarantine.grid(row=3, column=0, padx=10, pady=5)

        self.button_full_scan = tk.Button(self.main_frame, text="Full Scan", font=("Helvetica", 14), bg="magenta", fg="black", width=15, height=2)
        self.button_full_scan.grid(row=3, column=1, padx=10, pady=5)

        self.button_simple_update = tk.Button(self.main_frame, text="Simple Update", font=("Helvetica", 14), bg="magenta", fg="black", width=15, height=2)
        self.button_simple_update.grid(row=4, column=0, columnspan=2, pady=5)

        self.label_get_premium = tk.Label(self.main_frame, text="Get Premium to Enable: (Web Protection), (Full Scan), (Simple Update)", font=("Helvetica", 12), bg="white")
        self.label_get_premium.grid(row=5, column=0, columnspan=2, pady=20)

    def pause_recording(self):
        self.label_status.config(text="Recording Paused")

    def start_recording(self):
        fps = self.entry_fps.get()
        if not fps.isdigit():
            messagebox.showerror("Invalid input", "Please enter a valid number for FPS")
        else:
            self.label_status.config(text="Recording Started")

    def end_recording(self):
        self.label_status.config(text="Recording Ended")


if __name__ == "__main__":
    app = AntiVirusApp()
    app.mainloop()