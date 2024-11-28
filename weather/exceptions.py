class FailedGeCoordinates(Exception):
    """The module cannot get coordinates"""

    def __str__(self):
        if self.code is not None:
            return f"The module cannot get coordinates [Error Code {self.code}]: {self.args[0]}"
        return self.args[0]
    
class FailedGetWeather(Exception):
    """The module cannot get weather"""
    
    def __str__(self):
        if self.code is not None:
            return f"The module cannot get weather [Error Code {self.code}]: {self.args[0]}"
        return self.args[0]