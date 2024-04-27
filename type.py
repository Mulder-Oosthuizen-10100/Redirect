from dataclasses import dataclass
from enum import Enum

class LogMode(Enum):
    Rewrite = 0
    Append = 1

class LogLevel(Enum):
    Debug = 0
    Info = 1
    Warn = 2
    Error = 3

class LogCaller(Enum):
    Controller = 0
    View = 1
    Model = 2
    Validator = 3

@dataclass
class LogConfig:
    log_file_location: str
    log_file_name: str
    log_mode: LogMode
    log_level: LogLevel