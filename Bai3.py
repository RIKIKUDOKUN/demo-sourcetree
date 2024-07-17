import tkinter as tk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Registration Form")
        self.geometry("500x400")
        self.configure(background="#f0f0f0")  # Light gray background

        # Create frames
        self.user_info_frame = tk.Frame(self, bg="#ccefff")  # Light blue background
        self.registration_frame = tk.Frame(self, bg="#ccefff")  # Light blue background
        self.terms_frame = tk.Frame(self, bg="#ccefff")  # Light blue background

        # Create user information fields
        tk.Label(self.user_info_frame, text="Tên:", fg="blue").grid(row=0, column=0)  # Blue text
        self.name_entry = tk.Entry(self.user_info_frame, width=20, bg="#fff", fg="black")  # White background, black text
        self.name_entry.grid(row=0, column=1)

        tk.Label(self.user_info_frame, text="Họ:", fg="blue").grid(row=1, column=0)  # Blue text
        self.surname_entry = tk.Entry(self.user_info_frame, width=20, bg="#fff", fg="black")  # White background, black text
        self.surname_entry.grid(row=1, column=1)

        tk.Label(self.user_info_frame, text="Chức danh:", fg="blue").grid(row=2, column=0)  # Blue text
        self.position_entry = tk.Entry(self.user_info_frame, width=20, bg="#fff", fg="black")  # White background, black text
        self.position_entry.grid(row=2, column=1)

        tk.Label(self.user_info_frame, text="Tuổi:", fg="blue").grid(row=3, column=0)  # Blue text
        self.age_entry = tk.Entry(self.user_info_frame, width=20, bg="#fff", fg="black")  # White background, black text
        self.age_entry.grid(row=3, column=1)

        tk.Label(self.user_info_frame, text="Quốc tịch:", fg="blue").grid(row=4, column=0)  # Blue text
        self.nationality_entry = tk.Entry(self.user_info_frame, width=20, bg="#fff", fg="black")  # White background, black text
        self.nationality_entry.grid(row=4, column=1)

        # Create registration fields
        tk.Label(self.registration_frame, text="Trạng thái đăng ký:", fg="blue").grid(row=0, column=0)  # Blue text
        self.registration_status_var = tk.IntVar()
        tk.Checkbutton(self.registration_frame, variable=self.registration_status_var, bg="#ccefff", fg="blue").grid(row=0, column=1)  # Light blue background, blue text

        tk.Label(self.registration_frame, text="Số khóa học đã hoàn thành:", fg="blue").grid(row=1, column=0)  # Blue text
        self.completed_courses_var = tk.IntVar()
        tk.Spinbox(self.registration_frame, from_=0, to=10, width=5, textvariable=self.completed_courses_var, bg="#fff", fg="black").grid(row=1, column=1)  # White background, black text

        tk.Label(self.registration_frame, text="Học kỳ:", fg="blue").grid(row=2, column=0)  # Blue text
        self.semester_var = tk.IntVar()
        tk.Spinbox(self.registration_frame, from_=1, to=10, width=5, textvariable=self.semester_var, bg="#fff", fg="black").grid(row=2, column=1)  # White background, black text

        # Create terms and conditions field
        tk.Label(self.terms_frame, text="Chấp nhận các điều khoản và điều kiện:", fg="blue").grid(row=0, column=0)  # Blue text
        self.terms_var = tk.IntVar()
        tk.Checkbutton(self.terms_frame, variable=self.terms_var, bg="#ccefff", fg="blue").grid(row=0, column=1)  # Light blue background, blue text

        # Pack frames
        self.user_info_frame.pack(fill="x", pady=10)
        self.registration_frame.pack(fill="x", pady=10)
        self.terms_frame.pack(fill="x", pady=10)

        # Create submit and clean buttons
        self.submit_button = tk.Button(self, text="Gửi", command=self.submit_data, bg="#007bff", fg="white")  # Blue background, white text
        self.submit_button.pack(pady=10)
        self.clean_button = tk.Button(self, text="Xóa", command=self.clear_all, bg="#007bff", fg="white")  # Blue background, white text
        self.clean_button.pack(pady=10)
        def submit_data(self):
         print("Data submitted!")

    def clear_all(self):
        # Clear all user information entries
        self.name_entry.delete(0, tk.END)
        self.surname_entry.delete(0, tk.END)
        # ... (similar code to clear all other user information entries)

        # Clear registration fields (if applicable)
        self.registration_status_var.set(0)  # Reset checkbox selection
        self.completed_courses_var.set(0)  # Set completed courses to 0
        self.semester_var.set(0)  # Set semester to 0

        # Clear terms checkbox selection
        self.terms_var.set(0)
    def submit_data(self):
        print("Data submitted!")
       

if __name__ == "__main__":
    app = Application()
    app.mainloop()