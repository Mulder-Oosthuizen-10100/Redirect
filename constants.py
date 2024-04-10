class ViewConstantsNamespace:
    #################### 
    # Button Constants #
    ####################

    # Font Family
    @property
    def ButtonFontFamily(self):
        return "Currier New"

    # Font Size
    @property
    def ButtonFontSize(self):
        return 12

    ################### 
    # Label Constants #
    ###################

    # Font Family
    @property
    def LabelFontFamily(self):
        return "Currier New"
    
    # Font Size
    @property
    def LabelFontSize(self):
        return 40
    
ViewConstants = ViewConstantsNamespace()