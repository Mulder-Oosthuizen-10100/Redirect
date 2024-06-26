import os
from type import *
from datetime import datetime
from inspect import *

class RedirectLogger():
    def __init__(
        self,
        log_config: LogConfig,
    ):
        if log_config.log_file_name:
            self.log_file_name = log_config.log_file_name
        
        if log_config.log_file_location:
            self.log_file_location = log_config.log_file_location
            os.makedirs(self.log_file_location, exist_ok=True)

        if log_config.log_level:
            self.log_level = log_config.log_level

    def get_line_number(
        self,
        line_number: int,
        minus_lines: int,
    ):
        line_number = line_number - minus_lines
        return self._format_log_line_number(
            line_number=line_number,
        )
    
    def get_direct_line_number(
        self,
        direct_line_number: int,
    ):
        return self._format_log_line_number(
            line_number=direct_line_number,
        )
    
    def _format_log_line_number(
        self,
        line_number: int,
    ):
        return ('{: <4}'.format(str(line_number)))

    def log(
        self,
        log_message: str,
        log_caller: LogCaller,
        log_level: LogLevel,
    ):
        if (log_level.value <= self.log_level.value) and (log_level.value >= 0):
            self.log_file = open(self.log_file_location + '\\' + self.log_file_name, 'a')
            if self.log_file:
                log_line = self.get_log_file_log_line(
                    log_message=log_message,
                    log_caller=log_caller,
                    log_level=log_level,
                )
                self.log_file.write(log_line)
                self.log_file.close()

    def get_log_file_log_line(
        self,
        log_message: str,
        log_caller: LogCaller,
        log_level: LogLevel,
    ) -> str:
        date_time_string = datetime.now().strftime("%T.%f")[:-3]
        log_caller_string = (log_caller.name[:3]) if len(log_caller.name) > 3 else log_caller.name
        log_level_string = ('{: <5}'.format(log_level.name))

        log_line = date_time_string + ' - '
        log_line = log_line + log_caller_string + ' - '
        log_line = log_line + log_level_string + ' - '
        log_line = log_line + log_message + '\n'
        return log_line
    
    @classmethod
    def get_log_config(self) -> LogConfig:
        return LogConfig(
            log_file_location = self.get_log_file_location(),
            log_file_name = self.get_log_file_name(),
            log_level = LogLevel.Debug,
        )

    @classmethod
    def get_log_file_name(self) -> str:
        date_time_string = datetime.now().strftime("%d-%m-%Y")
        log_file_name = date_time_string + ".log"
        return log_file_name
    
    @classmethod
    def get_log_file_location(self) -> str:
        year_string = datetime.now().strftime("%Y") + "\\"
        month_string = datetime.now().strftime("%B")
        log_file_location = os.getcwd() + "\\" + "log\\" + year_string + month_string
        return log_file_location