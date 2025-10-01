import sys

class NetworkSecurityError(Exception):
    def __init__(self,error):
        self.error=error
        _,_,error_tb=sys.exc_info()
        
        self.lineno=error_tb.tb_lineno
        self.filename=error_tb.tb_frame.f_code.co_filename
        
    def __str__(self):
          return (f"u have error in file ({self.filename}) in line no ({self.lineno}) error message is({self.error})")
      
      
      
