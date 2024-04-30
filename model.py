from type import *
import gspread, os
from datetime import datetime

_caller = "MODEL"

class RedirectModel():
    def __init__(
        self,
        controller
    ):
        self.controller = controller
        self.shop_name = None
    
    def get_log_config(self) -> LogConfig:
        return LogConfig(
            log_file_location = self.get_log_file_location(),
            log_file_name = self.get_log_file_name(),
            log_mode = LogMode.Append,
            log_level = LogLevel.Debug,
        )

    def get_log_file_name(self) -> str:
        date_time_string = datetime.now().strftime("%d-%m-%Y")
        log_file_name = date_time_string + ".log"
        return log_file_name
    
    def get_log_file_location(self) -> str:
        year_string = datetime.now().strftime("%Y") + "\\"
        month_string = datetime.now().strftime("%B")
        log_file_location = os.getcwd() + "\\" + "log\\" + year_string + month_string
        return log_file_location

    def set_model_data(self) -> bool:
        self.service_account = gspread.service_account()
        self.sheet = self.service_account.open('WEBSITE_DATA')
        self.worksheet_websites = self.sheet.worksheet('WEBSITES')
        self.worksheet_keywords = self.sheet.worksheet('KEYWORDS')
        self.worksheet_remove_parts = self.sheet.worksheet('REMOVE_PARTS')

        self.lst_dict_websites = self.worksheet_websites.get_all_records()
        self.lst_dict_remove_parts = self.worksheet_remove_parts.get_all_records()
        self.lst_dict_keywords = self.worksheet_keywords.get_all_records()

        if self.controller.validate_worksheets(
            lst_dict_websites=self.lst_dict_websites,
            lst_dict_keywords=self.lst_dict_keywords,
            lst_dict_remove_parts=self.lst_dict_remove_parts,
            show_error_message=True,
        ):
            return True
        else:
            return False

    def get_default_directory(self) -> str:
        return os.path.expanduser("~\\Documents")
    
    def must_update_edt_redirect_folder_location(self):
        return True
    
    def get_root_directory_from_source_file_name(
        self,
        source_file_name,
    ):
        return os.path.dirname(source_file_name)

    def set_source_file_name(
        self,
        file_name,
        show_error_message,
    ) -> bool:
        if self.controller.validate_source_file_name(
            source_file_name=file_name,
            show_error_message=show_error_message,            
        ):
            self.source_file_name = file_name
            return True
        else:
            self.source_file_name = None
            return False

    def set_redirect_folder_name(self, folder_name):
        self.redirect_folder_name = folder_name

    def set_shop_name(
        self,
        shop_name,
        show_error_message
    ):
        if self.controller.validate_shop_name(
            shop_name=shop_name,
            show_error_message=show_error_message,
        ):
            self.shop_name = shop_name

    def generate_csv_file(
        self,
        show_error_message,
    ):
        if self.controller.validate_shop_name(
            shop_name=self.shop_name,
            show_error_message=show_error_message,
        ):
            if self.open_files(
                show_error_message=show_error_message,
            ):
                try:
                    self.internal_generate_csv_file(
                        show_error_message=show_error_message,
                    )
                    self.controller.open_message(
                        text_message="Successfully Redirected the Source File!",
                        close_application=False,
                    )
                except Exception as e:
                    self.controller.open_message(
                        text_message=f"An Error occurred during the redirect process! Error Message: {e}",
                        close_application=False,
                    )
                finally:
                    self.close_files()

    def open_files(
        self,
        show_error_message,
    ) -> bool:
        date_time = datetime.now()
        date_time_string = date_time.strftime("%Y_%m_%d__%H_%M_%S")
        self.redirect_file_name = self.redirect_folder_name + '\\' + f'redirect_{date_time_string}.csv'
        self.unmatched_redirect_file_name = self.redirect_folder_name + '\\' + f'unmatched_urls_{date_time_string}.txt'

        if self.controller.validate_source_file_name(
            source_file_name=self.source_file_name,
            show_error_message=show_error_message,
        ):
            self.source_file = open(self.source_file_name, 'r')
            self.redirect_file = open(self.redirect_file_name, 'a')
            self.unmatched_redirect_file = open(self.unmatched_redirect_file_name, 'a')
            return True

    def close_files(self):
        if self.source_file:
            self.source_file.close()
            self.redirect_file.close()
            self.unmatched_redirect_file.close()

    def get_remove_part(
        self,
        shop_name,
        show_error_message
    ):
        for website_remove_part in self.lst_dict_remove_parts:
            if shop_name == website_remove_part.get("WEBSITE"):
                remove_part = website_remove_part.get("REMOVE_PART")
                if remove_part:
                    return remove_part
                else:
                    if show_error_message:
                        self.controller.open_message(
                            text_message=f"WARNING: There are no remove parts for shop {shop_name}.",
                            close_application=False
                        )
                    return ""
    
    def internal_generate_csv_file(
        self,
        show_error_message,
    ):
        remove_part = self.get_remove_part(
            shop_name=self.shop_name,
            show_error_message=show_error_message,
        )

        for line in self.source_file:
            line = str.replace(line, "\n", "")
            line = str.replace(line, "\t", "")
            line = str.replace(
                line,
                remove_part,
                ""
            )
            line = line.lower()

            for dict_keyword in self.lst_dict_keywords:
                if dict_keyword.get('WEBSITE') == self.shop_name:
                    found_keyword = False
                    if dict_keyword.get('KEYWORD').lower() in line:
                        self.redirect_file.write(line + '*,' + dict_keyword.get('URL') + "\n")
                        found_keyword = True
                        break

            if not found_keyword:
                self.unmatched_redirect_file.write(line + "\n")
                for dict_keyword in self.lst_dict_keywords:
                    if dict_keyword.get('WEBSITE') == self.shop_name:
                        if dict_keyword.get('DEFAULT') == 'TRUE':
                            self.redirect_file.write(line + '*,' + dict_keyword.get('URL') + "\n")
                            break