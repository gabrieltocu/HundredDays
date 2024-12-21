def is_leap_year(year):
    """Helper function for is_leap_year"""
    if year % 4 != 0:
        return False
    elif year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0:
        return False

print(is_leap_year(1900))