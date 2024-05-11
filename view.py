import customtkinter as ctk
import inspect
from tkinter import filedialog
from PIL import Image
from type import *
from constants import RedirectConstants

ctk.set_appearance_mode(RedirectConstants.AppearanceModeSystem)
ctk.set_default_color_theme(RedirectConstants.DefaultColorTheme)

_caller: LogCaller = LogCaller.View

class ShopListFrame(ctk.CTkScrollableFrame):
    def __init__(
            self,
            master,
            controller,
            loading_text,
            **kwargs
        ):
        super().__init__(master, **kwargs)

        self.controller = controller
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageClassInitializing}({self.controller.get_line_number(12)}): {self.__class__.__name__}"
        )

        self.grid_columnconfigure(0, weight=1)
        self.lst_rdbtn_shops = []
        self.rdbtn_var = ctk.StringVar(value="off")
        self.lbl_loading_var = ctk.StringVar(value=loading_text)
        self.row_count = 0

        self.lbl_loading = ctk.CTkLabel(
            master=self,
            text=self.lbl_loading_var.get(),
            font=(
                RedirectConstants.TextFontFamily,
                RedirectConstants.MediumTextSize,
            ),
        )

        self.lbl_loading.grid(
            row=0,
            column=0,
        )

    def add_shops(
        self,
        lst_dict_websites
    ):
        self.controller.info(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionCalled}({self.controller.get_line_number(6)}): {inspect.stack()[0][3].capitalize}"
        )
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionParameters}({self.controller.get_line_number(8)}): [List of Dictionaries of Websites | {lst_dict_websites}]"
        )
        self.lbl_loading.destroy()
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionStatement}({self.controller.get_line_number(3)}): Loading Label Destroyed."
        )

        for shop in lst_dict_websites:
            self.grid_rowconfigure(self.row_count, weight=1)
            loop_shop_name = shop.get(RedirectConstants.KeyWebsite)
            self.rdbtn_var.set(loop_shop_name)
            ctk.CTkRadioButton(
                master=self,
                text=loop_shop_name,
                font=(
                    RedirectConstants.TextFontFamily,
                    RedirectConstants.SmallTextSize,
                ),
                variable=self.rdbtn_var,
                value=loop_shop_name,
                command=self.rdbtn_selected,
            ).grid(
                row=self.row_count,
                column=0,
                pady=(20,0),
                padx=20,
                sticky='ew',
            )

            self.controller.debug(
                log_caller=_caller,
                log_message=f"{RedirectConstants.LogMessageForLoop}[{self.controller.get_line_number(self.row_count,True)}]: Item Added -> {shop}"
            )

            self.row_count += 1
        
        self.controller.set_shop_name(
            shop_name=self.rdbtn_var.get(),
            show_error_message=True
        )
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionStatement}({self.controller.get_line_number(6)}): Auto selected shop -> {loop_shop_name}."
        )

    def rdbtn_selected(
        self
    ):
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageUserInteractionStart}: SHOP_SELECTION"
        )
        self.controller.info(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionCalled}({self.controller.get_line_number(5)}): {inspect.stack()[0][3].capitalize}"
        )
        self.controller.set_shop_name(
            shop_name=self.rdbtn_var.get(),
            show_error_message=True
        )
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageUserInteractionEnd}: SHOP_SELECTION"
        )

