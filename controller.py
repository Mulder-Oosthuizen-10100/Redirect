from type import *
from log import RedirectLogger
from validator import RedirectValidator
from view import RedirectView
from model import RedirectModel
from constants import RedirectConstants
from configurator import RedirectConfiguration
from inspect import *
import os, sys, inspect

_caller: LogCaller = LogCaller.Controller

class RedirectController:
    def __init__(
        self,
        logger: RedirectLogger,
    ):
        self.logger = logger
        self.const = RedirectConstants()
        
        self.info(
            log_caller=_caller,
            log_message=self.const.LogMessageApplicationStarting
        )
        
        self.model = RedirectModel(
            controller=self
        )
        self.info(
            log_caller=_caller,
            log_message=f"{self.const.LogMessageClassInitialized}({self.get_line_number(5)}): {self.model.__class__.__name__}"
        )

        self.validate = RedirectValidator(controller=self)
        self.info(
            log_caller=_caller,
            log_message=f"{self.const.LogMessageClassInitialized}({self.get_line_number(3)}): {self.validate.__class__.__name__}"
        )
        
        self.view = RedirectView(controller=self)
        self.info(
            log_caller=_caller,
            log_message=f"{self.const.LogMessageClassInitialized}({self.get_line_number(3)}): {self.view.__class__.__name__}"
        )

        self.info(
            log_caller=_caller,
            log_message=f"{self.const.LogMessageApplicationGUIBuilt}"
        )

        self.view.root.after(500, self.add_shops)
        self.view.root.mainloop()

        self.info(
            log_caller=_caller,
            log_message=f"{self.const.LogMessageApplicationClosing}"
        )

# VIEW
    def open_message(
        self,
        text_message,
        close_application: bool,
    ):
        self.view.open_message(
            text_message=text_message,
            close_application=close_application,
        )

    def close_message(
        self,
        close_application: bool,
    ):
        self.view.close_message()
        if close_application:
            self.close_application()

    def add_shops(
        self
    ):
        self.info(
            log_caller=_caller,
            log_message=f"{self.const.LogMessageFunctionCalled}({self.get_line_number(5)}): {inspect.stack()[0][3]}"
        )
        if self.model.set_model_data():
            self.view.add_shops(
                lst_dict_websites=self.model.lst_dict_websites
            )
            self.debug(
                log_caller=_caller,
                log_message=f"{self.const.LogMessageApplicationDataRetrieved}"
            )

    def update_edt_redirect_folder_location(
        self,
        new_text,
    ):
        self.view.update_edt_redirect_folder_location(
            new_text=new_text
        )
    
    def close_application(
        self
    ):
        self.view.close_application()

# MODEL
    def set_source_file_name(
        self,
        file_name,
        show_error_message,
        log_error_message,
    ) -> bool:
        return self.model.set_source_file_name(
            file_name=file_name,
            show_error_message=show_error_message,
            log_error_message=log_error_message,
        )

    def set_redirect_folder_name(
        self,
        folder
    ):
        # self.info(
        #     log_caller=_caller,
        #     log_message=f"{self.const.LogMessageFunctionCalled}({self.get_line_number(6)}): {inspect.stack()[0][3]}"
        # )
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
        log_error_message,
    ):
        # self.info(
        #     log_caller=_caller,
        #     log_message=f"{self.const.LogMessageFunctionCalled}({self.get_line_number(7)}): {inspect.stack()[0][3]}"
        # )
        self.model.generate_csv_file(
            show_error_message=show_error_message,
            log_error_message=log_error_message,
        )
    
    def get_default_directory(
        self
    ) -> str:
        # self.info(
        #     log_caller=_caller,
        #     log_message=f"{self.const.LogMessageFunctionCalled}({self.get_line_number(5)}): {inspect.stack()[0][3]}"
        # )
        return self.model.get_default_directory()
    
    def must_update_edt_redirect_folder_location(
        self
    ) -> bool:
        # self.info(
        #     log_caller=_caller,
        #     log_message=f"{self.const.LogMessageFunctionCalled}({self.get_line_number(5)}): {inspect.stack()[0][3]}"
        # )
        return self.model.must_update_edt_redirect_folder_location()

    def get_root_directory_from_source_file_name(
        self,
        source_file_name,
    ):
        # self.info(
        #     log_caller=_caller,
        #     log_message=f"{self.const.LogMessageFunctionCalled}({self.get_line_number(6)}): {inspect.stack()[0][3]}"
        # )
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
        self.logger.log(
            log_level=LogLevel.Debug,
            log_caller=log_caller,
            log_message=log_message
        )

    def info(
        self,
        log_caller: LogCaller,
        log_message: str,
    ):
        self.logger.log(
            log_level=LogLevel.Info,
            log_caller=log_caller,
            log_message=log_message
        )

    def warn(
        self,
        log_caller: LogCaller,
        log_message: str,
    ):
        self.logger.log(
            log_level=LogLevel.Warn,
            log_caller=log_caller,
            log_message=log_message
        )

    def error(
        self,
        log_caller: LogCaller,
        log_message: str,
    ):
        self.logger.log(
            log_level=LogLevel.Error,
            log_caller=log_caller,
            log_message=log_message
        )

    def get_line_number(
        self,
        minus_lines: int,
        direct_line: bool = False,
    ):
        if not direct_line:
            return self.logger.get_line_number(
                line_number=currentframe().f_back.f_lineno,
                minus_lines=minus_lines,
            )
        else:
            return self.logger.get_direct_line_number(
                direct_line_number=minus_lines,
            )

# OTHER

    def resource_path(
        self, 
        relative_path
    ):
        self.info(
            log_caller=_caller,
            log_message=f"{self.const.LogMessageFunctionCalled}({self.get_line_number(6)}): {inspect.stack()[0][3]}"
        )
        self.debug(
            log_caller=_caller,
            log_message=f"{self.const.LogMessageFunctionParameters}({self.get_line_number(8)}): [Relative Path | {relative_path}]"
        )
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

if __name__ == "__main__":
    configuration = RedirectConfiguration()

    logger = RedirectLogger(
        log_config=RedirectLogger.get_log_config()
    )

    logger.log_level = configuration.LogLevel

    print(f"Log Level: {configuration.LogLevel}")
    
    controller = RedirectController(
        logger=logger
    )