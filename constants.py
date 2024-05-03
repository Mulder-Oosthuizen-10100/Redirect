class classproperty(object):
    def __init__(self, fget):
        self.fget = fget
    def __get__(self, owner_self, owner_class):
        return self.fget(owner_class)

class RedirectConstants:
    @property
    def LogMessageApplicationStart(self):
        return "APPLICATION_STARTED"

    @property
    def LogMessageClassInitializing(self):
        return "  CLASS_INITIALIZING"

    @property
    def LogMessageClassInitialized(self):
        return "    CLASS_INITIALIZED"
    
    @property
    def LogMessageFunctionCalled(self):
        return "      FUNCTION_CALLED"
    
    @property
    def LogMessageFunctionStatement(self):
        return "        FUNCTION_STATEMENT"

    @property
    def LogMessageFunctionReturned(self):
        return "        FUNCTION_RETURNED"
    
    @property
    def LogMessageFunctionParameters(self):
        return "        FUNCTION_PARAMETERS"

    @property
    def PathRedirectLogo(self):
        return "images\\RedirectLogo.ico"

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