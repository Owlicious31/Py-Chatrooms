
class NoSuchUserException(Exception):
    """Was unable to find user in the db"""
    pass

class MissingSessionInfoException(Exception):
    """Was unable to find some info on a session """
    pass

class NonExistentSessionException(Exception):
    """Was unable to find a session for the provided invite code"""
    pass

class SessionParsingException(Exception):
    """Was unable to read session info and utilize it"""
    pass

class InvalidCredentialsException(Exception):
    """Provided user credentials did not match thos stored in the db"""
    pass
# TODO - Add more exceptions for specific cases