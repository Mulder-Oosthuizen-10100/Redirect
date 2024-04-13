# Redirect GUI
import customtkinter as ctk
from PIL import Image
import tkinter as tk
from constants import ViewConstants

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")

# class HeadingFrame(ctk.CTkFrame):
#     def __init__(self, master, **kwargs):
#         super().__init__(master, **kwargs)

#         self.grid_columnconfigure(0, weight=1)
#         self.grid_rowconfigure(0, weight=1)            
        
#         # App Heading 
#         self.lbl_heading = ctk.CTkLabel(
#             master=self,
#             text="Redirect 404 URLs",
#             font=(ViewConstants.LabelFontFamily, ViewConstants.LabelFontSize),
#             anchor="center",
#         ).grid(
#             row=0,
#             column=0,
#             padx=20,
#             pady=20,
#             # sticky="ew",
#         )        

class ShopListFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        def checkbox1_event():
            print("checkbox1 toggled, current value:", self.check_var1.get())

        self.check_var1 = ctk.StringVar(value="off")

        # first shop check box
        self.chb_shop1 = ctk.CTkCheckBox(
            master=self,
            text="Shop 1",
            command=checkbox1_event,
            variable=self.check_var1,
            onvalue="on",
            offvalue="off",
        ).grid(
            row=0,
            column=0,
            padx=20,
            pady=20,
            # sticky="nesw",
        )

        def checkbox2_event():
            print("checkbox2 toggled, current value:", self.check_var2.get())

        self.check_var2 = ctk.StringVar(value="off")

        # first shop check box
        self.chb_shop2 = ctk.CTkCheckBox(
            master=self,
            text="Shop 1",
            command=checkbox2_event,
            variable=self.check_var2,
            onvalue="on",
            offvalue="off",
        ).grid(
            row=1,
            column=0,
            padx=20,
            pady=20,
            # sticky="nesw",
        )


class SourceFolderLocationFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((1,2,), weight=1)        

        self.lbl_source_folder_location = ctk.CTkLabel(
            master=self,
            text="Source Folder Location",
        ).grid(
            row=0,
            column=0,
            padx=20,
            pady=20,
            # sticky="nesw",
        )

        self.edt_source_folder_location = ctk.CTkEntry(
            master=self,
        ).grid(
            row=1,
            column=0,
            sticky="ew",
            padx=10,
            pady=10,
        )

        self.img_source_folder_location = ctk.CTkImage(
            dark_image=Image.open("./images/folder_location.png"),
            size=(20,20),
        )

        self.btn_source_folder_location = ctk.CTkButton(
            master=self,
            image=self.img_source_folder_location,
            text="",
            width=20,
            height=20,
        ).grid(
            row=1,
            column=1,
        )

        # self.btn_source_folder_location.image = self.img_source_folder_location



# my_image = customtkinter.CTkImage(light_image=Image.open("<path to light mode image>"),
#                                   dark_image=Image.open("<path to dark mode image>"),
#                                   size=(30, 30))

# image_label = customtkinter.CTkLabel(app, image=my_image, text="")  # display image with a CTkLabel



# path_picker_img = tk.PhotoImage(file = ASSETS_PATH / "path_picker.png")
# path_picker_button = tk.Button(
#     image = path_picker_img,
#     text = '',
#     compound = 'center',
#     fg = 'white',
#     borderwidth = 0,
#     highlightthickness = 0,
#     command = select_path,
#     relief = 'flat')


class DestinationFolderLocationFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((1,2,), weight=1)          

        self.lbl_destination_folder_location = ctk.CTkLabel(
            master=self,
            text="Destination Folder Location",
        ).grid(
            row=0,
            column=0,
            padx=20,
            pady=20,
            sticky="ew",
        )

        self.edt_destination_folder_location = ctk.CTkEntry(
            master=self,
        ).grid(
            row=1,
            column=0,
            sticky="ew",
            padx=10,
            pady=10,
        )

        self.img_destination_folder_location = ctk.CTkImage(
            dark_image=Image.open("./images/folder_location.png"),
            size=(20,20),
        )

        self.btn_destination_folder_location = ctk.CTkButton(
            master=self,
            image=self.img_destination_folder_location,
            text="",
            width=20,
            height=20,
        ).grid(
            row=1,
            column=1,
        )


