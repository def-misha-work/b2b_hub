def check_number(number):
    if not number.isdigit():
        return False
    if len(number) != 10:
        return False
    return True
