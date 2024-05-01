from dataclasses import dataclass
from enum import Enum

class LogLevel(Enum):
    Nothing = -1
    Error = 0
    Warn = 1
    Info = 2
    Debug = 3

class LogCaller(Enum):
    Controller = 0
    View = 1
    Model = 2
    Validator = 3

@dataclass
class LogConfig:
    log_file_location: str
    log_file_name: str
    log_level: LogLevel