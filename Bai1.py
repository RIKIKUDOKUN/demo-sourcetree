import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser

class FrameRecorder:
    def __init__(self, master):
        self.master = master
        master.title("Frame Recorder")

        # Frame for title
        title_frame = tk.Frame(master, bg="#f0f0f0")
        title_frame.pack(pady=10)

        # Title Label
        title_label = tk.Label(title_frame, text="Frame Recorder", font=("Arial", 20), bg="#f0f0f0")
        title_label.pack()

        # Frame for input and buttons
        input_frame = tk.Frame(master, bg="#f0f0f0")
        input_frame.pack()

        # FPS Label and input
        fps_label = tk.Label(input_frame, text="create an", bg="#f0f0f0")
        fps_label.grid(row=0, column=0, padx=5, pady=5)

        self.fps_entry = tk.Entry(input_frame, bg="#ffffff")
        self.fps_entry.insert(0, "100")
        self.fps_entry.grid(row=0, column=1, padx=5, pady=5)

        fps_label = tk.Label(input_frame, text="fps video", bg="#f0f0f0")
        fps_label.grid(row=0, column=2, padx=5, pady=5)

        # Buttons Frame
        button_frame = tk.Frame(master, bg="#f0f0f0")
        button_frame.pack(pady=10)

        # Pause Button
        self.pause_button = tk.Button(button_frame, text="Pause", command=self.pause_recording, width=10, bg="#ffffff")
        self.pause_button.grid(row=0, column=0, padx=5, pady=5)

        # Start Button
        self.start_button = tk.Button(button_frame, text="Start", command=self.start_recording, width=10, bg="#ffffff")
        self.start_button.grid(row=0, column=1, padx=5, pady=5)

        # End Button
        self.end_button = tk.Button(button_frame, text="End", command=self.end_recording, width=10, bg="#ffffff")
        self.end_button.grid(row=0, column=2, padx=5, pady=5)

        # Status Label
        self.status_label = tk.Label(master, text="Recording Paused", font=("Arial", 12), bg="#f0f0f0")
        self.status_label.pack(pady=10)

        # Color Button
        self.color_button = tk.Button(master, text="Change Color", command=self.change_color, width=10, bg="#ffffff")
        self.color_button.pack(pady=10)

        # Initialize variables
        self.video_capture = None
        self.recording = False
        self.output_video = None
        self.fps = None

    def start_recording(self):
        self.fps = int(self.fps_entry.get())
        self.recording = True
        self.status_label.config(text="Recording Started")
        self.pause_button.config(state=tk.NORMAL)
        self.start_button.config(state=tk.DISABLED)
        self.end_button.config(state=tk.NORMAL)

        while self.recording:
            ret, frame = self.video_capture.read()
            if ret:
                self.output_video.write(frame)
            else:
                self.end_recording()
                self.status_label.config(text="Error reading frames")
                break

    def pause_recording(self):
        self.recording = False
        self.status_label.config(text="Recording Paused")
        self.pause_button.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL)

    def end_recording(self):
        self.recording = False
        if self.video_capture:
            self.video_capture.release()
        if self.output_video:
            self.output_video.release()
        self.status_label.config(text="Recording Ended")
        self.pause_button.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL)
        self.end_button.config(state=tk.DISABLED)

    def change_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.master.configure(background=color)
            self.title_frame.configure(background=color)
            self.input_frame.configure(background=color)
            self.button_frame.configure(background=color)
            self.status_label.configure(background=color)
            self.color_button.configure(background=color)
            self.fps_entry.configure(background=color)
            self.pause_button.configure(background=color)
            self.start_button.configure(background=color)
            self.end_button.configure(background=color)

# Create main window and run the app
root = tk.Tk()
app = FrameRecorder(root)
root.mainloop()