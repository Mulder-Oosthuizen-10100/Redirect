from view import RedirectView
from model import RedirectModel
import os, sys

class RedirectController:
    def __init__(self):
        self.model = RedirectModel(self)
        self.view = RedirectView(
            self,
            lst_dict_websites=self.model.lst_dict_websites,
        )
        self.view.root.mainloop()
    
    def set_source_file_name(self, file_name):
        self.source_file_name = file_name
    
    def set_destination_folder(self, folder):
        self.destination_folder = folder
    
    def set_shop_name(self, shop_name):
        self.shop_name = shop_name
        print(self.shop_name)

    def generate_csv_file(self):
        print("Generating the file")
        self.model.generate_csv_file(
            source_file_name=self.source_file_name,
            destination_folder=self.destination_folder,
            shop_name=self.shop_name,
        )
    
    def resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

if __name__ == "__main__":
    controller = RedirectController()