class SourceFolderLocationFrame(ctk.CTkFrame):
    def __init__(
        self,
        master,
        controller,
        **kwargs
    ):
        super().__init__(master, **kwargs)

        self.controller = controller
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageClassInitializing}({self.controller.get_line_number(11)}): {self.__class__.__name__}"
        )

        self.edt_text_var = ctk.StringVar(value=self.controller.get_default_directory())
        self.controller.set_source_file_name(
            file_name=self.edt_text_var.get(),
            show_error_message=False,
        )
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0,1,), weight=1)

        self.lbl_source_file_location = ctk.CTkLabel(
            master=self,
            text=RedirectConstants.LabelSourceFileLocationText,
            font=(
                RedirectConstants.TextFontFamily,
                RedirectConstants.MediumTextSize,
            ),
        ).grid(
            row=0,
            column=0,
            columnspan=2,
            padx=20,
            sticky="w",
        )

        self.edt_source_file_location = ctk.CTkEntry(
            master=self,
            font=(
                RedirectConstants.TextFontFamily,
                RedirectConstants.SmallTextSize,
            ),
            textvariable=self.edt_text_var,
            justify="right",
            state="disabled",
        ).grid(
            row=1,
            column=0,
            sticky="ew",
            padx=(20,5),
            pady=(0,10),
        )

        self.img_source_folder_location = ctk.CTkImage(
            dark_image=Image.open(
                self.controller.resource_path(
                    relative_path=RedirectConstants.ImageOpenDialog,
                ),
            ),
            size=
            (
                20,
                20
            ),
        )

        self.btn_source_file_location = ctk.CTkButton(
            master=self,
            image=self.img_source_folder_location,
            text="",
            command=lambda: self.open_source_file(
                show_error_message=True,
            ),
            width=20,
            height=20,
        ).grid(
            row=1,
            column=1,
            padx=(5,20),
            pady=(0,10),
        )

    def open_source_file(
        self,
        show_error_message,
    ):
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageUserInteractionStart}: SOURCE_FILE_SELECTION"
        )
        self.controller.info(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionCalled}({self.controller.get_line_number(7)}): {inspect.stack()[0][3].capitalize}"
        )
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionParameters}({self.controller.get_line_number(13)}): [Show Error Message | {show_error_message}]"
        )
        file_name = filedialog.askopenfilename(
            title=RedirectConstants.TitleSourceFileDialog,
            initialdir=self.controller.get_default_directory(),
            defaultextension=RedirectConstants.DefaultSourceFileExtension,
            filetypes=[
                (
                    RedirectConstants.ExtensionTypeSourceFile,
                    RedirectConstants.DefaultSourceFileExtension,
                ),
            ],
        )
        if file_name:
            self.controller.debug(
                log_caller=_caller,
                log_message=f"{RedirectConstants.LogMessageFunctionStatement}({self.controller.get_line_number(3)}): User has selected a source file."
            )
            if self.controller.set_source_file_name(
                file_name=file_name,
                show_error_message=show_error_message,
            ):
                self.update_edt_source_folder_location(
                    new_text=file_name
                )
        else:
            self.controller.debug(
                log_caller=_caller,
                log_message=f"{RedirectConstants.LogMessageFunctionStatement}({self.controller.get_line_number(3)}): User has aborted the source file selection."
            )
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageUserInteractionEnd}: SOURCE_FILE_SELECTION"
        )

    def update_edt_source_folder_location(
        self,
        new_text
    ):
        self.controller.info(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionCalled}({self.controller.get_line_number(6)}): {inspect.stack()[0][3].capitalize}"
        )
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionParameters}({self.controller.get_line_number(8)}): [New Text | {new_text}]"
        )
        self.edt_text_var.set(new_text)
        if self.controller.must_update_edt_redirect_folder_location():
            self.controller.update_edt_redirect_folder_location(
                new_text=self.controller.get_root_directory_from_source_file_name(
                    source_file_name=new_text
                )
            )

