import customtkinter as ctk
from tkinter import filedialog
import os
from PIL import Image
from constants import ViewConstants

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")

class ShopListFrame(ctk.CTkScrollableFrame):
    def __init__(
            self,
            master,
            controller,
            # lst_dict_websites,
            **kwargs
        ):
        super().__init__(master, **kwargs)

        self.controller = controller
        self.grid_columnconfigure(0, weight=1)
        self.lst_rdbtn_shops = []
        self.rdbtn_var = ctk.StringVar(value="off")
        self.row_count = 0

        self.lbl_loading = ctk.CTkLabel(
            master=self,
            text="Loading",
            font=('JetBrains Mono', 18),
        )

        self.lbl_loading.grid(
            row=0,
            column=0,
        )

    def add_shops(self, lst_dict_websites):
        self.lbl_loading.destroy()
        for shop in lst_dict_websites:
            self.grid_rowconfigure(self.row_count, weight=1)
            self.lst_rdbtn_shops.append(
                ctk.CTkRadioButton(
                    master=self,
                    text=shop.get('WEBSITE'),
                    font=('JetBrains Mono',14),
                    variable=self.rdbtn_var,
                    value=shop.get('WEBSITE'),
                    command=self.rdbtn_selected,
                ).grid(
                    row=self.row_count,
                    column=0,
                    pady=(20,0),
                    padx=20,
                    sticky='ew',
                )
            )
            self.row_count += 1

    def rdbtn_selected(self):
        self.controller.set_shop_name(
            self.rdbtn_var.get()
        )

class SourceFolderLocationFrame(ctk.CTkFrame):
    def __init__(self, master, controller, **kwargs):
        super().__init__(master, **kwargs)

        self.controller = controller
        self.edt_text_var = ctk.StringVar(value="c:/projects/redirect/source.txt")
        self.controller.set_source_file_name(self.edt_text_var.get())
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
            textvariable=self.edt_text_var,
        ).grid(
            row=1,
            column=0,
            sticky="ew",
            padx=(20,5),
            pady=(0,10),
        )

        self.img_source_folder_location = ctk.CTkImage(
            dark_image=Image.open(self.controller.resource_path(".\\images\\folder_location.png")),
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
            self.update_edt_source_folder_location(file_name)

    def update_edt_source_folder_location(self, new_text=""):
        self.edt_text_var.set(new_text)

class RedirectFolderLocationFrame(ctk.CTkFrame):
    def __init__(self, master, controller, **kwargs):
        super().__init__(master, **kwargs)

        self.controller = controller
        self.edt_text_var = ctk.StringVar(value="c:/projects/redirect/redirects")
        self.controller.set_redirect_folder_name(self.edt_text_var.get())
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0,1,), weight=1)

        self.lbl_redirect_folder_location = ctk.CTkLabel(
            master=self,
            text="Redirect Folder Location",
            font=('JetBrains Mono',18),
        ).grid(
            row=0,
            column=0,
            columnspan=2,
            padx=20,
            sticky="w",
        )

        self.edt_redirect_folder_location = ctk.CTkEntry(
            master=self,
            font=('JetBrains Mono',14),
            textvariable=self.edt_text_var,
        ).grid(
            row=1,
            column=0,
            sticky="ew",
            padx=(20,5),
            pady=(0,10),
        )

        self.img_redirect_folder_location = ctk.CTkImage(
            dark_image=Image.open(self.controller.resource_path(".\\images\\folder_location.png")),
            size=(20,20),
        )

        self.btn_redirect_folder_location = ctk.CTkButton(
            master=self,
            image=self.img_redirect_folder_location,
            text="",
            command=self.open_redirect_folder,
            width=20,
            height=20,
        ).grid(
            row=1,
            column=1,
            padx=(5,20),
            pady=(0,10),
        )
    
    def open_redirect_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.controller.set_redirect_folder_name(folder)
            self.update_edt_redirect_folder_location(folder)
    
    def update_edt_redirect_folder_location(self, new_text=""):
        self.edt_text_var.set(new_text)

