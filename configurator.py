import configparser, os
from type import *
from constants import RedirectConstants

class RedirectConfiguration():
    def __init__(self) -> None:
        self.configuration = configparser.ConfigParser()
        self.read_configuration_file()

    def read_configuration_file(self):
        if self.configuration.read(
            filenames=RedirectConstants.ConfigurationFileName
        ):
            return True
        else:
            self.build_configuration()

    def build_configuration(self):
        self.configuration[RedirectConstants.ConfigurationSectionLogging] = {}
        self.configuration[RedirectConstants.ConfigurationSectionLogging][RedirectConstants.ConfigurationKeyLogLevel] = LogLevel.Error.name
        with open(RedirectConstants.ConfigurationFileName, 'w') as self.configuration_file:
            self.configuration.write(self.configuration_file)

    @property
    def LogLevel(self) -> LogLevel:
        self.section_logging = self.configuration[RedirectConstants.ConfigurationSectionLogging]
        try:
            return LogLevel[self.section_logging.get(RedirectConstants.ConfigurationKeyLogLevel, LogLevel.Error)]
        except KeyError:
            return LogLevel.Error

# con = RedirectConfiguration()
# print(con.LogLevel)