import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime
from PIL import Image, ImageTk
from course import CourseClass
from student import studentClass
from result import resultClass
from report import reportClass
import login

class RMS:
    def __init__(self, root, role):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        self.role = role  # Admin or Student

        # Load and set the logo image
        self.logo_dash = ImageTk.PhotoImage(file="images/logo_p.png")

        # Title
        title = tk.Label(self.root, text="Student Result Management System", padx=10, compound=tk.LEFT, image=self.logo_dash, font=("goudy old style", 20, "bold"), bg="#033054", fg="white")
        title.place(x=0, y=0, relwidth=1, height=50)

        # Menu
        M_frame = tk.LabelFrame(self.root, text="Menus", font=("times new roman", 15), bg="white")
        M_frame.place(x=10, y=70, width=1340, height=80)

        # Buttons inside the menu frame
        if self.role == 'admin':
            btn_course = tk.Button(M_frame, text="Course", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add_course)
            btn_course.place(x=20, y=5, width=200, height=40)
            btn_student = tk.Button(M_frame, text="Student", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add_student)
            btn_student.place(x=240, y=5, width=200, height=40)
            btn_result = tk.Button(M_frame, text="Result", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add_result)
            btn_result.place(x=460, y=5, width=200, height=40)
        btn_view = tk.Button(M_frame, text="View", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add_report)
        btn_view.place(x=680, y=5, width=200, height=40)
        btn_logout = tk.Button(M_frame, text="Logout", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.logout)
        btn_logout.place(x=900, y=5, width=200, height=40)
        btn_exit = tk.Button(M_frame, text="Exit", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.root.quit)
        btn_exit.place(x=1120, y=5, width=200, height=40)

        # Content window background image
        self.bg_img = Image.open("images/bg.png")
        self.bg_img = self.bg_img.resize((920, 350))
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg = tk.Label(self.root, image=self.bg_img)
        self.lbl_bg.place(x=400, y=180, width=920, height=350)

        # Update details
        self.lbl_course = tk.Label(self.root, text="Total Courses\n[ 0 ]", font=("goudy old style", 20), bd=10, relief=tk.RIDGE, bg="#e43b06", fg="white")
        self.lbl_course.place(x=400, y=530, width=300, height=100)

        self.lbl_student = tk.Label(self.root, text="Total Students\n[ 0 ]", font=("goudy old style", 20), bd=10, relief=tk.RIDGE, bg="#0676ad", fg="white")
        self.lbl_student.place(x=710, y=530, width=300, height=100)

        self.lbl_result = tk.Label(self.root, text="Total Results\n[ 0 ]", font=("goudy old style", 20), bd=10, relief=tk.RIDGE, bg="#038074", fg="white")
        self.lbl_result.place(x=1020, y=530, width=300, height=100)

        # Footer
        footer = tk.Label(self.root, text="SRMS - Student Result Management System\nContact us for any Technical Issues: 939061516x", font=("goudy old style", 12), bg="#262626", fg="white")
        footer.pack(side=tk.BOTTOM, fill=tk.X)

        # Load initial data
        self.load_data()

    def load_data(self):
        # Load total courses, students, and results
        total_courses = self.get_total("courses")
        total_students = self.get_total("student")
        total_results = self.get_total("result")

        # Update labels
        self.lbl_course.config(text=f"Total Courses\n[ {total_courses} ]")
        self.lbl_student.config(text=f"Total Students\n[ {total_students} ]")
        self.lbl_result.config(text=f"Total Results\n[ {total_results} ]")

    def get_total(self, table):
        try:
            con = sqlite3.connect("rms.db")
            cur = con.cursor()
            cur.execute(f"SELECT COUNT(*) FROM {table}")
            total = cur.fetchone()[0]
            return total
        except Exception as e:
            print(f"Error fetching total {table}: {e}")
            return 0
        finally:
            con.close()

    def add_course(self):
        self.new_win = tk.Toplevel(self.root)
        self.new_obj = CourseClass(self.new_win)

    def add_student(self):
        self.new_win = tk.Toplevel(self.root)
        self.new_obj = studentClass(self.new_win)

    def add_result(self):
        self.new_win = tk.Toplevel(self.root)
        self.new_obj = resultClass(self.new_win)

    def add_report(self):
        self.new_win = tk.Toplevel(self.root)
        self.new_obj = reportClass(self.new_win)

    def logout(self):
        self.root.destroy()
        login_root = tk.Tk()
        login_app = login.LoginApp(login_root)
        login_root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = RMS(root, role='admin')  # Example role
    root.mainloop()
