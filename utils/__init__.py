import string
from random import choices


def generate_access_code():
    """
    Generate access code
    This method is used to generate an access code.
    """
    return ''.join(choices(string.ascii_uppercase + string.digits, k=10))
