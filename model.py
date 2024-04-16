import gspread
# import re
from datetime import datetime


class RedirectModel():
    def __init__(self, controller):
        self.controller = controller

        self.service_account = gspread.service_account()
        self.sheet = self.service_account.open('WEBSITE_DATA')
        self.worksheet_websites = self.sheet.worksheet('WEBSITES')
        self.worksheet_keywords = self.sheet.worksheet('KEYWORDS')
        self.worksheet_remove_part = self.sheet.worksheet('REMOVE_PARTS')

        self.lst_dict_websites = self.worksheet_websites.get_all_records()
        self.lst_dict_remove_parts = self.worksheet_remove_part.get_all_records()
        self.lst_dict_keywords = self.worksheet_keywords.get_all_records()
    
    def set_source_file_name(self, file_name):
        print("set source file name:", file_name)
        self.source_file_name = file_name
    
    def set_redirect_folder_name(self, folder_name):
        self.redirect_folder_name = folder_name

    def set_shop_name(self, shop_name):
        self.shop_name = shop_name

    def generate_csv_file(self,):
        self.set_files()
        self.internal_generate_csv_file()

    def set_files(self,):
        self.source_file = open(self.source_file_name, 'r')

        self.redirect_file_name = str.replace(self.source_file_name,'.txt','_redirect.csv')
        self.redirect_file = open(self.redirect_file_name, 'a')

        self.unmatched_redirect_file_name = str.replace(self.source_file_name, '.txt', '_unmatched_urls.txt')
        self.unmatched_redirect_file = open(self.unmatched_redirect_file_name, 'a')

        # c:\projects\redirect\source.txt
        # c:\projects\redirect\source_redirect.csv
        # date_time_str = datetime.now()
        # dt_string = date_time_str.strftime("%Y_%m_%d__%H_%M_%S")

    def get_remove_part(self, shop_name):
        for website_remove_part in self.lst_dict_remove_parts:
            if shop_name == website_remove_part.get("WEBSITE"):
                remove_part = website_remove_part.get("REMOVE_PART")
                if remove_part:
                    return remove_part
            break
    
    def internal_generate_csv_file(self,):
        for line in self.source_file:
            if line.find("?") == -1:
                new_line = str.replace(line,"\n","")
                self.remove_part = self.get_remove_part(self.shop_name)
                if self.remove_part:
                    new_line = str.replace(new_line, self.remove_part, "")
                lower_line = new_line.lower()
                for dict_keyword in self.lst_dict_keywords:
                    if dict_keyword.get('WEBSITE') == self.shop_name:
                        found_keyword = False
                        if lower_line.find(dict_keyword.get('KEYWORD').lower()) != -1:
                            self.redirect_file.write(lower_line + '*,' + dict_keyword.get('URL') + "\n")
                            found_keyword = True
                            break

                if not found_keyword:
                    self.unmatched_redirect_file.write(lower_line + "\n")
                    for dict_keyword in self.lst_dict_keywords:
                        if dict_keyword.get('WEBSITE') == self.shop_name:
                            if dict_keyword.get('DEFAULT') == 'TRUE':
                                self.unmatched_redirect_file.write(lower_line + '*,' + dict_keyword.get('URL') + "\n")
                                break