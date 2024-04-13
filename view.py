import customtkinter as ctk
from tkinter import filedialog
import os
from PIL import Image
from constants import ViewConstants

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")

class ShopListFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, controller, lst_shop_names=["Shop 1", "Shop 2", "Shop 3", "Shop 4", "Shop 5"], **kwargs):
        super().__init__(master, **kwargs)

        self.controller = controller
        self.rdbtn_variable = ctk.IntVar(value=0)
        self.rdbtn_list = []
        self.row_count = 0
        for shop_name in lst_shop_names:
            itm = ctk.CTkRadioButton(
                master=self,
                text=shop_name,
                command=self.shop_selected(), #self.controller.set_shop_name(self.rdbtn_variable.get()),
                # command=lambda:self.rdbtn_variable.get(),
                variable=self.rdbtn_variable,
                value=self.row_count,
            ).grid(
                row=self.row_count,
                column=0,
            )
            self.rdbtn_list.append(itm)
            self.row_count += 1

        # def radiobutton_event():
        #     print("radiobutton toggled, current value:", radio_var.get())

        # radio_var = tkinter.IntVar(value=0)
        # radiobutton_1 = customtkinter.CTkRadioButton(app, text="CTkRadioButton 1",
        #                                             command=radiobutton_event, variable= radio_var, value=1)
        # radiobutton_2 = customtkinter.CTkRadioButton(app, text="CTkRadioButton 2",
        #                                             command=radiobutton_event, variable= radio_var, value=2)        

    
    def shop_selected(self):
        self.controller.set_shop_name(self.rdbtn_variable.get())
        # print(f"value: {self.rdbtn_variable.get()}")

class SourceFolderLocationFrame(ctk.CTkFrame):
    def __init__(self, master, controller, **kwargs):
        super().__init__(master, **kwargs)

        self.controller = controller
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0,1,), weight=1)

        self.lbl_source_folder_location = ctk.CTkLabel(
            master=self,
            text="Source Folder Location",
            font=('JetBrains Mono',18),
        ).grid(
            row=0,
            column=0,
            columnspan=2,
            padx=20,
            sticky="w",
        )

        self.edt_source_folder_location = ctk.CTkEntry(
            master=self,
            font=('JetBrains Mono',14),
        ).grid(
            row=1,
            column=0,
            sticky="ew",
            padx=(20,5),
            pady=(0,10),
        )

        self.img_source_folder_location = ctk.CTkImage(
            dark_image=Image.open("./images/folder_location.png"),
            size=(20,20),
        )

        self.btn_source_folder_location = ctk.CTkButton(
            master=self,
            image=self.img_source_folder_location,
            text="",
            command=self.open_source_file,
            width=20,
            height=20,
        ).grid(
            row=1,
            column=1,
            padx=(5,20),
            pady=(0,10),
        )

    def open_source_file(self):
        file_name = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            defaultextension=".txt",
            filetypes=[("Text Files",".txt")],
        )
        if file_name:
            self.controller.set_source_file_name(file_name)

class DestinationFolderLocationFrame(ctk.CTkFrame):
    def __init__(self, master, controller, **kwargs):
        super().__init__(master, **kwargs)

        self.controller = controller
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0,1,), weight=1)

        self.lbl_destination_folder_location = ctk.CTkLabel(
            master=self,
            text="Destination Folder Location",
            font=('JetBrains Mono',18),
        ).grid(
            row=0,
            column=0,
            columnspan=2,
            padx=20,
            sticky="w",
        )

        self.edt_destination_folder_location = ctk.CTkEntry(
            master=self,
            font=('JetBrains Mono',14),
        ).grid(
            row=1,
            column=0,
            sticky="ew",
            padx=(20,5),
            pady=(0,10),
        )

        self.img_destination_folder_location = ctk.CTkImage(
            dark_image=Image.open("./images/folder_location.png"),
            size=(20,20),
        )

        self.btn_destination_folder_location = ctk.CTkButton(
            master=self,
            image=self.img_destination_folder_location,
            text="",
            command=self.open_destination_folder,
            width=20,
            height=20,
        ).grid(
            row=1,
            column=1,
            padx=(5,20),
            pady=(0,10),
        )
    
    def open_destination_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.controller.set_destination_folder(folder)

class MainWindow(ctk.CTk):
    def __init__(self, controller, *args, **kwargs):
        super().__init__(*args, **kwargs)
       
        self.controller = controller
        self.title("Redirect 404 URLs")
        self.geometry("1000x600")
        self.iconbitmap("Images/RedirectLogo.ico")
        self.resizable(
            height=False,
            width=False,
        )
        
        self.grid_columnconfigure(0, weight=6)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure((1,2,3), weight=2)

        self.lbl_heading = ctk.CTkLabel(
            master=self,
            text="Redirect 404 URLs",
            font=(ViewConstants.LabelFontFamily, ViewConstants.LabelFontSize),
        ).grid(
            row=0,
            column=0,
            columnspan=2,
            pady=20,
            sticky="nesw",
        )

        self.frm_shop_list = ShopListFrame(
            controller=controller,
            master=self,
            corner_radius=16,
        ).grid(
            row=1,
            rowspan=3,
            column=0,
            padx=(10,10),
            pady=(0,10),
            sticky="nesw",
        )

        self.frm_source_location = SourceFolderLocationFrame(
            controller=controller,
            master=self,
            corner_radius=16,
        ).grid(
            row=1,
            column=1,
            padx=60,
            pady=(0,60),
            sticky="nsew",
        )

        self.frm_destination_location = DestinationFolderLocationFrame(
            controller=controller,
            master=self,
            corner_radius=16,
        ).grid(
            row=2,
            column=1,
            padx=60,
            pady=(0,60),
            sticky="nsew",
        )

        self.btn_generate_csv = ctk.CTkButton(
            master=self,
            corner_radius=20,
            text="Generate CSV File",
            font=('JetBrains Mono',18),
            command=self.controller.generate_csv_file,
            width=100,
            height=50,            
        ).grid(
            row=3,
            column=1,
            padx=60,
            pady=(0,60),
        )        

# MVC - View Class
class RedirectView:
    def __init__(self, controller):
        self.controller = controller
        self.root = MainWindow(controller=controller)