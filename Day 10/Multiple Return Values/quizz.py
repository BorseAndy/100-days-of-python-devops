def is_leap_year(year):
    """" It will return True if the given year is leap year """
    if not year % 4:
        if not year % 100:
            if not year % 400:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


print(is_leap_year(2000))