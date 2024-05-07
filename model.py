from type import *
from datetime import datetime
import gspread, os, inspect

_caller: LogCaller = LogCaller.Model

class RedirectModel():
    def __init__(
        self,
        controller
    ):
        self.controller = controller
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{self.controller.const.LogMessageClassInitializing}({self.controller.get_line_number(8)}): {self.__class__.__name__}"
        )
        self.shop_name = None

    def set_model_data(
        self
    ) -> bool:
        self.controller.info(
            log_caller=_caller,
            log_message=f"{self.controller.const.LogMessageFunctionCalled}({self.controller.get_line_number(5)}): {inspect.stack()[0][3]}"
        )
        
        self.service_account = gspread.service_account()
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{self.controller.const.LogMessageFunctionStatement}({self.controller.get_line_number(3)}): Service Account Loaded -> {self.service_account}"
        )

        self.sheet = self.service_account.open('WEBSITE_DATA')
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{self.controller.const.LogMessageFunctionStatement}({self.controller.get_line_number(3)}): Sheet Opened -> {self.sheet}"
        )

        self.worksheet_websites = self.sheet.worksheet('WEBSITES')
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{self.controller.const.LogMessageFunctionStatement}({self.controller.get_line_number(3)}): Worksheet Websites Loaded -> {self.worksheet_websites}"
        )

        self.worksheet_keywords = self.sheet.worksheet('KEYWORDS')
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{self.controller.const.LogMessageFunctionStatement}({self.controller.get_line_number(3)}): Worksheet Keywords Loaded -> {self.worksheet_keywords}"
        )

        self.worksheet_remove_parts = self.sheet.worksheet('REMOVE_PARTS')
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{self.controller.const.LogMessageFunctionStatement}({self.controller.get_line_number(3)}): Worksheet Remove Parts Loaded -> {self.worksheet_remove_parts}"
        )

        self.lst_dict_websites = self.worksheet_websites.get_all_records()
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{self.controller.const.LogMessageFunctionStatement}({self.controller.get_line_number(3)}): List of Dictionaries of Websites Loaded -> {self.lst_dict_websites}"
        )

        self.lst_dict_keywords = self.worksheet_keywords.get_all_records()
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{self.controller.const.LogMessageFunctionStatement}({self.controller.get_line_number(3)}): List of Dictionaries of Keywords Loaded -> {self.lst_dict_keywords}"
        )

        self.lst_dict_remove_parts = self.worksheet_remove_parts.get_all_records()
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{self.controller.const.LogMessageFunctionStatement}({self.controller.get_line_number(3)}): List of Dictionaries of Remove Parts Loaded -> {self.lst_dict_remove_parts}"
        )

        if self.controller.validate_worksheets(
            lst_dict_websites=self.lst_dict_websites,
            lst_dict_keywords=self.lst_dict_keywords,
            lst_dict_remove_parts=self.lst_dict_remove_parts,
            show_error_message=True,
        ):
            self.controller.debug(
                log_caller=_caller,
                log_message=f"{self.controller.const.LogMessageFunctionReturned}({self.controller.get_line_number(-2)}): {inspect.stack()[0][3]} -> [TRUE]"
            )
            return True
        else:
            self.controller.debug(
                log_caller=_caller,
                log_message=f"{self.controller.const.LogMessageFunctionReturned}({self.controller.get_line_number(-2)}): {inspect.stack()[0][3]} -> [FALSE]"
            )
            return False

    def get_default_directory(
        self
    ) -> str:
        self.controller.info(
            log_caller=_caller,
            log_message=f"{self.controller.const.LogMessageFunctionCalled}({self.controller.get_line_number(5)}): {inspect.stack()[0][3]}"
        )
        p = os.path.expanduser(
            path="~\\Documents"
        )
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{self.controller.const.LogMessageFunctionReturned}({self.controller.get_line_number(-2)}): {inspect.stack()[0][3]} -> [{p}]"
        )
        return p
    
    def must_update_edt_redirect_folder_location(
        self
    ):
        self.controller.info(
            log_caller=_caller,
            log_message=f"{self.controller.const.LogMessageFunctionCalled}({self.controller.get_line_number(5)}): {inspect.stack()[0][3]}"
        )
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{self.controller.const.LogMessageFunctionReturned}({self.controller.get_line_number(-2)}): {inspect.stack()[0][3]} -> [{self.controller.const.ResultMustUpdateRedirectFolder}]"
        )
        return self.controller.const.ResultMustUpdateRedirectFolder
    
    def get_root_directory_from_source_file_name(
        self,
        source_file_name,
    ):
        self.controller.info(
            log_caller=_caller,
            log_message=f"{self.controller.const.LogMessageFunctionCalled}({self.controller.get_line_number(6)}): {inspect.stack()[0][3]}"
        )
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{self.controller.const.LogMessageFunctionParameters}({self.controller.get_line_number(-2)}): [Source File Name | {source_file_name}]"
        )
        p = os.path.dirname(
            p=source_file_name
        )
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{self.controller.const.LogMessageFunctionReturned}({self.controller.get_line_number(-2)}): {inspect.stack()[0][3]} -> [{p}]"
        )
        return p

    def set_source_file_name(
        self,
        file_name,
        show_error_message,
        log_error_message,
    ) -> bool:
        self.controller.info(
            log_caller=_caller,
            log_message=f"{self.controller.const.LogMessageFunctionCalled}({self.controller.get_line_number(8)}): {inspect.stack()[0][3]}"
        )
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{self.controller.const.LogMessageFunctionParameters}({self.controller.get_line_number(10)}): [Source File Name | {file_name}]"
        )
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{self.controller.const.LogMessageFunctionParameters}({self.controller.get_line_number(13)}): [Show Error Message | {show_error_message}]"
        )
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{self.controller.const.LogMessageFunctionParameters}({self.controller.get_line_number(16)}): [Log Error Message | {log_error_message}]"
        )
        if self.controller.validate_source_file_name(
            source_file_name=file_name,
            show_error_message=show_error_message,
            log_error_message=log_error_message,
        ):
            self.source_file_name = file_name
            self.controller.debug(
                log_caller=_caller,
                log_message=f"{self.controller.const.LogMessageFunctionReturned}({self.controller.get_line_number(-2)}): {inspect.stack()[0][3]} -> [TRUE]"
            )
            return True
        else:
            self.source_file_name = None
            self.controller.debug(
                log_caller=_caller,
                log_message=f"{self.controller.const.LogMessageFunctionReturned}({self.controller.get_line_number(-2)}): {inspect.stack()[0][3]} -> [FALSE]"
            )
            return False

    def set_redirect_folder_name(
        self,
        folder_name
    ):
        self.controller.info(
            log_caller=_caller,
            log_message=f"{self.controller.const.LogMessageFunctionCalled}({self.controller.get_line_number(6)}): {inspect.stack()[0][3]}"
        )
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{self.controller.const.LogMessageFunctionParameters}({self.controller.get_line_number(8)}): [Folder Name | {folder_name}]"
        )
        self.redirect_folder_name = folder_name

    def set_shop_name(
        self,
        shop_name,
        show_error_message
    ):
        self.controller.info(
            log_caller=_caller,
            log_message=f"{self.controller.const.LogMessageFunctionCalled}({self.controller.get_line_number(7)}): {inspect.stack()[0][3]}"
        )
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{self.controller.const.LogMessageFunctionParameters}({self.controller.get_line_number(9)}): [Shop Name | {shop_name}]"
        )
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{self.controller.const.LogMessageFunctionParameters}({self.controller.get_line_number(12)}): [Show Error Message | {show_error_message}]"
        )
        if self.controller.validate_shop_name(
            shop_name=shop_name,
            show_error_message=show_error_message,
        ):
            self.shop_name = shop_name

    def generate_csv_file(
        self,
        show_error_message,
        log_error_message,
    ):
        self.controller.info(
            log_caller=_caller,
            log_message=f"{self.controller.const.LogMessageFunctionCalled}({self.controller.get_line_number(8)}): {inspect.stack()[0][3]}"
        )
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{self.controller.const.LogMessageFunctionParameters}({self.controller.get_line_number(9)}): [Show Error Message | {show_error_message}]"
        )
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{self.controller.const.LogMessageFunctionParameters}({self.controller.get_line_number(11)}): [Log Error Message | {log_error_message}]"
        )
        if self.controller.validate_shop_name(
            shop_name=self.shop_name,
            show_error_message=show_error_message,
        ):
            if self.open_files(
                show_error_message=show_error_message,
                log_error_message=log_error_message,
            ):
                try:
                    self.controller.debug(
                        log_caller=_caller,
                        log_message=f"{self.controller.const.LogMessageFunctionStatement}({self.controller.get_line_number(3)}): TRY..."
                    )
                    self.internal_generate_csv_file(
                        show_error_message=show_error_message,
                    )
                    self.controller.open_message(
                        text_message="Successfully Redirected the Source File!",
                        close_application=False,
                    )
                except Exception as e:
                    self.controller.debug(
                        log_caller=_caller,
                        log_message=f"{self.controller.const.LogMessageFunctionStatement}({self.controller.get_line_number(3)}): ...EXCEPT..."
                    )
                    self.controller.open_message(
                        text_message=f"An Error occurred during the redirect process! Error Message: {e}",
                        close_application=False,
                    )
                finally:
                    self.controller.debug(
                        log_caller=_caller,
                        log_message=f"{self.controller.const.LogMessageFunctionStatement}({self.controller.get_line_number(3)}): ...FINALLY"
                    )
                    self.close_files()

    def open_files(
        self,
        show_error_message,
        log_error_message,
    ) -> bool:
        self.controller.info(
            log_caller=_caller,
            log_message=f"{self.controller.const.LogMessageFunctionCalled}({self.controller.get_line_number(7)}): {inspect.stack()[0][3]}"
        )
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{self.controller.const.LogMessageFunctionParameters}({self.controller.get_line_number(9)}): [Show Error Message | {show_error_message}]"
        )
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{self.controller.const.LogMessageFunctionParameters}({self.controller.get_line_number(12)}): [Log Error Message | {log_error_message}]"
        )
        date_time = datetime.now()
        date_time_string = date_time.strftime("%Y_%m_%d__%H_%M_%S")
        self.redirect_file_name = self.redirect_folder_name + '\\' + f'redirect_{date_time_string}.csv'
        self.unmatched_redirect_file_name = self.redirect_folder_name + '\\' + f'unmatched_urls_{date_time_string}.txt'

        if self.controller.validate_source_file_name(
            source_file_name=self.source_file_name,
            show_error_message=show_error_message,
            log_error_message=log_error_message,
        ):
            self.source_file = open(self.source_file_name, 'r')
            self.controller.debug(
                log_caller=_caller,
                log_message=f"{self.controller.const.LogMessageFunctionStatement}({self.controller.get_line_number(3)}): Source File Opened -> {self.source_file}"
            )
            self.redirect_file = open(self.redirect_file_name, 'a')
            self.controller.debug(
                log_caller=_caller,
                log_message=f"{self.controller.const.LogMessageFunctionStatement}({self.controller.get_line_number(3)}): Redirect File Opened -> {self.redirect_file}"
            )
            self.unmatched_redirect_file = open(self.unmatched_redirect_file_name, 'a')
            self.controller.debug(
                log_caller=_caller,
                log_message=f"{self.controller.const.LogMessageFunctionStatement}({self.controller.get_line_number(3)}): Unmatched Redirect File Opened -> {self.unmatched_redirect_file}"
            )
            self.controller.debug(
                log_caller=_caller,
                log_message=f"{self.controller.const.LogMessageFunctionReturned}({self.controller.get_line_number(-2)}): {inspect.stack()[0][3]} -> [TRUE]"
            )
            return True

    def close_files(
        self
    ):
        self.controller.info(
            log_caller=_caller,
            log_message=f"{self.controller.const.LogMessageFunctionCalled}({self.controller.get_line_number(6)}): {inspect.stack()[0][3]}"
        )
        if self.source_file:
            self.controller.debug(
                log_caller=_caller,
                log_message=f"{self.controller.const.LogMessageFunctionStatement}({self.controller.get_line_number(3)}): Source File Opened -> Closing Other Files"
            )
            self.source_file.close()
            self.redirect_file.close()
            self.unmatched_redirect_file.close()

    def get_remove_part(
        self,
        shop_name,
        show_error_message
    ):
        self.controller.info(
            log_caller=_caller,
            log_message=f"{self.controller.const.LogMessageFunctionCalled}({self.controller.get_line_number(7)}): {inspect.stack()[0][3]}"
        )
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{self.controller.const.LogMessageFunctionParameters}({self.controller.get_line_number(9)}): [Shop Name | {shop_name}]"
        )
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{self.controller.const.LogMessageFunctionParameters}({self.controller.get_line_number(12)}): [Show Error Message | {show_error_message}]"
        )
        for website_remove_part in self.lst_dict_remove_parts:
            if shop_name == website_remove_part.get("WEBSITE"):
                remove_part = website_remove_part.get("REMOVE_PART")
                if remove_part:
                    self.controller.debug(
                        log_caller=_caller,
                        log_message=f"{self.controller.const.LogMessageFunctionReturned}({self.controller.get_line_number(-2)}): {inspect.stack()[0][3]} -> [{remove_part}]"
                    )
                    return remove_part
                else:
                    if show_error_message:
                        self.controller.open_message(
                            text_message=f"WARNING: There are no remove parts for shop '{shop_name}'.",
                            close_application=False
                        )
                    self.controller.warn(
                        log_caller=_caller,
                        log_message=f"There are no remove parts for shop '{shop_name}'.",
                    )
                    self.controller.debug(
                        log_caller=_caller,
                        log_message=f"{self.controller.const.LogMessageFunctionReturned}({self.controller.get_line_number(-2)}): {inspect.stack()[0][3]} -> [{self.controller.const.EmptyString}]"
                    )
                    return self.controller.const.EmptyString
    
    def internal_generate_csv_file(
        self,
        show_error_message,
    ):
        self.controller.info(
            log_caller=_caller,
            log_message=f"{self.controller.const.LogMessageFunctionCalled}({self.controller.get_line_number(6)}): {inspect.stack()[0][3]}"
        )
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{self.controller.const.LogMessageFunctionParameters}({self.controller.get_line_number(9)}): [Show Error Message | {show_error_message}]"
        )
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
            self.controller.debug(
                log_caller=_caller,
                log_message=f"{self.controller.const.LogMessageFunctionStatement}({self.controller.get_line_number(3)}): Processed Line -> {line}"
            )

            for dict_keyword in self.lst_dict_keywords:
                if dict_keyword.get('WEBSITE') == self.shop_name:
                    found_keyword = False
                    keyword = dict_keyword.get('KEYWORD').lower()
                    if keyword in line:
                        final_line = line + '*,' + dict_keyword.get('URL') 
                        self.redirect_file.write(final_line + "\n")
                        self.controller.debug(
                            log_caller=_caller,
                            log_message=f"{self.controller.const.LogMessageFunctionStatement}({self.controller.get_line_number(3)}): Final Line with Keyword [{keyword}] -> {final_line}"
                        )
                        found_keyword = True
                        break

            if not found_keyword:
                self.controller.debug(
                    log_caller=_caller,
                    log_message=f"{self.controller.const.LogMessageFunctionStatement}({self.controller.get_line_number(3)}): No matching Keyword found for Processed Line -> {line}"
                )
                self.unmatched_redirect_file.write(line + "\n")
                for dict_keyword in self.lst_dict_keywords:
                    if dict_keyword.get('WEBSITE') == self.shop_name:
                        if dict_keyword.get('DEFAULT') == 'TRUE':
                            self.redirect_file.write(line + '*,' + dict_keyword.get('URL') + "\n")
                            self.controller.debug(
                                log_caller=_caller,
                                log_message=f"{self.controller.const.LogMessageFunctionStatement}({self.controller.get_line_number(3)}): No matching Keyword found applying default -> {dict_keyword.get('KEYWORD').lower()} ({dict_keyword.get('URL')})"
                            )
                            break
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{self.controller.const.LogMessageFunctionReturned}({self.controller.get_line_number(0)}): {inspect.stack()[0][3]} -> [None]"
        )