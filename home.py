from tkinter import *
from tkinter import messagebox


def click():
    messagebox.showinfo("showinfo", "button clicked")


login_window = Tk()
login_window.title("Login")
login_window.geometry("500x500")
login_button = Button(login_window, font=50, text="login", fg="#ff0000", command=click)
login_button.pack(side="left")
login_window.mainloop()
