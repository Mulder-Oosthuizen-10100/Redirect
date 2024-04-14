from view import RedirectView
from model import RedirectModel

class RedirectController:
    def __init__(self):
        # self.model = RedirectModel(self)
        self.view = RedirectView(
            self,
            # lst_dict_websites=self.model.lst_dict_websites,
            lst_dict_websites = [
                {"WEBSITE":"BagsOfFlags"},
                {"WEBSITE":"Bohocondo"},
                {"WEBSITE":"GaiterGoblin"},
                {"WEBSITE":"MyManFur"},
                {"WEBSITE":"OurCBDPantry"},
                {"WEBSITE":"SandmanShop"},
                {"WEBSITE":"BagsOfFlags"},
                {"WEBSITE":"Bohocondo"},
                {"WEBSITE":"GaiterGoblin"},
                {"WEBSITE":"MyManFur"},
                {"WEBSITE":"OurCBDPantry"},
                {"WEBSITE":"SandmanShop"},
            ],
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

if __name__ == "__main__":
    controller = RedirectController()