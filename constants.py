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
        return "JetBrains Mono"
    
    # Font Size
    @property
    def LabelFontSize(self):
        return 40
    
    @property
    def GoogleSheetDocumentName(self):
        return "WEBSITE_DATA"

ViewConstants = ViewConstantsNamespace()

# Add the default source file location to the constants file