import os

class RedirectValidator():
    def __init__(
        self,
        controller,
    ):
        self.controller = controller

    def validate_shop_name(
        self,
        shop_name,
    ) -> bool:
        if (len(shop_name) <= 1) or (not shop_name):
            msg = f"'{shop_name}' is not a valid shop name"
            self.controller.open_message(msg)
            print(msg)
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
                if show_error_message:
                    self.controller.open_message("Source File: OK")
                    print("Source File: OK")
                return True
            else:
                if show_error_message:
                    self.controller.open_message("Source File: EMPTY")
                    print("Source File: EMPTY")
                return False
        except OSError:
            if show_error_message:
                self.controller.open_message("Source File: DOES NOT EXIST")
                print("Source File: DOES NOT EXIST")
            return False