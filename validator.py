import os
from type import LogCaller
from constants import ViewConstants

_caller: LogCaller = LogCaller.Validator

class RedirectValidator():
    def __init__(
        self,
        controller,
    ):
        self.controller = controller

    def validate_websites(
        self,
        lst_dict_websites,
        show_error_message,
    ) -> bool:
        if lst_dict_websites:
            return True
        else:
            if show_error_message:
                self.controller.open_message(
                    text_message="Google Sheet does not contain any websites!",
                    close_application=True,
                )
            self.controller.error(
                log_caller=_caller,
                log_message=f"Google Sheet Document '{ViewConstants.GoogleSheetDocumentName}' does not contain any WEBSITE entries in the WEBSITES tab.",
            )
            return False

    def validate_shop_name(
        self,
        shop_name,
        show_error_message,
    ) -> bool:
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
    ) -> bool:
        try:
            if os.stat(
                path=source_file_name
            ).st_size > 0:
                return True
            else:
                if show_error_message:
                    self.controller.open_message(
                        text_message="Source File: EMPTY",
                        close_application=False,
                    )
                self.controller.error(
                    log_caller=_caller,
                    log_message=f"Source File: EMPTY -> '{source_file_name}'.",
                )
                return False
        except OSError:
            if show_error_message:
                self.controller.open_message(
                    text_message="Source File: DOES NOT EXIST",
                    close_application=False,
                )
            self.controller.error(
                log_caller=_caller,
                log_message=f"Source File: DOES NOT EXIST -> '{source_file_name}'.",
            )
            return False