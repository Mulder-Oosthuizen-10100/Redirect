class classproperty(object):
    def __init__(self, fget):
        self.fget = fget
    def __get__(self, owner_self, owner_class):
        return self.fget(owner_class)

class RedirectConstants:

# LOGGING CONSTANTS
    @classproperty
    def LogMessageApplicationStarting(self):
        return "APPLICATION_STARTING"

    @classproperty
    def LogMessageApplicationGUIBuilt(self):
        return "APPLICATION_GUI_BUILT"

    @classproperty
    def LogMessageApplicationDataRetrieved(self):
        return "APPLICATION_DATA_RETRIEVED"

    @classproperty
    def LogMessageApplicationClosing(self):
        return "APPLICATION_CLOSING"

    @classproperty
    def LogMessageUserInteractionStart(self):
        return "USER_INTERACTION_START"

    @classproperty
    def LogMessageUserInteractionEnd(self):
        return "USER_INTERACTION_END"

    @classproperty
    def LogMessageClassInitializing(self):
        return " CLASS_INITIALIZING    "

    @classproperty
    def LogMessageClassInitialized(self):
        return " CLASS_INITIALIZED     "

    @classproperty
    def LogMessageFunctionCalled(self):
        return "  FUNCTION_CALLED      "

    @classproperty
    def LogMessageFunctionStatement(self):
        return "   FUNCTION_STATEMENT  "

    @classproperty
    def LogMessageFunctionReturned(self):
        return "   FUNCTION_RETURNED   "

    @classproperty
    def LogMessageFunctionParameters(self):
        return "   FUNCTION_PARAMETERS "

    @classproperty
    def LogMessageForLoop(self):
        return "   FOR_LOOP            "

# VIEW CONSTANTS
    @classproperty
    def AppearanceModeSystem(self) -> str:
        return 'System'

    @classproperty
    def DefaultColorTheme(self) -> str:
        return 'dark-blue'
    
    @classproperty
    def ApplicationTitle(self) -> str:
        '''Redirect 404 URLs'''
        return 'Redirect 404 URLs'

    @classproperty
    def ApplicationHeadingText(self) -> str:
        '''Redirect 404 URLs'''
        return 'Redirect 404 URLs'

    @classproperty
    def ApplicationLoadingText(self) -> str:
        '''Shops Loading'''
        return 'Shops Loading'

    @classproperty
    def ApplicationGeometry(self) -> str:
        '''1000x600'''
        return '1000x600'

    @classproperty
    def TextButtonGenerate(self) -> str:
        '''Generate CSV File'''
        return 'Generate CSV File'

    @classproperty
    def MessageWindowTitle(self) -> str:
        '''You have a Message'''
        return 'You have a Message'

    @classproperty
    def TextFontFamily(self) -> str:
        return 'JetBrains Mono'

    @classproperty
    def LargeTextSize(self) -> int:
        return 40

    @classproperty
    def MediumTextSize(self) -> int:
        return 18

    @classproperty
    def SmallTextSize(self) -> int:
        return 14

    @classproperty
    def KeyWebsite(self) -> str:
        return 'WEBSITE'

    @classproperty
    def KeyRemovePart(self) -> str:
        return 'REMOVE_PART'

    @classproperty
    def KeyKeyword(self) -> str:
        return 'KEYWORD'

    @classproperty
    def KeyURL(self) -> str:
        return 'URL'
    
    @classproperty
    def KeyDefault(self) -> str:
        return 'DEFAULT'

    @classproperty
    def ImageOpenDialog(self) -> str:
        '''.\\images\\folder_location.png'''
        return '.\\images\\folder_location.png'

    @classproperty
    def ImageApplicationIcon(self) -> str:
        '''images\\RedirectLogo.ico'''
        return 'images\\RedirectLogo.ico'
    
    @classproperty
    def TextMessageWindowButton(self) -> str:
        '''OK'''
        return 'OK'

    # SOURCE FILE
    @classproperty
    def LabelSourceFileLocationText(self) -> str:
        '''Source File Location'''
        return 'Source File Location'

    @classproperty
    def DefaultSourceFileExtension(self) -> str:
        '''.txt'''
        return '.txt'

    @classproperty
    def ExtensionTypeSourceFile(self) -> str:
        '''Text Files'''
        return 'Text Files'

    # REDIRECT FOLDER
    @classproperty
    def LabelRedirectFolderLocationText(self) -> str:
        '''Redirect Folder Location'''
        return 'Redirect Folder Location'

    @classproperty
    def PathRedirectLogo(self):
        return "images\\RedirectLogo.ico"

    @classproperty
    def TitleSourceFileDialog(self):
        return "Select the Source File that contains the URLs with 404 errors."

    @classproperty
    def TitleDestinationFolderDialog(self):
        return "Select the Destination Folder where the redirect CSV file will be placed."

