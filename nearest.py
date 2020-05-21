
def nearest_square(num):
    """Return the nearest perfect square that is
    less than or equal to num."""
    root = 0
    while (root +1) ** 2 <= num:
        root += 1
    return root **2


def email_validator(email):
    if email.count('@') != 0 and email.count('.')!= 0:
        return True
    else:
        return False