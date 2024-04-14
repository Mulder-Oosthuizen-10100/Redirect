import gspread
import re
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

    def generate_csv_file(
        self,
        source_file_name,
        destination_folder,
        shop_name,
    ):
        self.set_files(
            source_file_name=source_file_name,
            destination_folder=destination_folder,
        )

        self.internal_generate_csv_file(shop_name)

    def set_files(
        self,
        source_file_name,
        destination_folder,
    ):
        self.source_file = open(source_file_name, 'r')
        self.destination_folder = destination_folder
        date_time_str = datetime.now()
        dt_string = date_time_str.strftime("%Y_%m_%d__%H_%M_%S")
        csv_directory = re.sub('.txt', "_" + dt_string + '.csv', self.destination_folder)
        unmatched_url_directory = re.sub('.txt', "_Unmatched_URLS_" + dt_string + ".txt", self.destination_folder)
        self.new_file = open(csv_directory, 'a')
        self.unmatched_url_file = open(unmatched_url_directory, 'a')

    def get_remove_part(self, shop_name):
        for website_remove_part in self.lst_dict_remove_parts:
            if shop_name == website_remove_part.get("WEBSITE"):
                remove_part = website_remove_part.get("REMOVE_PART")
                if remove_part:
                    return remove_part
            break
    
    def internal_generate_csv_file(
        self, 
        shop_name,
    ):
        for line in self.source_file:
            if line.find("?") == -1:
                new_line = re.sub("\n", "", line)
                self.remove_part = self.get_remove_part(shop_name)
                if self.remove_part:
                    new_line = re.sub(self.remove_part, "", new_line)
                    lower_line = new_line.lower()
                for dict_keyword in self.lst_dict_keywords:
                    if dict_keyword.get('WEBSITE') == shop_name:
                        found_keyword = False
                        if lower_line.find(dict_keyword.get('KEYWORD').lower()) != -1:
                            self.new_file.write(lower_line + '*,' + dict_keyword.get('URL') + "\n")
                            found_keyword = True
                            break

                if not found_keyword:
                    self.unmatched_url_file.write(lower_line + "\n")
                    for dict_keyword in self.lst_dict_keywords:
                        if dict_keyword.get('WEBSITE') == shop_name:
                            if dict_keyword.get('DEFAULT') == 'TRUE':
                                self.unmatched_url_file.write(lower_line + '*,' + dict_keyword.get('URL') + "\n")
                                break