class RedirectFolderLocationFrame(ctk.CTkFrame):
    def __init__(
        self,
        master,
        controller,
        **kwargs
    ):
        super().__init__(master, **kwargs)

        self.controller = controller
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageClassInitializing}({self.controller.get_line_number(11)}): {self.__class__.__name__}"
        )

        self.edt_text_var = ctk.StringVar(value=self.controller.get_default_directory())
        self.controller.set_redirect_folder_name(self.edt_text_var.get())
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0,1,), weight=1)

        self.lbl_redirect_folder_location = ctk.CTkLabel(
            master=self,
            text=RedirectConstants.LabelRedirectFolderLocationText,
            font=(
                RedirectConstants.TextFontFamily,
                RedirectConstants.MediumTextSize,
            ),
        ).grid(
            row=0,
            column=0,
            columnspan=2,
            padx=20,
            sticky="w",
        )

        self.edt_redirect_folder_location = ctk.CTkEntry(
            master=self,
            font=(
                RedirectConstants.TextFontFamily,
                RedirectConstants.SmallTextSize,
            ),
            textvariable=self.edt_text_var,
            justify="right",
            state="disabled",
        ).grid(
            row=1,
            column=0,
            sticky="ew",
            padx=(20,5),
            pady=(0,10),
        )

        self.img_redirect_folder_location = ctk.CTkImage(
            dark_image=Image.open(
                self.controller.resource_path(
                    RedirectConstants.ImageOpenDialog,
                ),
            ),
            size=(
                20,
                20,
            ),
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
    
    def open_redirect_folder(
        self
    ):
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageUserInteractionStart}: REDIRECT_FOLDER_SELECTION"
        )
        self.controller.info(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionCalled}({self.controller.get_line_number(9)}): {inspect.stack()[0][3].capitalize}"
        )
        folder = filedialog.askdirectory(
            title=RedirectConstants.TitleDestinationFolderDialog,
            initialdir=self.edt_text_var.get(),
        )
        if folder:
            self.controller.debug(
                log_caller=_caller,
                log_message=f"{RedirectConstants.LogMessageFunctionStatement}({self.controller.get_line_number(3)}): User has selected a folder."
            )
            self.controller.set_redirect_folder_name(folder)
            self.update_edt_redirect_folder_location(folder)
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageUserInteractionEnd}: REDIRECT_FOLDER_SELECTION"
        )
    
    def update_edt_redirect_folder_location(
        self,
        new_text
    ):
        self.controller.info(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionCalled}({self.controller.get_line_number(6)}): {inspect.stack()[0][3].capitalize}"
        )
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionParameters}({self.controller.get_line_number(8)}): [New Text | {new_text}]"
        )
        self.edt_text_var.set(new_text)
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionStatement}({self.controller.get_line_number(3)}): Entry Redirect Folder Location Updated."
        )

class MainWindow(ctk.CTk):
    def __init__(
            self,
            controller,
            *args,
            **kwargs
        ):
        super().__init__(*args, **kwargs)
        
        self.controller = controller
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageClassInitializing}({self.controller.get_line_number(11)}): {self.__class__.__name__}"
        )

        self.title(RedirectConstants.ApplicationTitle)
        self.geometry(RedirectConstants.ApplicationGeometry)
        self.iconbitmap(
            bitmap=self.controller.resource_path(
                relative_path=RedirectConstants.PathRedirectLogo
            )
        )
        self.resizable(
            height=False,
            width=False,
        )
        
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure((1,2,3), weight=2)

        self.lbl_heading = ctk.CTkLabel(
            master=self,
            text=RedirectConstants.ApplicationHeadingText,
            font=(
                RedirectConstants.TextFontFamily,
                RedirectConstants.LargeTextSize,
            )
        ).grid(
            row=0,
            column=0,
            columnspan=2,
            pady=20,
            sticky="nesw",
        )

        self.frm_shop_list = ShopListFrame(
            master=self,
            controller=controller,
            loading_text=RedirectConstants.ApplicationLoadingText,
            corner_radius=16,
        )
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageClassInitialized}({self.controller.get_line_number(8)}): {self.frm_shop_list.__class__.__name__}"
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
        )
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageClassInitialized}({self.controller.get_line_number(7)}): {self.frm_source_location.__class__.__name__}"
        )
        
        self.frm_source_location.grid(
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
        )
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageClassInitialized}({self.controller.get_line_number(7)}): {self.frm_redirect_location.__class__.__name__}"
        )

        self.frm_redirect_location.grid(
            row=2,
            column=1,
            padx=60,
            pady=(0,60),
            sticky="nsew",
        )

        self.btn_generate_csv = ctk.CTkButton(
            master=self,
            corner_radius=20,
            text=RedirectConstants.TextButtonGenerate,
            font=(
                RedirectConstants.TextFontFamily,
                RedirectConstants.MediumTextSize,
            ),
            command=lambda:self.controller.generate_csv_file(
                show_error_message=True,
            ),
            width=100,
            height=50,
        ).grid(
            row=3,
            column=1,
            padx=60,
            pady=(0,60),
        )

