
class NoSuchUserException(Exception):
    """Was unable to find a user_info.json file in the current directory"""
    pass

class MissingInfoException(Exception):
    """Was unable to find some info in sessions_info.json"""
    pass

class SessionsInfoMissingException(Exception):
    """sessions_info.json is either not in the main directory or empty"""
    pass

class NonExistentSessionException(Exception):
    """Was unable to find a session from the provided index"""
    pass

class InvalidMessageTypeException(Exception):
    """An invalid message type was provided i.e not 'str'"""
    pass
# TODO - Add more exceptions for specific cases