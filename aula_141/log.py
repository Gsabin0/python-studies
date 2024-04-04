import os 

PATH_LOG_FILE = os.getcwd() + r'\log.txt'

class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o metodo log')

    def log_error(self, msg):
        return self._log(f'Eroor: {msg}')


    def log_success(self, msg):
        return self._log(f'Success: {msg}')


class LogFileMixin(Log):
    def _log(self, msg):
        with open(PATH_LOG_FILE, 'a') as arquivo:
            arquivo.write(msg)
            arquivo.write('\r\n')
        print(msg)
    
    
    

if __name__ == "__main__":
    l1 = LogFileMixin()
    l1.log_success('teste')
    l1.log_error('teste1')