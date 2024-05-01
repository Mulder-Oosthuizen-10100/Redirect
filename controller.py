from type import *
from log import RedirectLogger
from validator import RedirectValidator
from view import RedirectView
from model import RedirectModel
from constants import RedirectConstants
import os, sys, inspect

_caller: LogCaller = LogCaller.Controller

class RedirectController:
    def __init__(
        self,
        log_configuration: LogConfig
    ):
        self.const = RedirectConstants()
        application_started_log_message=self.const.LogMessageApplicationStart
        
        self.log = RedirectLogger(controller=self)


        self.model = RedirectModel(controller=self)
        temp_info_log_message=f"{self.const.LogMessageClassInitialized}: {self.model.__class__.__name__}"

        self.log = RedirectLogger(controller=self,log_config=self.model.get_log_config())
        self.info(log_caller=_caller,log_message=application_started_log_message)
        self.info(log_caller=_caller,log_message=temp_info_log_message)
        self.info(log_caller=_caller,log_message=f"{self.const.LogMessageClassInitialized}: {self.log.__class__.__name__}")

        self.validate = RedirectValidator(controller=self)
        self.info(log_caller=_caller,log_message=f"{self.const.LogMessageClassInitialized}: {self.validate.__class__.__name__}")
        
        self.view = RedirectView(controller=self)
        self.info(log_caller=_caller,log_message=f"{self.const.LogMessageClassInitialized}: {self.view.__class__.__name__}")

        self.view.root.after(500, self.add_shops)
        self.view.root.mainloop()

# VIEW
    def add_shops(self):
        self.info(log_caller=_caller,log_message=f"{self.const.LogMessageFunctionCalled}: {inspect.stack()[0][3]}")
        if self.model.set_model_data():
            self.view.root.frm_shop_list.add_shops(lst_dict_websites=self.model.lst_dict_websites)

    def open_message(
        self,
        text_message,
        close_application: bool,
    ):
        self.info(log_caller=_caller,log_message=f"{self.const.LogMessageFunctionCalled}: {inspect.stack()[0][3]}")
        self.view.open_message(
            text_message=text_message,
            close_application=close_application,
        )

    def close_message(
        self,
        close_application: bool,
    ):
        self.info(log_caller=_caller,log_message=f"{self.const.LogMessageFunctionCalled}: {inspect.stack()[0][3]}")
        self.view.close_message()
        if close_application:
            self.close_application()

    def update_edt_redirect_folder_location(
        self,
        new_text
    ):
        self.info(log_caller=_caller,log_message=f"{self.const.LogMessageFunctionCalled}: {inspect.stack()[0][3]}")
        self.view.root.frm_redirect_location.update_edt_redirect_folder_location(new_text=new_text)
    
    def close_application(self):
        self.info(log_caller=_caller,log_message=f"{self.const.LogMessageFunctionCalled}: {inspect.stack()[0][3]}")
        self.view.root.destroy()

# MODEL
    def set_source_file_name(
        self,
        file_name,
        show_error_message,
        log_error_message,
    ) -> bool:
        self.info(log_caller=_caller,log_message=f"{self.const.LogMessageFunctionCalled}: {inspect.stack()[0][3]}")
        return self.model.set_source_file_name(
            file_name=file_name,
            show_error_message=show_error_message,
            log_error_message=log_error_message,
        )

    def set_redirect_folder_name(self, folder):
        self.info(log_caller=_caller,log_message=f"{self.const.LogMessageFunctionCalled}: {inspect.stack()[0][3]}")
        self.model.set_redirect_folder_name(folder_name=folder)

    def set_shop_name(
        self,
        shop_name,
        show_error_message,
    ):
        self.info(log_caller=_caller,log_message=f"{self.const.LogMessageFunctionCalled}: {inspect.stack()[0][3]}")
        self.model.set_shop_name(
            shop_name=shop_name,
            show_error_message=show_error_message
        )

    def generate_csv_file(
        self,
        show_error_message,
        log_error_message,
    ):
        self.info(log_caller=_caller,log_message=f"{self.const.LogMessageFunctionCalled}: {inspect.stack()[0][3]}")
        self.model.generate_csv_file(
            show_error_message=show_error_message,
            log_error_message=log_error_message,
        )
    
    def get_default_directory(self) -> str:
        self.info(log_caller=_caller,log_message=f"{self.const.LogMessageFunctionCalled}: {inspect.stack()[0][3]}")
        return self.model.get_default_directory()
    
    def must_update_edt_redirect_folder_location(self) -> bool:
        self.info(log_caller=_caller,log_message=f"{self.const.LogMessageFunctionCalled}: {inspect.stack()[0][3]}")
        return self.model.must_update_edt_redirect_folder_location()

    def get_root_directory_from_source_file_name(
        self,
        source_file_name,
    ):
        self.info(log_caller=_caller,log_message=f"{self.const.LogMessageFunctionCalled}: {inspect.stack()[0][3]}")
        return self.model.get_root_directory_from_source_file_name(
            source_file_name=source_file_name
        )

# VALIDATE
    def validate_worksheets(
        self,
        lst_dict_websites,
        lst_dict_keywords,
        lst_dict_remove_parts,
        show_error_message,
    ) -> bool:
        self.info(log_caller=_caller,log_message=f"{self.const.LogMessageFunctionCalled}: {inspect.stack()[0][3]}")
        return self.validate.validate_worksheets(
            lst_dict_websites=lst_dict_websites,
            lst_dict_keywords=lst_dict_keywords,
            lst_dict_remove_parts=lst_dict_remove_parts,
            show_error_message=show_error_message,
        )

    def validate_shop_name(
        self,
        shop_name,
        show_error_message,
    ) -> bool:
        self.info(log_caller=_caller,log_message=f"{self.const.LogMessageFunctionCalled}: {inspect.stack()[0][3]}")
        return self.validate.validate_shop_name(
            shop_name=shop_name,
            show_error_message=show_error_message,
        )
    
    def validate_source_file_name(
        self,
        source_file_name,
        show_error_message,
        log_error_message,
    ) -> bool:
        self.info(log_caller=_caller,log_message=f"{self.const.LogMessageFunctionCalled}: {inspect.stack()[0][3]}")
        return self.validate.validate_source_file_name(
            source_file_name=source_file_name,
            show_error_message=show_error_message,
            log_error_message=log_error_message,
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
        self.info(log_caller=_caller,log_message=f"{self.const.LogMessageFunctionCalled}: {inspect.stack()[0][3]}")        
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

if __name__ == "__main__":

    # have to use the config class
    # have to create the logger using the config class 

    # con = RedirectConfiguration()
    # print(con.LogLevel)

    controller = RedirectController(
        log_configuration=RedirectLogger.get_log_config()
    )