from type import *
from datetime import datetime
from constants import RedirectConstants
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
            log_message=f"{RedirectConstants.LogMessageClassInitializing}({self.controller.get_line_number(8)}): {self.__class__.__name__}"
        )
        self.shop_name = None

    def set_model_data(
        self
    ) -> bool:
        self.controller.info(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionCalled}({self.controller.get_line_number(5)}): {inspect.stack()[0][3].capitalize}"
        )
        
        self.service_account = gspread.service_account()
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionStatement}({self.controller.get_line_number(3)}): Service Account Loaded -> {self.service_account}"
        )

        self.sheet = self.service_account.open(RedirectConstants.GoogleSheetDocumentName)
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionStatement}({self.controller.get_line_number(3)}): Sheet Opened -> {self.sheet}"
        )

        self.worksheet_websites = self.sheet.worksheet(RedirectConstants.GoogleSheetTabWebsites)
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionStatement}({self.controller.get_line_number(3)}): Worksheet Websites Loaded -> {self.worksheet_websites}"
        )

        self.worksheet_keywords = self.sheet.worksheet(RedirectConstants.GoogleSheetTabKeywords)
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionStatement}({self.controller.get_line_number(3)}): Worksheet Keywords Loaded -> {self.worksheet_keywords}"
        )

        self.worksheet_remove_parts = self.sheet.worksheet(RedirectConstants.GoogleSheetTabRemoveParts)
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionStatement}({self.controller.get_line_number(3)}): Worksheet Remove Parts Loaded -> {self.worksheet_remove_parts}"
        )

        self.lst_dict_websites = self.worksheet_websites.get_all_records()
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionStatement}({self.controller.get_line_number(3)}): List of Dictionaries of Websites Loaded -> {self.lst_dict_websites}"
        )

        self.lst_dict_keywords = self.worksheet_keywords.get_all_records()
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionStatement}({self.controller.get_line_number(3)}): List of Dictionaries of Keywords Loaded -> {self.lst_dict_keywords}"
        )

        self.lst_dict_remove_parts = self.worksheet_remove_parts.get_all_records()
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionStatement}({self.controller.get_line_number(3)}): List of Dictionaries of Remove Parts Loaded -> {self.lst_dict_remove_parts}"
        )

        if self.controller.validate_worksheets(
            lst_dict_websites=self.lst_dict_websites,
            lst_dict_keywords=self.lst_dict_keywords,
            lst_dict_remove_parts=self.lst_dict_remove_parts,
            show_error_message=True,
        ):
            self.controller.debug(
                log_caller=_caller,
                log_message=f"{RedirectConstants.LogMessageFunctionReturned}({self.controller.get_line_number(-2)}): {inspect.stack()[0][3].capitalize} -> [TRUE]"
            )
            return True
        else:
            self.controller.debug(
                log_caller=_caller,
                log_message=f"{RedirectConstants.LogMessageFunctionReturned}({self.controller.get_line_number(-2)}): {inspect.stack()[0][3].capitalize} -> [FALSE]"
            )
            return False

    def get_default_directory(
        self
    ) -> str:
        self.controller.info(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionCalled}({self.controller.get_line_number(5)}): {inspect.stack()[0][3].capitalize}"
        )
        p = os.path.expanduser(
            path=RedirectConstants.DefaultDirectory
        )
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionReturned}({self.controller.get_line_number(-2)}): {inspect.stack()[0][3].capitalize} -> [{p}]"
        )
        return p
    
    def must_update_edt_redirect_folder_location(
        self
    ):
        self.controller.info(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionCalled}({self.controller.get_line_number(5)}): {inspect.stack()[0][3].capitalize}"
        )
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionReturned}({self.controller.get_line_number(-2)}): {inspect.stack()[0][3].capitalize} -> [{RedirectConstants.ResultMustUpdateRedirectFolder}]"
        )
        return RedirectConstants.ResultMustUpdateRedirectFolder
    
    def get_root_directory_from_source_file_name(
        self,
        source_file_name,
    ):
        self.controller.info(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionCalled}({self.controller.get_line_number(6)}): {inspect.stack()[0][3].capitalize}"
        )
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionParameters}({self.controller.get_line_number(-2)}): [Source File Name | {source_file_name}]"
        )
        p = os.path.dirname(
            p=source_file_name
        )
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionReturned}({self.controller.get_line_number(-2)}): {inspect.stack()[0][3].capitalize} -> [{p}]"
        )
        return p

    def set_source_file_name(
        self,
        file_name,
        show_error_message,
    ) -> bool:
        self.controller.info(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionCalled}({self.controller.get_line_number(8)}): {inspect.stack()[0][3].capitalize}"
        )
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionParameters}({self.controller.get_line_number(10)}): [Source File Name | {file_name}]"
        )
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionParameters}({self.controller.get_line_number(13)}): [Show Error Message | {show_error_message}]"
        )
        if self.controller.validate_source_file_name(
            source_file_name=file_name,
            show_error_message=show_error_message,
        ):
            self.source_file_name = file_name
            self.controller.debug(
                log_caller=_caller,
                log_message=f"{RedirectConstants.LogMessageFunctionReturned}({self.controller.get_line_number(-2)}): {inspect.stack()[0][3].capitalize} -> [TRUE]"
            )
            return True
        else:
            self.source_file_name = None
            self.controller.debug(
                log_caller=_caller,
                log_message=f"{RedirectConstants.LogMessageFunctionReturned}({self.controller.get_line_number(-2)}): {inspect.stack()[0][3].capitalize} -> [FALSE]"
            )
            return False

    def set_redirect_folder_name(
        self,
        folder_name
    ):
        self.controller.info(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionCalled}({self.controller.get_line_number(6)}): {inspect.stack()[0][3].capitalize}"
        )
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionParameters}({self.controller.get_line_number(8)}): [Folder Name | {folder_name}]"
        )
        self.redirect_folder_name = folder_name

    def set_shop_name(
        self,
        shop_name,
        show_error_message
    ):
        self.controller.info(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionCalled}({self.controller.get_line_number(7)}): {inspect.stack()[0][3].capitalize}"
        )
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionParameters}({self.controller.get_line_number(9)}): [Shop Name | {shop_name}]"
        )
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionParameters}({self.controller.get_line_number(12)}): [Show Error Message | {show_error_message}]"
        )
        if self.controller.validate_shop_name(
            shop_name=shop_name,
            show_error_message=show_error_message,
        ):
            self.shop_name = shop_name

    def generate_csv_file(
        self,
        show_error_message,
    ):
        self.controller.info(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionCalled}({self.controller.get_line_number(8)}): {inspect.stack()[0][3].capitalize}"
        )
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionParameters}({self.controller.get_line_number(9)}): [Show Error Message | {show_error_message}]"
        )
        if self.controller.validate_shop_name(
            shop_name=self.shop_name,
            show_error_message=show_error_message,
        ):
            if self.open_files(
                show_error_message=show_error_message,
            ):
                try:
                    self.controller.debug(
                        log_caller=_caller,
                        log_message=f"{RedirectConstants.LogMessageFunctionStatement}({self.controller.get_line_number(3)}): TRY..."
                    )
                    self.internal_generate_csv_file(
                        show_error_message=show_error_message,
                    )
                    self.controller.open_message(
                        text_message=RedirectConstants.RedirectSuccessMessage,
                        close_application=False,
                    )
                except Exception as e:
                    self.controller.debug(
                        log_caller=_caller,
                        log_message=f"{RedirectConstants.LogMessageFunctionStatement}({self.controller.get_line_number(3)}): ...EXCEPT..."
                    )
                    self.controller.open_message(
                        text_message=RedirectConstants.ModelExceptionMessageRedirectProcess,
                        close_application=False,
                    )
                    self.controller.exception(
                        log_caller=_caller,
                        log_message=e,
                    )
                finally:
                    self.controller.debug(
                        log_caller=_caller,
                        log_message=f"{RedirectConstants.LogMessageFunctionStatement}({self.controller.get_line_number(3)}): ...FINALLY"
                    )
                    self.close_files()

    def open_files(
        self,
        show_error_message,
    ) -> bool:
        self.controller.info(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionCalled}({self.controller.get_line_number(7)}): {inspect.stack()[0][3].capitalize}"
        )
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionParameters}({self.controller.get_line_number(9)}): [Show Error Message | {show_error_message}]"
        )
        date_time = datetime.now()
        date_time_string = date_time.strftime(RedirectConstants.OutputFileNameFormat)
        self.redirect_file_name = self.redirect_folder_name + '\\' + f'{RedirectConstants.RedirectOutputFileName}{date_time_string}.csv'
        self.unmatched_redirect_file_name = self.redirect_folder_name + '\\' + f'{RedirectConstants.UnmatchedRedirectOutputFileName}{date_time_string}.txt'

        if self.controller.validate_source_file_name(
            source_file_name=self.source_file_name,
            show_error_message=show_error_message,
        ):
            self.source_file = open(self.source_file_name, 'r')
            self.controller.debug(
                log_caller=_caller,
                log_message=f"{RedirectConstants.LogMessageFunctionStatement}({self.controller.get_line_number(3)}): Source File Opened -> {self.source_file}"
            )
            self.redirect_file = open(self.redirect_file_name, 'a')
            self.controller.debug(
                log_caller=_caller,
                log_message=f"{RedirectConstants.LogMessageFunctionStatement}({self.controller.get_line_number(3)}): Redirect File Opened -> {self.redirect_file}"
            )
            self.unmatched_redirect_file = open(self.unmatched_redirect_file_name, 'a')
            self.controller.debug(
                log_caller=_caller,
                log_message=f"{RedirectConstants.LogMessageFunctionStatement}({self.controller.get_line_number(3)}): Unmatched Redirect File Opened -> {self.unmatched_redirect_file}"
            )
            self.controller.debug(
                log_caller=_caller,
                log_message=f"{RedirectConstants.LogMessageFunctionReturned}({self.controller.get_line_number(-2)}): {inspect.stack()[0][3].capitalize} -> [TRUE]"
            )
            return True

    def close_files(
        self
    ):
        self.controller.info(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionCalled}({self.controller.get_line_number(6)}): {inspect.stack()[0][3].capitalize}"
        )
        if self.source_file:
            self.controller.debug(
                log_caller=_caller,
                log_message=f"{RedirectConstants.LogMessageFunctionStatement}({self.controller.get_line_number(3)}): Source File Opened -> Closing Other Files"
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
            log_message=f"{RedirectConstants.LogMessageFunctionCalled}({self.controller.get_line_number(7)}): {inspect.stack()[0][3].capitalize}"
        )
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionParameters}({self.controller.get_line_number(9)}): [Shop Name | {shop_name}]"
        )
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionParameters}({self.controller.get_line_number(12)}): [Show Error Message | {show_error_message}]"
        )
        for website_remove_part in self.lst_dict_remove_parts:
            if shop_name == website_remove_part.get(RedirectConstants.KeyWebsite):
                remove_part = website_remove_part.get(RedirectConstants.KeyRemovePart)
                if remove_part:
                    self.controller.debug(
                        log_caller=_caller,
                        log_message=f"{RedirectConstants.LogMessageFunctionReturned}({self.controller.get_line_number(-2)}): {inspect.stack()[0][3].capitalize} -> [{remove_part}]"
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
                        log_message=f"{RedirectConstants.LogMessageFunctionReturned}({self.controller.get_line_number(-2)}): {inspect.stack()[0][3].capitalize} -> [{RedirectConstants.EmptyString}]"
                    )
                    return RedirectConstants.EmptyString
    
    def internal_generate_csv_file(
        self,
        show_error_message,
    ):
        self.controller.info(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionCalled}({self.controller.get_line_number(6)}): {inspect.stack()[0][3].capitalize}"
        )
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionParameters}({self.controller.get_line_number(9)}): [Show Error Message | {show_error_message}]"
        )
        remove_part = self.get_remove_part(
            shop_name=self.shop_name,
            show_error_message=show_error_message,
        )

        for line in self.source_file:
            try:
                self.controller.debug(
                    log_caller=_caller,
                    log_message=f"{RedirectConstants.LogMessageFunctionStatement}({self.controller.get_line_number(3)}): TRY..."
                )
                line = line.rstrip('\n\t')
            except Exception as e:
                self.controller.debug(
                    log_caller=_caller,
                    log_message=f"{RedirectConstants.LogMessageFunctionStatement}({self.controller.get_line_number(3)}): ...EXCEPT..."
                )
                self.controller.open_message(
                    text_message=RedirectConstants.ModelExceptionMessageProcessLine,
                    close_application=True
                )
                self.controller.exception(
                    log_caller=_caller,
                    log_message=e,
                )

            line = str.replace(
                line,
                remove_part,
                RedirectConstants.EmptyString,
            )
            line = line.lower()
            self.controller.debug(
                log_caller=_caller,
                log_message=f"{RedirectConstants.LogMessageFunctionStatement}({self.controller.get_line_number(3)}): Processed Line -> {line}"
            )

            for dict_keyword in self.lst_dict_keywords:
                if dict_keyword.get(RedirectConstants.KeyWebsite) == self.shop_name:
                    found_keyword = False
                    keyword = dict_keyword.get(RedirectConstants.KeyKeyword).lower()
                    if keyword in line:
                        final_line = line + '*,' + dict_keyword.get(RedirectConstants.KeyURL) 
                        self.redirect_file.write(final_line + "\n")
                        self.controller.debug(
                            log_caller=_caller,
                            log_message=f"{RedirectConstants.LogMessageFunctionStatement}({self.controller.get_line_number(3)}): Final Line with Keyword [{keyword}] -> {final_line}"
                        )
                        found_keyword = True
                        break

            if not found_keyword:
                self.controller.debug(
                    log_caller=_caller,
                    log_message=f"{RedirectConstants.LogMessageFunctionStatement}({self.controller.get_line_number(3)}): No matching Keyword found for Processed Line -> {line}"
                )
                self.unmatched_redirect_file.write(line + "\n")
                for dict_keyword in self.lst_dict_keywords:
                    if dict_keyword.get(RedirectConstants.KeyWebsite) == self.shop_name:
                        if dict_keyword.get(RedirectConstants.KeyDefault) == 'TRUE':
                            self.redirect_file.write(line + '*,' + dict_keyword.get(RedirectConstants.KeyURL) + "\n")
                            self.controller.debug(
                                log_caller=_caller,
                                log_message=f"{RedirectConstants.LogMessageFunctionStatement}({self.controller.get_line_number(3)}): No matching Keyword found applying default -> {dict_keyword.get('KEYWORD').lower()} ({dict_keyword.get('URL')})"
                            )
                            break
        self.controller.debug(
            log_caller=_caller,
            log_message=f"{RedirectConstants.LogMessageFunctionReturned}({self.controller.get_line_number(0)}): {inspect.stack()[0][3].capitalize} -> [None]"
        )