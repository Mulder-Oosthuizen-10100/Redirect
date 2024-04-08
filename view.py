# Redirect GUI

from tkinter import *
import customtkinter
from constants import ViewConstants

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title('Redirect 404 URLs')
root.iconbitmap('Images/RedirectLogo.ico')
root.geometry("800x600")


def generate_redirect_file():
    return 1

btn_create_redirects = customtkinter.CTkButton(
    root,
    text="Create Redirect File",
    command= generate_redirect_file,
    font=(ViewConstants.ButtonFontFamily, ViewConstants.ButtonFontSize)
)

btn_create_redirects.pack(pady=80)


root.mainloop()