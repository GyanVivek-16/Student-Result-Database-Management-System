from tkinter import *
from tkinter import messagebox
import sqlite3
import dashboard
from PIL import Image, ImageTk

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page")
        self.root.geometry("400x300")
        
        # Load background image
        self.bg_image = Image.open("images/login_bg.png")  # Replace with your image path
        self.bg_image = self.bg_image.resize((400, 300))
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        # Background Label
        self.bg_label = Label(root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Title Label
        self.title_label = Label(root, text="Login to SRMS", font=("Arial", 20, "bold"), bg="#033054", fg="white")
        self.title_label.pack(pady=10)

        # Frame for login form
        self.login_frame = Frame(root, bg="white")
        self.login_frame.pack(pady=20)

        # Email Label and Entry
        self.label_email = Label(self.login_frame, text="Email ID", font=("Arial", 14), bg="white")
        self.label_email.grid(row=0, column=0, pady=10, padx=10, sticky="w")
        self.entry_email = Entry(self.login_frame, font=("Arial", 14))
        self.entry_email.grid(row=0, column=1, pady=10, padx=10)

        # Password Label and Entry
        self.label_password = Label(self.login_frame, text="Password", font=("Arial", 14), bg="white")
        self.label_password.grid(row=1, column=0, pady=10, padx=10, sticky="w")
        self.entry_password = Entry(self.login_frame, font=("Arial", 14), show="*")
        self.entry_password.grid(row=1, column=1, pady=10, padx=10)

        # Login Button
        self.btn_login = Button(root, text="Login", font=("Arial", 14), bg="#0b5377", fg="white", command=self.login)
        self.btn_login.pack(pady=10)

        # Forgot Password Button
        self.btn_forgot_password = Button(root, text="Forgot Password?", font=("Arial", 10), bg="white", fg="#0b5377", command=self.forgot_password)
        self.btn_forgot_password.pack(pady=5)

    def login(self):
        email = self.entry_email.get()
        password = self.entry_password.get()

        # Here you would typically check the email and password against a database
        if email == "admin@example.com" and password == "password":
            messagebox.showinfo("Login Success", "Logged in successfully!")
            self.open_dashboard(admin=True)
        elif email == "student@example.com" and password == "password":
            messagebox.showinfo("Login Success", "Logged in successfully!")
            self.open_dashboard(admin=False)
        else:
            messagebox.showerror("Login Failed", "Invalid email or password")

    def open_dashboard(self, admin):
        self.root.destroy()
        dashboard_root = Tk()
        if admin:
            app = dashboard.RMS(dashboard_root, role='admin')
        else:
            app = dashboard.RMS(dashboard_root, role='student')
        dashboard_root.mainloop()

    def forgot_password(self):
        email = self.entry_email.get()
        if email:
            messagebox.showinfo("Forgot Password", f"Password reset link sent to {email}")
        else:
            messagebox.showwarning("Forgot Password", "Please enter your email ID")

if __name__ == "__main__":
    root = Tk()
    app = LoginApp(root)
    root.mainloop()
