from type import *
import os
from datetime import datetime

class RedirectLogger():
    def __init__(
        self,
        controller,
        log_config: LogConfig
    ):
        self.controller = controller

        if log_config.log_file_name:
            self.log_file_name = log_config.log_file_name
        
        if log_config.log_file_location:
            self.log_file_location = log_config.log_file_location
            os.makedirs(self.log_file_location, exist_ok=True)

        if log_config.log_mode:
            self.log_mode = log_config.log_mode

        if log_config.log_level:
            self.log_level = log_config.log_level

    def log(
        self,
        log_message: str,
        log_caller: LogCaller,
        log_level: LogLevel,
    ):
        if log_level == self.log_level:

            if self.log_mode == LogMode.Append:
                self.log_file = open(self.log_file_location + '\\' + self.log_file_name, 'a')
            else:
                self.log_file = open(self.log_file_location + '\\' + self.log_file_name, 'w')

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
        date_time_string = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_line = date_time_string + ' - '
        log_line = log_line + log_caller + ' - '
        log_line = log_line + log_level.name + ' - '
        log_line = log_line + log_message
        return log_line