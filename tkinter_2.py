import tkinter as tk
from tkinter import messagebox as mb

def login():
    login_window = tk.Toplevel(root)
    login_window.title("Login")
    login_window.geometry("300x200")

    tk.Label(login_window,text="username").pack(padx=5)
    username=tk.Entry(login_window)
    username.pack()

    tk.Label(login_window,text="pas").pack(pady=10)
    pas=tk.Entry(login_window)
    pas.pack()

    def show():
        mb.showerror("login failed","no user found")
    button=tk.Button(login_window,text="login",command=show)
    button.pack()

    

def signup():
    sign=tk.Toplevel(root)
    sign.title("sign up")
    sign.geometry("350x400")
    tk.Label(sign,text="name").pack(padx=5,pady=5)
    name=tk.Entry(sign)
    name.pack()
    tk.Label(sign,text="email").pack(padx=3,pady=3)
    email=tk.Entry(sign)
    email.pack()

    tk.Label(sign, text="Password").pack(pady=3)
    password=tk.Entry(sign)
    password.pack()

    def save():
        with open("HIIII.txt", "a") as f:
            f.write(name.get() + "\n")

    def save():
        with open("HIIII.txt", "a") as f:
            f.write(email.get() + "\n")

    def save():
        with open("HIIII.txt", "a") as f:
            f.write(password.get() + "\n")

    tk.Label(sign, text="Confirm Password").pack(pady=3)
    confirm = tk.Entry(sign)
    confirm.pack()

    button=tk.Button(sign, text="Register", command=save)
    button.pack()
    
root = tk.Tk()

root.title("User")
root.geometry("250x150")

tk.Label(root, text="Choose an option:").pack(pady=10)

tk.Button(root, text="Login", command=login).pack(pady=5)
tk.Button(root, text="SignUp", command=signup).pack(pady=5)

root.mainloop()

