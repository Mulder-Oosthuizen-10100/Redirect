import customtkinter as ctk
from PIL import Image
from constants import ViewConstants

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")

class ShopListFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        def checkbox1_event():
            print("checkbox1 toggled, current value:", self.check_var1.get())

        self.check_var1 = ctk.StringVar(value="off")

        self.chb_shop1 = ctk.CTkCheckBox(
            master=self,
            text="Shop 1",
            command=checkbox1_event,
            variable=self.check_var1,
            onvalue="on",
            offvalue="off",
            font=('JetBrains Mono',14),
        ).grid(
            row=0,
            column=0,
            padx=20,
            pady=20,
        )

        def checkbox2_event():
            print("checkbox2 toggled, current value:", self.check_var2.get())

        self.check_var2 = ctk.StringVar(value="off")

        self.chb_shop2 = ctk.CTkCheckBox(
            master=self,
            text="Shop 1",
            command=checkbox2_event,
            variable=self.check_var2,
            onvalue="on",
            offvalue="off",
            font=('JetBrains Mono',14),
        ).grid(
            row=1,
            column=0,
            padx=20,
            pady=20,
        )


class SourceFolderLocationFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

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
            width=20,
            height=20,
        ).grid(
            row=1,
            column=1,
            padx=(5,20),
            pady=(0,10),
        )
class DestinationFolderLocationFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

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
            width=20,
            height=20,
        ).grid(
            row=1,
            column=1,
            padx=(5,20),
            pady=(0,10),
        )

class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

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
            width=100,
            height=50,            
        ).grid(
            row=3,
            column=1,
            padx=60,
            pady=(0,60),
        )

app = App()
app.mainloop()