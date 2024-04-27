from type import LogLevel, LogCaller
from log import RedirectLogger
from validator import RedirectValidator
from view import RedirectView
from model import RedirectModel
import os, sys

class RedirectController:
    def __init__(self):
        self.model = RedirectModel(controller=self)
        self.log = RedirectLogger(controller=self,log_config=self.model.get_log_config())
        self.validate = RedirectValidator(controller=self)
        self.view = RedirectView(controller=self)
        self.view.root.after(1000, self.add_shops)
        self.view.root.mainloop()

# VIEW
    def add_shops(self):
        self.model.set_model_data()
        self.view.root.frm_shop_list.add_shops(lst_dict_websites=self.model.lst_dict_websites)

    def open_message(
        self,
        text_message,
    ):
        self.view.open_message(
            text_message=text_message
        )

    def close_message(self):
        self.view.close_message()

    def update_edt_redirect_folder_location(
        self,
        new_text
    ):
        self.view.root.frm_redirect_location.update_edt_redirect_folder_location(new_text=new_text)

# MODEL
    def set_source_file_name(
        self,
        file_name,
        show_error_message,
    ) -> bool:
        return self.model.set_source_file_name(
            file_name=file_name,
            show_error_message=show_error_message,
        )

    def set_redirect_folder_name(self, folder):
        self.model.set_redirect_folder_name(folder_name=folder)

    def set_shop_name(
        self,
        shop_name,
        show_error_message,
    ):
        self.model.set_shop_name(
            shop_name=shop_name,
            show_error_message=show_error_message
        )

    def generate_csv_file(
        self,
        show_error_message,
    ):
        self.model.generate_csv_file(
            show_error_message=show_error_message
        )
    
    def get_default_directory(self) -> str:
        return self.model.get_default_directory()
    
    def must_update_edt_redirect_folder_location(self) -> bool:
        return self.model.must_update_edt_redirect_folder_location()

    def get_root_directory_from_source_file_name(
        self,
        source_file_name,
    ):
        return self.model.get_root_directory_from_source_file_name(
            source_file_name=source_file_name
        )

# VALIDATE
    def validate_shop_name(
        self,
        shop_name,
        show_error_message,
    ) -> bool:
        return self.validate.validate_shop_name(
            shop_name=shop_name,
            show_error_message=show_error_message,
        )
    
    def validate_source_file_name(
        self,
        source_file_name,
        show_error_message,
    ) -> bool:
        return self.validate.validate_source_file_name(
            source_file_name=source_file_name,
            show_error_message=show_error_message,
        )

# LOG
    def debug(
        self,
        log_caller: LogCaller,
        log_message: str,
    ):
        self.log.log(
            log_level=LogLevel.Debug,
            log_caller=log_caller,
            log_message=log_message
        )

    def info(
        self,
        log_caller: LogCaller,
        log_message: str,
    ):
        self.log.log(
            log_level=LogLevel.Info,
            log_caller=log_caller,
            log_message=log_message
        )

    def warn(
        self,
        log_caller: LogCaller,
        log_message: str,
    ):
        self.log.log(
            log_level=LogLevel.Warn,
            log_caller=log_caller,
            log_message=log_message
        )

    def error(
        self,
        log_caller: LogCaller,
        log_message: str,
    ):
        self.log.log(
            log_level=LogLevel.Error,
            log_caller=log_caller,
            log_message=log_message
        )

# OTHER

    def resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

if __name__ == "__main__":
    controller = RedirectController()