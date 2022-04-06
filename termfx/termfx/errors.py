class TermfxException(Exception):
    def __init__(self, message):
        super().__init__(message)

class RegisteredVariable(TermfxException):
    pass

class RegisteredFunction(TermfxException):
    pass
