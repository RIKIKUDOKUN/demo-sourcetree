import tkinter as tk
from tkinter import messagebox, ttk
import re

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Registration Form")
        self.geometry("600x700")
        self.configure(background="#f0f0f0")

        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('TButton', background='#007bff', foreground='white')
        self.style.map('TButton', background=[('active', '#0056b3')])

        self.create_widgets()

    def create_widgets(self):
        # Create main frame
        main_frame = ttk.Frame(self, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Create and pack frames
        self.user_info_frame = ttk.LabelFrame(main_frame, text="User Information", padding="10")
        self.user_info_frame.pack(fill="x", pady=10)

        self.registration_frame = ttk.LabelFrame(main_frame, text="Registration Details", padding="10")
        self.registration_frame.pack(fill="x", pady=10)

        self.terms_frame = ttk.LabelFrame(main_frame, text="Terms and Conditions", padding="10")
        self.terms_frame.pack(fill="x", pady=10)

        # User Information Fields
        self.create_entry("Tên:", "name_entry")
        self.create_entry("Họ:", "surname_entry")
        self.create_entry("Chức danh:", "position_entry")
        self.create_entry("Tuổi:", "age_entry")
        self.create_entry("Quốc tịch:", "nationality_entry")
        self.create_entry("Email:", "email_entry")

        # Registration Fields
        ttk.Label(self.registration_frame, text="Trạng thái đăng ký:").grid(row=0, column=0, sticky="w")
        self.registration_status_var = tk.StringVar(value="Not Registered")
        ttk.Radiobutton(self.registration_frame, text="Đã đăng ký", variable=self.registration_status_var, value="Registered").grid(row=0, column=1)
        ttk.Radiobutton(self.registration_frame, text="Chưa đăng ký", variable=self.registration_status_var, value="Not Registered").grid(row=0, column=2)

        ttk.Label(self.registration_frame, text="Số khóa học đã hoàn thành:").grid(row=1, column=0, sticky="w")
        self.completed_courses_var = tk.IntVar()
        ttk.Spinbox(self.registration_frame, from_=0, to=10, width=5, textvariable=self.completed_courses_var).grid(row=1, column=1)

        ttk.Label(self.registration_frame, text="Học kỳ:").grid(row=2, column=0, sticky="w")
        self.semester_var = tk.IntVar(value=1)
        ttk.Spinbox(self.registration_frame, from_=1, to=10, width=5, textvariable=self.semester_var).grid(row=2, column=1)

        # Terms and Conditions
        self.terms_var = tk.BooleanVar()
        ttk.Checkbutton(self.terms_frame, text="Tôi đồng ý với các điều khoản và điều kiện", variable=self.terms_var).pack()

        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(pady=10)

        self.submit_button = ttk.Button(button_frame, text="Gửi", command=self.submit_data)
        self.submit_button.pack(side=tk.LEFT, padx=5)

        self.clear_button = ttk.Button(button_frame, text="Xóa", command=self.clear_all)
        self.clear_button.pack(side=tk.LEFT, padx=5)

        # Progress bar
        self.progress = ttk.Progressbar(main_frame, orient="horizontal", length=200, mode="determinate")
        self.progress.pack(pady=10)

    def create_entry(self, label, attribute_name):
        ttk.Label(self.user_info_frame, text=label).pack(anchor="w")
        entry = ttk.Entry(self.user_info_frame, width=30)
        entry.pack(fill="x", padx=5, pady=5)
        setattr(self, attribute_name, entry)

    def submit_data(self):
        if not self.validate_fields():
            return

        self.progress["value"] = 0
        self.update_idletasks()

        # Simulate processing
        for i in range(5):
            self.progress["value"] += 20
            self.update_idletasks()
            self.after(500)  # Wait for 500 ms

        messagebox.showinfo("Success", "Data submitted successfully!")
        self.progress["value"] = 0

    def clear_all(self):
        for attr in ["name_entry", "surname_entry", "position_entry", "age_entry", "nationality_entry", "email_entry"]:
            getattr(self, attr).delete(0, tk.END)

        self.registration_status_var.set("Not Registered")
        self.completed_courses_var.set(0)
        self.semester_var.set(1)
        self.terms_var.set(False)
        self.progress["value"] = 0

    def validate_fields(self):
        if not all([self.name_entry.get(), self.surname_entry.get(), self.age_entry.get(), self.email_entry.get()]):
            messagebox.showerror("Error", "Please fill in all required fields.")
            return False

        if not self.age_entry.get().isdigit():
            messagebox.showerror("Error", "Age must be a number.")
            return False

        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.email_entry.get()):
            messagebox.showerror("Error", "Please enter a valid email address.")
            return False

        if not self.terms_var.get():
            messagebox.showerror("Error", "You must agree to the terms and conditions.")
            return False

        return True

if __name__ == "__main__":
    app = Application()
    app.mainloop()
