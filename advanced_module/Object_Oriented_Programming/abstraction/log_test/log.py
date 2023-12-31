# Abstraction

from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'

class Log:
    def _log(self, msg):
        raise NotImplementedError('Implement the log method')

    def log_error(self, msg):
        return self._log(f'Error: {msg}')

    def log_success(self, msg):
        return self._log(f'Success: {msg}')

class LogFileMixin(Log):
    def _log(self, msg):
        # print(msg)
        msg_formatted = f'{msg} ({self.__class__.__name__})'
        print('Saving to the log:', msg_formatted)
        with open(LOG_FILE, 'a') as file:
            file.write(msg_formatted)
            file.write('\n')
        
class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')

if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_error('anything')
    lp.log_success("That's cool")
    lf = LogFileMixin()
    lf.log_error('anything')
    lf.log_success("That's cool")