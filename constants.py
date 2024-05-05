class classproperty(object):
    def __init__(self, fget):
        self.fget = fget
    def __get__(self, owner_self, owner_class):
        return self.fget(owner_class)

class RedirectConstants:
    @property
    def LogMessageApplicationStarting(self):
        return "APPLICATION_STARTING"
    
    @property
    def LogMessageApplicationGUIBuilt(self):
        return "APPLICATION_GUI_BUILT"

    @property
    def LogMessageApplicationDataRetrieved(self):
        return "APPLICATION_DATA_RETRIEVED"
    
    @property
    def LogMessageApplicationClosing(self):
        return "APPLICATION_CLOSING"
    
    @property
    def LogMessageUserInteractionStart(self):
        return "USER_INTERACTION_START"

    @property
    def LogMessageUserInteractionEnd(self):
        return "USER_INTERACTION_END"

    @property
    def LogMessageClassInitializing(self):
        return " CLASS_INITIALIZING    "

    @property
    def LogMessageClassInitialized(self):
        return " CLASS_INITIALIZED     "
    
    @property
    def LogMessageFunctionCalled(self):
        return "  FUNCTION_CALLED      "
    
    @property
    def LogMessageFunctionStatement(self):
        return "   FUNCTION_STATEMENT  "

    @property
    def LogMessageFunctionReturned(self):
        return "   FUNCTION_RETURNED   "
    
    @property
    def LogMessageFunctionParameters(self):
        return "   FUNCTION_PARAMETERS "

    @property
    def LogMessageForLoop(self):
        return "   FOR_LOOP            "

    @property
    def PathRedirectLogo(self):
        return "images\\RedirectLogo.ico"
    
    @property
    def TitleSourceFileDialog(self):
        return "Select the Source File that contains the URLs with 404 errors."

    @classproperty
    def ConfigurationFileName(self) -> str:
        return "Redirect.ini"

    @classproperty
    def ConfigurationSectionLogging(self) -> str:
        return "LOGGING"

    @classproperty
    def ConfigurationKeyLogLevel(self) -> str:
        return "LogLevel"



    @property
    def ButtonFontFamily(self):
        return "Currier New"

    @property
    def ButtonFontSize(self):
        return 12

    @property
    def LabelFontFamily(self):
        return "JetBrains Mono"
    
    @property
    def LabelFontSize(self):
        return 40
    
    @property
    def GoogleSheetDocumentName(self):
        return "WEBSITE_DATA"

# Add the default source file location to the constants file