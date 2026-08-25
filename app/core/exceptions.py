class LibraryException(Exception):
    def __init__(self, message: str):
        self.message = message


class BookNotFoundError(LibraryException):
    pass


class UserNotFoundError(LibraryException):
    pass


class BookAlreadyReservedError(LibraryException):
    pass


class BookAlreadyCheckedOutError(LibraryException):
    pass


class BookNotAvailableError(LibraryException):
    pass


class DuplicateISBNError(LibraryException):
    pass


class DuplicateEmailError(LibraryException):
    pass
