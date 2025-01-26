
class NoSuchUserException(Exception):
    """Was unable to find a user_info.json file in the current directory"""
    pass

class MissingSessionInfoException(Exception):
    """Was unable to find a session in sessions_info.json"""
    pass

class SessionsInfoMIssingException(Exception):
    """Was unable to find sessions_info.json file in the current directory"""
    pass

# TODO - Add more exceptions for specific cases