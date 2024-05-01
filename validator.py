import os, inspect
from type import LogCaller

_caller: LogCaller = LogCaller.Validator

class RedirectValidator():
    def __init__(
        self,
        controller,
    ):
        self.controller = controller

    def validate_worksheets(
        self,
        lst_dict_websites,
        lst_dict_keywords,
        lst_dict_remove_parts,
        show_error_message,
    ) -> bool:
        self.controller.info(log_caller=_caller,log_message=f"{self.controller.const.LogMessageFunctionCalled}: {inspect.stack()[0][3]}")
        if lst_dict_websites:
            if lst_dict_keywords:
                if lst_dict_remove_parts:
                    return True
                else:
                    if show_error_message:
                        self.controller.open_message(
                            text_message="Google Sheet does not contain any remove parts!",
                            close_application=True,
                        )
                    self.controller.error(
                        log_caller=_caller,
                        log_message=f"Google Sheet Document '{self.controller.const.GoogleSheetDocumentName}' does not contain any REMOVE_PART entries in the REMOVE_PARTS tab.",
                    )
                    return False
            else:
                if show_error_message:
                    self.controller.open_message(
                        text_message="Google Sheet does not contain any keywords!",
                        close_application=True,
                    )
                self.controller.error(
                    log_caller=_caller,
                    log_message=f"Google Sheet Document '{self.controller.const.GoogleSheetDocumentName}' does not contain any KEYWORD entries in the KEYWORDS tab.",
                )
                return False
        else:
            if show_error_message:
                self.controller.open_message(
                    text_message="Google Sheet does not contain any websites!",
                    close_application=True,
                )
            self.controller.error(
                log_caller=_caller,
                log_message=f"Google Sheet Document '{self.controller.const.GoogleSheetDocumentName}' does not contain any WEBSITE entries in the WEBSITES tab.",
            )
            return False

    def validate_shop_name(
        self,
        shop_name,
        show_error_message,
    ) -> bool:
        self.controller.info(log_caller=_caller,log_message=f"{self.controller.const.LogMessageFunctionCalled}: {inspect.stack()[0][3]}")
        if not shop_name:
            if show_error_message:
                self.controller.open_message(
                    text_message="Please select a shop name!",
                    close_application=False,
                )
            self.controller.error(
                log_caller=_caller,
                log_message=f"Invalid shop name '{shop_name}'.",
            )
            return False
        else:
            return True

    def validate_source_file_name(
        self,
        source_file_name,
        show_error_message,
        log_error_message,
    ) -> bool:
        self.controller.info(log_caller=_caller,log_message=f"{self.controller.const.LogMessageFunctionCalled}: {inspect.stack()[0][3]}")
        try:
            if source_file_name:
                if os.path.isfile(
                    path=source_file_name
                ):
                    if os.stat(
                        path=source_file_name
                    ).st_size > 0:
                        return True
                    else:
                        if show_error_message:
                            self.controller.open_message(
                                text_message="The selected source file is empty!",
                                close_application=False,
                            )
                        if log_error_message:
                            self.controller.error(
                                log_caller=_caller,
                                log_message=f"Source file empty -> '{source_file_name}'.",
                            )
                        return False
                else:
                    if show_error_message:
                        self.controller.open_message(
                            text_message="The selected source file is not a file!",
                            close_application=False,
                        )
                    if log_error_message:
                        self.controller.error(
                            log_caller=_caller,
                            log_message=f"Source file is not a file -> '{source_file_name}'.",
                        )
                    return False
            else:
                if show_error_message:
                    self.controller.open_message(
                        text_message="Please select a source file!",
                        close_application=False,
                    )
                if log_error_message:
                    self.controller.error(
                        log_caller=_caller,
                        log_message=f"Source file is None -> '{source_file_name}'.",
                    )
                return False

        except OSError:
            if show_error_message:
                self.controller.open_message(
                    text_message="Source File: DOES NOT EXIST",
                    close_application=False,
                )
            if log_error_message:
                self.controller.error(
                    log_caller=_caller,
                    log_message=f"Source File: DOES NOT EXIST -> '{source_file_name}'.",
                )
            return False
        except Exception as e:
            if show_error_message:
                self.controller.open_message(
                    text_message="An unknown exception occurred!",
                    close_application=False,
                )
            if log_error_message:
                self.controller.error(
                    log_caller=_caller,
                    log_message=f"An Error occurred during the validation of the source file! Error Message: {e}.",
                )
            return False