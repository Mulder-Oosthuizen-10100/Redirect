import os
from type import LogCaller

_caller: LogCaller = LogCaller.Validator

class RedirectValidator():
    def __init__(
        self,
        controller,
    ):
        self.controller = controller

    def validate_shop_name(
        self,
        shop_name,
        show_error_message,
    ) -> bool:
        if not shop_name:
            self.controller.error(
                log_caller=_caller,
                log_message=f"Invalid shop name '{shop_name}'",
            )

            if show_error_message:
                self.controller.open_message(
                    text_message="Please select a shop name"
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
                    self.controller.open_message("Source File: EMPTY")

                self.controller.error(
                    log_caller=_caller,
                    log_message=f"Source File: EMPTY -> '{source_file_name}'",
                )

                return False
        except OSError:
            if show_error_message:
                self.controller.open_message("Source File: DOES NOT EXIST")

            self.controller.error(
                log_caller=_caller,
                log_message=f"Source File: DOES NOT EXIST -> '{source_file_name}'",
            )

            return False