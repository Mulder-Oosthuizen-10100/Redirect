from type import LogConfig, LogLevel

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

        if log_config.log_mode:
            self.log_mode = log_config.log_mode

        if log_config.log_level:
            self.log_level = log_config.log_level

        # if log_config.log_caller:
            # self.log_caller = log_config.log_caller

    def log(self,level: LogLevel, msg):
        if level == self.log_level:
            pass # log the message

    def debug(self, msg):
        self.log(level=LogLevel.Debug, msg=msg)