# MODEL CONSTANTS
    @classproperty
    def GoogleSheetDocumentName(self):
        '''WEBSITE_DATA'''
        return 'WEBSITE_DATA'
    
    @classproperty
    def GoogleSheetTabWebsites(self):
        '''WEBSITES'''
        return 'WEBSITES'

    @classproperty
    def GoogleSheetTabKeywords(self):
        '''KEYWORDS'''
        return 'KEYWORDS'
    
    @classproperty
    def GoogleSheetTabRemoveParts(self):
        '''REMOVE_PARTS'''
        return 'REMOVE_PARTS'

    @classproperty
    def DefaultDirectory(self) -> str:
        '''~\\Documents'''
        return '~\\Documents'
    
    @classproperty
    def ResultMustUpdateRedirectFolder(self) -> bool:
        '''TRUE'''
        return True
    
    @classproperty
    def RedirectSuccessMessage(self) -> str:
        '''Successfully Redirected the Source File!'''
        return 'Successfully Redirected the Source File!'
    
    @classproperty
    def ModelExceptionMessageRedirectProcess(self) -> str:
        '''ERROR: An Error occurred during the redirect process!\nPlease see the log file for more detail.'''
        return 'ERROR: An Error occurred during the redirect process!\nPlease see the log file for more detail.'

    @classproperty
    def ModelExceptionMessageProcessLine(self) -> str:
        '''ERROR: An error occurred trying to process a line in the source file!\nPlease see the log file for more detail.'''
        return 'ERROR: An error occurred trying to process a line in the source file!\nPlease see the log file for more detail.'

    @classproperty
    def OutputFileNameFormat(self) -> str:
        '''%Y_%m_%d__%H_%M_%S'''
        return '%Y_%m_%d__%H_%M_%S'

    @classproperty
    def RedirectOutputFileName(self) -> str:
        '''redirect_'''
        return 'redirect_'

    @classproperty
    def UnmatchedRedirectOutputFileName(self) -> str:
        '''unmatched_urls_'''
        return 'unmatched_urls_'
    
# VALIDATOR CONSTANTS
    @classproperty
    def ValidateErrorMessageNoRemoveParts(self) -> str:
        '''Google Sheet does not contain any remove parts!'''
        return 'Google Sheet does not contain any remove parts!'

    @classproperty
    def ValidateErrorMessageNoKeyWords(self) -> str:
        '''Google Sheet does not contain any keywords!'''
        return 'Google Sheet does not contain any keywords!'
    
    @classproperty
    def ValidateErrorMessageNoWebsites(self) -> str:
        '''Google Sheet does not contain any websites!'''
        return 'Google Sheet does not contain any websites!'    

    @classproperty
    def ValidateErrorMessageNoShop(self) -> str:
        '''Please select a shop name!'''
        return 'Please select a shop name!'

    @classproperty
    def ValidateErrorMessageSourceFileEmpty(self) -> str:
        '''The selected source file is empty!'''
        return 'The selected source file is empty!'

    @classproperty
    def ValidateErrorMessageSourceFileNotAFile(self) -> str:
        '''The selected source file is not a file!'''
        return 'The selected source file is not a file!'

    @classproperty
    def ValidateErrorMessageSourceFileNotSelected(self) -> str:
        '''Please select a source file!'''
        return 'Please select a source file!'

    @classproperty
    def ValidateExceptionMessageSourceFileNotExist(self) -> str:
        '''Source File: DOES NOT EXIST\nPlease see the log file for more detail.'''
        return 'Source File: DOES NOT EXIST\nPlease see the log file for more detail.'

    @classproperty
    def ValidateExceptionMessage(self) -> str:
        '''An unknown exception occurred!\nPlease see the log file for more detail.'''
        return 'An unknown exception occurred!\nPlease see the log file for more detail.'

# CONFIG CONSTANTS
    @classproperty
    def EmptyString(self) -> str:
        return ""

    @classproperty
    def ConfigurationFileName(self) -> str:
        return "Redirect.ini"

    @classproperty
    def ConfigurationSectionLogging(self) -> str:
        return "LOGGING"

    @classproperty
    def ConfigurationKeyLogLevel(self) -> str:
        return "LogLevel"
