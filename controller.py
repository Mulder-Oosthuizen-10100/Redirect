from view import RedirectView

class RedirectController:
    def __init__(self):
        self.view = RedirectView(self)
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