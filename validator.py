import os, inspect
from type import LogCaller
from constants import RedirectConstants

_caller: LogCaller = LogCaller.Validator

class RedirectValidator():
    def __init__(
        self,
        controller,
    ):
        self.controller = controller
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageClassInitializing}({self.controller.get_line_number(7)}): {self.__class__.__name__}"
        )

    def validate_worksheets(
        self,
        lst_dict_websites,
        lst_dict_keywords,
        lst_dict_remove_parts,
        show_error_message,
    ) -> bool:
        self.controller.info(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionCalled}({self.controller.get_line_number(9)}): {inspect.stack()[0][3]}"
        )
        if lst_dict_websites:
            if lst_dict_keywords:
                if lst_dict_remove_parts:
                    self.controller.debug(
                        log_caller=_caller,
                        log_message=f"{RedirectConstants.LogMessageFunctionStatement}({self.controller.get_line_number(3)}): ALL Worksheets are valid."
                    )                    
                    self.controller.debug(
                        log_caller=_caller,
                        log_message=f"{RedirectConstants.LogMessageFunctionReturned}({self.controller.get_line_number(-2)}): {inspect.stack()[0][3]} -> [TRUE]"
                    )
                    return True
                else:
                    if show_error_message:
                        self.controller.open_message(
                            text_message=RedirectConstants.ValidateErrorMessageNoRemoveParts,
                            close_application=True,
                        )
                    self.controller.error(
                        log_caller=_caller,
                        log_message=f"Google Sheet Document '{RedirectConstants.GoogleSheetDocumentName}' does not contain any REMOVE_PART entries in the REMOVE_PARTS tab.",
                    )
                    self.controller.debug(
                        log_caller=_caller,
                        log_message=f"{RedirectConstants.LogMessageFunctionReturned}({self.controller.get_line_number(-2)}): {inspect.stack()[0][3]} -> [FALSE]"
                    )
                    return False
            else:
                if show_error_message:
                    self.controller.open_message(
                        text_message=RedirectConstants.ValidateErrorMessageNoKeyWords,
                        close_application=True,
                    )
                self.controller.error(
                    log_caller=_caller,
                    log_message=f"Google Sheet Document '{RedirectConstants.GoogleSheetDocumentName}' does not contain any KEYWORD entries in the KEYWORDS tab.",
                )
                self.controller.debug(
                    log_caller=_caller,
                    log_message=f"{RedirectConstants.LogMessageFunctionReturned}({self.controller.get_line_number(-2)}): {inspect.stack()[0][3]} -> [FALSE]"
                )
                return False
        else:
            if show_error_message:
                self.controller.open_message(
                    text_message=RedirectConstants.ValidateErrorMessageNoWebsites,
                    close_application=True,
                )
            self.controller.error(
                log_caller=_caller,
                log_message=f"Google Sheet Document '{RedirectConstants.GoogleSheetDocumentName}' does not contain any WEBSITE entries in the WEBSITES tab.",
            )
            self.controller.debug(
                log_caller=_caller,
                log_message=f"{RedirectConstants.LogMessageFunctionReturned}({self.controller.get_line_number(-2)}): {inspect.stack()[0][3]} -> [FALSE]"
            )
            return False

    def validate_shop_name(
        self,
        shop_name,
        show_error_message,
    ) -> bool:
        self.controller.info(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionCalled}({self.controller.get_line_number(7)}): {inspect.stack()[0][3]}"
        )
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionParameters}({self.controller.get_line_number(9)}): [Shop Name | {shop_name}]"
        )
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionParameters}({self.controller.get_line_number(12)}): [Show Error Message | {show_error_message}]"
        )
        if not shop_name:
            if show_error_message:
                self.controller.open_message(
                    text_message=RedirectConstants.ValidateErrorMessageNoShop,
                    close_application=False,
                )
            self.controller.error(
                log_caller=_caller,
                log_message=f"Invalid shop name '{shop_name}'.",
            )
            self.controller.debug(
                log_caller=_caller,
                log_message=f"{RedirectConstants.LogMessageFunctionReturned}({self.controller.get_line_number(-2)}): {inspect.stack()[0][3]} -> [FALSE]"
            )
            return False
        else:
            self.controller.debug(
                log_caller=_caller,
                log_message=f"{RedirectConstants.LogMessageFunctionReturned}({self.controller.get_line_number(-2)}): {inspect.stack()[0][3]} -> [TRUE]"
            )
            return True

    def validate_source_file_name(
        self,
        source_file_name,
        show_error_message,
    ) -> bool:
        '''
        This function will validate if the file is a file and not a directory. It will also check that the file is a valid file 
        in the sense that it exists and that it is not empty. If there are any exceptions this function will also catch them.
        '''
        self.controller.info(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionCalled}({self.controller.get_line_number(12)}): {inspect.stack()[0][3]}"
        )
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionParameters}({self.controller.get_line_number(14)}): [Source File Name | {source_file_name}]"
        )
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionParameters}({self.controller.get_line_number(17)}): [Show Error Message | {show_error_message}]"
        )
        try:
            if source_file_name:
                if os.path.isfile(
                    path=source_file_name
                ):
                    if os.stat(
                        path=source_file_name
                    ).st_size > 0:
                        self.controller.debug(
                            log_caller=_caller,
                            log_message=f"{RedirectConstants.LogMessageFunctionReturned}({self.controller.get_line_number(-2)}): {inspect.stack()[0][3]} -> [TRUE]"
                        )
                        return True
                    else:
                        if show_error_message:
                            self.controller.open_message(
                                text_message=RedirectConstants.ValidateErrorMessageSourceFileEmpty,
                                close_application=False,
                            )
                        self.controller.error(
                            log_caller=_caller,
                            log_message=f"Source file empty -> '{source_file_name}'.",
                        )
                        self.controller.debug(
                            log_caller=_caller,
                            log_message=f"{RedirectConstants.LogMessageFunctionReturned}({self.controller.get_line_number(-2)}): {inspect.stack()[0][3]} -> [FALSE]"
                        )
                        return False
                else:
                    if show_error_message:
                        self.controller.open_message(
                            text_message=RedirectConstants.ValidateErrorMessageSourceFileNotAFile,
                            close_application=False,
                        )
                    self.controller.error(
                        log_caller=_caller,
                        log_message=f"Source file is not a file -> '{source_file_name}'.",
                    )
                    self.controller.debug(
                        log_caller=_caller,
                        log_message=f"{RedirectConstants.LogMessageFunctionReturned}({self.controller.get_line_number(-2)}): {inspect.stack()[0][3]} -> [FALSE]"
                    )
                    return False
            else:
                if show_error_message:
                    self.controller.open_message(
                        text_message=RedirectConstants.ValidateErrorMessageSourceFileNotSelected,
                        close_application=False,
                    )
                self.controller.error(
                    log_caller=_caller,
                    log_message=f"Source file is None -> '{source_file_name}'.",
                )
                self.controller.debug(
                    log_caller=_caller,
                    log_message=f"{RedirectConstants.LogMessageFunctionReturned}({self.controller.get_line_number(-2)}): {inspect.stack()[0][3]} -> [FALSE]"
                )
                return False
        except OSError as e:
            if show_error_message:
                self.controller.open_message(
                    text_message=RedirectConstants.ValidateExceptionMessageSourceFileNotExist,
                    close_application=False,
                )
            self.controller.exception(
                log_caller=_caller,
                log_message=e,
            )
            self.controller.debug(
                log_caller=_caller,
                log_message=f"{RedirectConstants.LogMessageFunctionReturned}({self.controller.get_line_number(-2)}): {inspect.stack()[0][3]} -> [FALSE]"
            )
            return False
        except Exception as e:
            if show_error_message:
                self.controller.open_message(
                    text_message=RedirectConstants.ValidateExceptionMessage,
                    close_application=False,
                )
            self.controller.exception(
                log_caller=_caller,
                log_message=e
            )
            self.controller.debug(
                log_caller=_caller,
                log_message=f"{RedirectConstants.LogMessageFunctionReturned}({self.controller.get_line_number(-2)}): {inspect.stack()[0][3]} -> [FALSE]"
            )
            return False