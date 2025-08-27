from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass

class ConsoleLogger(Logger):

    def log(self, message):
        print(f"Log: {message}")

class FileLogger:

    def write_log(self, msg):
        print(f"FileLogger: {msg}")

class FileLoggerAdapter(Logger):
    def __init__(self):
        self._file_logger = FileLogger()

    def log(self, message):
        self._file_logger.write_log(message)

if __name__ == "__main__":
    loggers = [ConsoleLogger(), FileLoggerAdapter()]
    message = input("Enter message to log: ")
    
    for logger in loggers:
        logger.log(message)