class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Redirect 404 URLs")
        self.geometry("800x600")
        self.iconbitmap("Images/RedirectLogo.ico")
        
        self.grid_columnconfigure((0,1,), weight=1)
        
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure((1,2,3), weight=2)

        # self.grid_columnconfigure((0,2), weight=1)
        # self.grid_rowconfigure((0,3), weight=1)
        

        self.lbl_heading = ctk.CTkLabel(
            master=self,
            text="Redirect 404 URLs",
            font=(ViewConstants.LabelFontFamily, ViewConstants.LabelFontSize),
            # anchor="center",
        ).grid(
            row=0,
            column=0,
            columnspan=2,
            pady=20,
            sticky="nesw",
            # sticky="ew",
        )

        # self.frm_heading = HeadingFrame(
        #     master=self,
        #     corner_radius=16,
        # ).grid(
        #     row=0,
        #     column=0,
        #     columnspan=2,
        #     padx=10,
        #     pady=20,
        #     sticky="nesw",
        # )

        self.frm_shop_list = ShopListFrame(
            master=self,
            corner_radius=16,
        ).grid(
            row=1,
            rowspan=3,
            column=0,
            padx=(10,5),
            pady=(0,10),
            # padx=(10,40),
            sticky="nesw",
        )

        self.frm_source_location = SourceFolderLocationFrame(
            master=self,
            corner_radius=16,
        ).grid(
            row=1,
            column=1,
            padx=(5,10),
            pady=(0,10),
            sticky="nsew",
        )

        self.frm_destination_location = DestinationFolderLocationFrame(
            master=self,
            corner_radius=16,
        ).grid(
            row=2,
            column=1,
            padx=(5,10),
            pady=(0,10),
            sticky="nsew",
        )

        self.btn_generate_csv = ctk.CTkButton(
            master=self,
            corner_radius=20,
            text="Generate CSV File",
            width=100,
            height=50,            
        ).grid(
            row=3,
            column=1,
            # sticky="nsew",
        )

        # Shop list frame
        # self.frm_list_shop = ctk.CTkFrame(
            # master=self,
            # width=200,
            # height=400
        # )

        # self.frm_list_shop.grid(
            # row=1,
            # column=0,
            # padx=20
        # )

        # def checkbox_event():
        #     print("checkbox toggled, current value:", self.check_var1.get())

        # self.check_var1 = ctk.StringVar(value="on")
        # self.checkbox1 = ctk.CTkCheckBox(
        #     master=self.frm_list_shop,
        #     text="CTkCheckBox",
        #     command=checkbox_event,
        #     variable=self.check_var1,
        #     onvalue="on",
        #     offvalue="off"
        # )

        # self.checkbox1.grid(
        #     row=0,
        #     column=0,
        # )

        # self.check_var2 = ctk.StringVar(value="on")
        # self.checkbox2 = ctk.CTkCheckBox(
        #     master=self.frm_list_shop,
        #     text="CTkCheckBox",
        #     command=checkbox_event,
        #     variable=self.check_var2,
        #     onvalue="on",
        #     offvalue="off"
        # )

        # self.checkbox2.grid(
        #     row=1,
        #     column=0,
        #     pady=20,
        #     padx=20
        # )


app = App()
app.mainloop()


# root.geometry("800x600")
# root.grid_columnconfigure((0,1), weight=1)

# frame = customtkinter.CTkFrame(
#     master=root,
#     width=200, 
#     height=200
# )

# lbl_heading = customtkinter.CTkLabel(
#     master=root,
#     corner_radius=16,
#     text="Redirect 404 URLs",
#     font=(ViewConstants.LabelFontFamily, ViewConstants.LabelFontSize)
# )

# def generate_redirect_file():
#     return 1

# btn_create_redirects = customtkinter.CTkButton(
#     master=root,
#     text="Create Redirect File",
#     command= generate_redirect_file,
#     font=(ViewConstants.ButtonFontFamily, ViewConstants.ButtonFontSize)
# )

# checkbox_1 = customtkinter.CTkCheckBox(root, text="checkbox 1")
# checkbox_1.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")
# checkbox_2 = customtkinter.CTkCheckBox(root, text="checkbox 2")
# checkbox_2.grid(row=1, column=1, padx=20, pady=(0, 20), sticky="w")

# lbl_heading.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)
# # btn_create_redirects.grid(row=6, column=5, padx=20, pady=20)#.pack(pady=20)
# # frame.pack(pady=20)


# root.mainloop()


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