from view import RedirectView
from model import RedirectModel
import os, sys
import threading
# import gc

class RedirectController:
    def __init__(self):
        # self.model = RedirectModel(self)
        # self.view = RedirectView(
        #     self,
        #     lst_dict_websites=self.model.lst_dict_websites,
        # )
        # self.view.root.mainloop()      

        # self.splash_screen_view = RedirectView(
        #     self,
        #     lst_dict_websites="",
        #     is_splash=True
        # )
        # self.splash_screen_view.root.mainloop()
        # self.model = RedirectModel(self)
  
        view_thread = threading.Thread(
            target=self.create_view,
            args=()
        )
        
        model_thread = threading.Thread(
            target=self.create_model,
            args=()
        )
        
        view_thread.start()
        model_thread.start()
        model_thread.join()

        self.splash_view.root.quit()

        # del self.splash_screen_view
        # gc.collect()


        # self.splash_screen_view.destroy()
        # self.splash_screen_view.refresh()
        # self.splash_screen_view.hide()
        print("view exited")

        self.view = RedirectView(
            self,
            lst_dict_websites=self.model.lst_dict_websites,
            is_splash=False
        )
        self.view.root.mainloop()

    def create_model(self):
        print("creating model")
        self.model = RedirectModel(self)
        print("model created successfully")
    
    def create_view(self):
        print("creating view")
        self.splash_view = RedirectView(
            self,
            lst_dict_websites="",
            is_splash=True
        )
        self.splash_view.root.mainloop()

    def set_source_file_name(self, file_name):
        self.model.set_source_file_name(file_name=file_name)
    
    def set_redirect_folder_name(self, folder):
        self.model.set_redirect_folder_name(folder_name=folder)
    
    def set_shop_name(self, shop_name):
        self.model.set_shop_name(shop_name=shop_name)

    def generate_csv_file(self):
        self.model.generate_csv_file()
    
    def resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

if __name__ == "__main__":
    controller = RedirectController()