class MessageWindow(ctk.CTkToplevel):
    def __init__(
            self,
            controller,
            text_message,
            close_application: bool,
            *args,
            **kwargs
        ):
        super().__init__(*args, **kwargs)

        self.title(RedirectConstants.MessageWindowTitle)
        self.controller = controller
        self.text_message = text_message
        self.geometry(str(len(self.text_message) * 10)+'x200')
        self.iconbitmap(self.controller.resource_path(RedirectConstants.ImageApplicationIcon))
        self.resizable(
            height=False,
            width=False,
        )
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.lbl_heading = ctk.CTkLabel(
            master=self,
            text=self.text_message,
            font=(
                RedirectConstants.TextFontFamily,
                RedirectConstants.SmallTextSize,
            ),
        ).grid(
            row=0,
            column=0,
            sticky="nesw",
        )

        self.btn_ok = ctk.CTkButton(
            master=self,
            text=RedirectConstants.TextMessageWindowButton,
            command=lambda: self.controller.close_message(
                close_application=close_application,
            ),
            font=(
                RedirectConstants.TextFontFamily,
                RedirectConstants.SmallTextSize,
            ),
            corner_radius=16,
        ).grid(
            row=1,
            column=0,
            pady=20,
        )        

class RedirectView:
    def __init__(
        self,
        controller,
    ):
        self.controller = controller
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageClassInitializing}({self.controller.get_line_number(6)}): {self.__class__.__name__}"
        )

        self.sub_root = None
        self.root = MainWindow(
            controller=self.controller,
        )
        
        self.center(
            win=self.root
        )

        self.controller.debug(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageClassInitialized}({self.controller.get_line_number(5)}): {self.root.__class__.__name__}"
        )
    
    def center(
        self,
        win,
    ):
        '''
        centers a tkinter window
        :param win: the main window or Toplevel window to center
        '''
        win.update_idletasks()
        width = win.winfo_width()
        frm_width = win.winfo_rootx() - win.winfo_x()
        win_width = width + 2 * frm_width
        height = win.winfo_height()
        titlebar_height = win.winfo_rooty() - win.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = win.winfo_screenwidth() // 2 - win_width // 2
        y = win.winfo_screenheight() // 2 - win_height // 2
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        win.deiconify()

    def open_message(
        self,
        text_message,
        close_application: bool,
    ):
        self.controller.info(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionCalled}({self.controller.get_line_number(7)}): {inspect.stack()[0][3].capitalize}"
        )
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionParameters}({self.controller.get_line_number(9)}): [Text Message | {text_message}]"
        )
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionParameters}({self.controller.get_line_number(12)}): [Close Application | {close_application}]"
        )
        if self.sub_root is None or not self.sub_root.winfo_exists():
            self.sub_root = MessageWindow(
                controller=self.controller,
                text_message=text_message,
                close_application=close_application,
            )
            self.center(self.sub_root)
            self.sub_root.grab_set()
        else:
            previous_message=self.sub_root.text_message
            self.close_message()
            self.open_message(
                text_message=previous_message + '\n' + text_message,
                close_application=close_application,
            )

    def close_message(
        self
    ):
        self.controller.info(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionCalled}({self.controller.get_line_number(5)}): {inspect.stack()[0][3].capitalize}"
        )
        self.sub_root.destroy()
        self.sub_root = None
    
    def add_shops(
        self,
        lst_dict_websites,
    ):
        self.root.frm_shop_list.add_shops(
            lst_dict_websites=lst_dict_websites,
        )

    def update_edt_redirect_folder_location(
        self,
        new_text,
    ):
        self.root.frm_redirect_location.update_edt_redirect_folder_location(
            new_text=new_text
        )
    
    def close_application(
        self,
    ):
        self.controller.info(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionCalled}({self.controller.get_line_number(5)}): {inspect.stack()[0][3].capitalize}"
        )        
        self.root.destroy()