class MainWindow(ctk.CTk):
    def __init__(
            self,
            controller,
            # lst_dict_websites,
            *args,
            **kwargs
        ):
        super().__init__(*args, **kwargs)
       
        self.controller = controller
        self.title("Redirect 404 URLs")
        self.geometry("1000x600")
        self.iconbitmap(self.controller.resource_path("images\\RedirectLogo.ico"))
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
            # lst_dict_websites=lst_dict_websites,
            corner_radius=16,
        )
        
        self.frm_shop_list.grid(
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

        self.frm_redirect_location = RedirectFolderLocationFrame(
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

class SplashWindow(ctk.CTk):
    def __init__(
            self,
            controller,
            *args,
            **kwargs
        ):
        super().__init__(*args, **kwargs)
       
        self.controller = controller
        self.title("Redirect 404 URLs")
        self.geometry("1000x600")
        self.iconbitmap(self.controller.resource_path("images\\RedirectLogo.ico"))
        self.resizable(
            height=False,
            width=False,
        )
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.lbl_heading = ctk.CTkLabel(
            master=self,
            text="Redirect 404 URLs",
            font=(ViewConstants.LabelFontFamily, ViewConstants.LabelFontSize),
        ).grid(
            row=0,
            column=0,
            pady=20,
            sticky="nesw",
        )

# MVC - View Class
class RedirectView:
    def __init__(
            self,
            controller,
            # lst_dict_websites,
            # is_splash=True,
        ):
        self.controller = controller
        # self.lst_dict_websites = lst_dict_websites
        # self.is_splash = is_splash
        # self.create_window()
    
    # def refresh(self):
        # self.root.destroy()
        # self.create_window()

    # def create_window(self):
        # if self.is_splash:
            # self.root = SplashWindow(
                # controller=self.controller,
            # )
        # else:
        self.root = MainWindow(
            controller=self.controller,
                # lst_dict_websites=self.lst_dict_websites,
        )
        # self.root.eval('tk::PlaceWindow . center')
    
    # def destroy(self):
        # self.root.destroy()
    
    # def hide(self):
        # self.root.withdraw()



# class MainWindow(ctk.CTk):
#     pass

# class MainView():
#     pass

# class RedirectTopLevelWindow(ctk.CTkToplevel):
#     pass

# class RedirectTopLevelView():
#     pass


# class MainWindow(ctk.CTk):
#     def __init__(
#             self,
#             controller,
#             *args,
#             **kwargs
#         ):
#         super().__init__(*args, **kwargs)
       
#         self.controller = controller
#         self.title("Redirect 404 URLs")
#         self.geometry("1000x600")
#         # self.iconbitmap(self.controller.resource_path("images\\RedirectLogo.ico"))
#         self.resizable(
#             height=False,
#             width=False,
#         )
        
#         self.grid_columnconfigure(0, weight=6)
#         self.grid_columnconfigure(1, weight=1)
#         self.grid_rowconfigure(0, weight=0)

#         self.lbl_heading = ctk.CTkLabel(
#             master=self,
#             text="Redirect 404 URLs",
#             font=(ViewConstants.LabelFontFamily, ViewConstants.LabelFontSize),
#         ).grid(
#             row=0,
#             column=0,
#             columnspan=2,
#             pady=20,
#             sticky="nesw",
#         )

# class MainView():
#     def __init__(self, controller):
#         self.controller = controller       
#         self.root = MainWindow(controller=self)

# class SplashWindow(ctk.CTk):
#     def __init__(
#             self,
#             controller,
#             *args,
#             **kwargs
#         ):
#         super().__init__(*args, **kwargs)
       
#         self.controller = controller
#         self.title("Loading")
#         self.geometry("1000x600")
#         # self.iconbitmap(self.controller.resource_path("images\\RedirectLogo.ico"))
#         self.resizable(
#             height=False,
#             width=False,
#         )
        
#         self.grid_columnconfigure(0, weight=6)
#         self.grid_columnconfigure(1, weight=1)
#         self.grid_rowconfigure(0, weight=0)

#         self.lbl_heading = ctk.CTkLabel(
#             master=self,
#             text="Loading",
#             font=(ViewConstants.LabelFontFamily, ViewConstants.LabelFontSize),
#         ).grid(
#             row=0,
#             column=0,
#             columnspan=2,
#             pady=20,
#             sticky="nesw",
#         )

# class SplashView():
#     def __init__(self, controller):
#         self.controller = controller       
#         self.root = SplashWindow(controller=self)