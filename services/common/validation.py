

def check_decimal(dec):
    try:
        Decimal(dec)
    except InvalidOperation:
        return False
    return True
def check_int(num):
    try:
        int(num)
    except ValueError:
        return False
    return True