def nextDay(year, month, day):
    """ Warning: this version incorrectly
        assumes all months have 30 days!"""
    if day < 30:
        return year, month, day + 1
    else:
        if month < 12 :
            return year, month + 1, 1
        else:
            return year + 1 , 1 , 1
print nextDay (1996,12,21)
print nextDay (2001,12,1)
print('')

def dateIsBefore(year1, month1, day1, year2, month2 ,day2):
    """Returns True if year1-month1-day1 is before
       year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        return True
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False
print dateIsBefore(2013,2,10,2012,2,1)
print dateIsBefore(2001,12,1,2020,12,1)

print('')

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days
print daysBetweenDates(2011,2,12,2012,2,12)
print daysBetweenDates(2001,12,1,2020,12,1)

print('')

print 365.25 * 18 + 90
