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
root.grid_columnconfigure((0,1), weight=1)

frame = customtkinter.CTkFrame(
    master=root,
    width=200, 
    height=200
)

lbl_heading = customtkinter.CTkLabel(
    master=root,
    corner_radius=16,
    text="Redirect 404 URLs",
    font=(ViewConstants.LabelFontFamily, ViewConstants.LabelFontSize)
)

def generate_redirect_file():
    return 1

btn_create_redirects = customtkinter.CTkButton(
    master=root,
    text="Create Redirect File",
    command= generate_redirect_file,
    font=(ViewConstants.ButtonFontFamily, ViewConstants.ButtonFontSize)
)

checkbox_1 = customtkinter.CTkCheckBox(root, text="checkbox 1")
checkbox_1.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")
checkbox_2 = customtkinter.CTkCheckBox(root, text="checkbox 2")
checkbox_2.grid(row=1, column=1, padx=20, pady=(0, 20), sticky="w")

lbl_heading.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)
# btn_create_redirects.grid(row=6, column=5, padx=20, pady=20)#.pack(pady=20)
# frame.pack(pady=20)


root.mainloop()


# class App(customtkinter.CTk):
#     def __init__(self):
#         super().__init__()

#         self.title("my app")
#         self.geometry("400x150")
#         self.grid_columnconfigure((0, 1), weight=1)

#         self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callback)
#         self.button.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)
#         self.checkbox_1 = customtkinter.CTkCheckBox(self, text="checkbox 1")
#         self.checkbox_1.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")
#         self.checkbox_2 = customtkinter.CTkCheckBox(self, text="checkbox 2")
#         self.checkbox_2.grid(row=1, column=1, padx=20, pady=(0, 20), sticky="w")
        
#     def button_callback(self):
#         print("button pressed")

# app = App()
# app.mainloop()