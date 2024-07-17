import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser
from tkinter import filedialog
import os
import cv2
import numpy as np
from PIL import Image, ImageTk

class FrameRecorder:
    def __init__(self, master):
        self.master = master
        master.title("Frame Recorder")

        # Frame for title
        self.title_frame = tk.Frame(master, bg="#f0f0f0")
        self.title_frame.pack(pady=10)

        # Title Label
        title_label = tk.Label(self.title_frame, text="Frame Recorder", font=("Arial", 20), bg="#f0f0f0")
        title_label.pack()

        # Frame for input and buttons
        self.input_frame = tk.Frame(master, bg="#f0f0f0")
        self.input_frame.pack()

        # FPS Label and input
        fps_label = tk.Label(self.input_frame, text="create an", bg="#f0f0f0")
        fps_label.grid(row=0, column=0, padx=5, pady=5)

        self.fps_entry = tk.Entry(self.input_frame, bg="#ffffff")
        self.fps_entry.insert(0, "30")
        self.fps_entry.grid(row=0, column=1, padx=5, pady=5)

        fps_label = tk.Label(self.input_frame, text="fps video", bg="#f0f0f0")
        fps_label.grid(row=0, column=2, padx=5, pady=5)

        # Buttons Frame
        self.button_frame = tk.Frame(master, bg="#f0f0f0")
        self.button_frame.pack(pady=10)

        # Pause Button
        self.pause_button = tk.Button(self.button_frame, text="Pause", command=self.pause_recording, width=10, bg="#ffffff")
        self.pause_button.grid(row=0, column=0, padx=5, pady=5)

        # Start Button
        self.start_button = tk.Button(self.button_frame, text="Start", command=self.start_recording, width=10, bg="#ffffff")
        self.start_button.grid(row=0, column=1, padx=5, pady=5)

        # End Button
        self.end_button = tk.Button(self.button_frame, text="End", command=self.end_recording, width=10, bg="#ffffff")
        self.end_button.grid(row=0, column=2, padx=5, pady=5)

        # Status Label
        self.status_label = tk.Label(master, text="Ready to Record", font=("Arial", 12), bg="#f0f0f0")
        self.status_label.pack(pady=10)

        # Color Button
        self.color_button = tk.Button(master, text="Change Color", command=self.change_color, width=10, bg="#ffffff")
        self.color_button.pack(pady=10)

        # New frame for output options
        output_frame = tk.Frame(master, bg="#f0f0f0")
        output_frame.pack(pady=10)

        # Folder selection
        self.folder_button = tk.Button(output_frame, text="Choose Folder", command=self.choose_folder, width=15, bg="#ffffff")
        self.folder_button.grid(row=0, column=0, padx=5, pady=5)

        self.folder_label = tk.Label(output_frame, text="No folder selected", bg="#f0f0f0", width=30)
        self.folder_label.grid(row=0, column=1, padx=5, pady=5)

        # File name input
        file_label = tk.Label(output_frame, text="File name:", bg="#f0f0f0")
        file_label.grid(row=1, column=0, padx=5, pady=5)

        self.file_entry = tk.Entry(output_frame, bg="#ffffff", width=30)
        self.file_entry.insert(0, "recorded_video.mp4")
        self.file_entry.grid(row=1, column=1, padx=5, pady=5)

        # Export Button
        self.export_button = tk.Button(output_frame, text="Export", command=self.export_video, width=15, bg="#ffffff")
        self.export_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        # Canvas for video display
        self.canvas = tk.Canvas(master, width=600, height=300)
        self.canvas.pack(pady=10)

        # Initialize variables
        self.video_capture = None
        self.recording = False
        self.output_video = None
        self.fps = None
        self.output_folder = None
        self.frames = []

    def choose_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.output_folder = folder
            self.folder_label.config(text=os.path.basename(folder))

    def start_recording(self):
        if not self.output_folder:
            self.status_label.config(text="Please select an output folder first")
            return

        self.fps = int(self.fps_entry.get())
        self.video_capture = cv2.VideoCapture(0)
        self.recording = True
        self.status_label.config(text="Recording Started")
        self.pause_button.config(state=tk.NORMAL)
        self.start_button.config(state=tk.DISABLED)
        self.end_button.config(state=tk.NORMAL)

        self.frames = []
        self.record_frame()

    def record_frame(self):
        if self.recording:
            ret, frame = self.video_capture.read()
            if ret:
                self.frames.append(frame)
                self.show_frame(frame)
                self.master.after(int(1000/self.fps), self.record_frame)
            else:
                self.end_recording()
                self.status_label.config(text="Error reading frames")

    def show_frame(self, frame):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = Image.fromarray(frame)
        frame = frame.resize((640, 480))
        photo = ImageTk.PhotoImage(image=frame)
        self.canvas.create_image(0, 0, image=photo, anchor=tk.NW)
        self.canvas.image = photo

    def pause_recording(self):
        self.recording = False
        self.status_label.config(text="Recording Paused")
        self.pause_button.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL)

    def end_recording(self):
        self.recording = False
        if self.video_capture:
            self.video_capture.release()
        self.status_label.config(text="Recording Ended")
        self.pause_button.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL)
        self.end_button.config(state=tk.DISABLED)

    def export_video(self):
        if not self.frames:
            self.status_label.config(text="No frames to export")
            return

        file_name = self.file_entry.get()
        if not file_name.endswith('.mp4'):
            file_name += '.mp4'
        
        output_path = os.path.join(self.output_folder, file_name)

        height, width, _ = self.frames[0].shape
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_path, fourcc, self.fps, (width, height))

        for frame in self.frames:
            out.write(frame)

        out.release()
        self.status_label.config(text=f"Video exported to {output_path}")

    def change_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            widgets_to_change = [self.master, self.title_frame, self.input_frame, self.button_frame, 
                                 self.status_label, self.color_button, self.fps_entry, 
                                 self.pause_button, self.start_button, self.end_button,
                                 self.folder_button, self.folder_label, self.file_entry]
            for widget in widgets_to_change:
                widget.configure(background=color)

# Create main window and run the app
root = tk.Tk()
app = FrameRecorder(root)
root.mainloop()
