# Solution to Project Euler problem 19.

# Preliminary thoughts:
# I don't have to consider the special case for leap years on centuries,
# because 2000 *is* divisible by 400. In this situation, leap years are just every 4 years.

# Straightforward solution: Loop through all years and months,
# and check if the current month is a Sunday.
# How do I know that a month begins with a Sunday?
# By taking the day count modulo 7, then comparing the remainder with an offset.

# In my original solution, I reset the day count after each year,
# so I also had to compute the weekday offset again for the next year.

# But this is unnecessary; we can just keep a running total of the day we're currently
# on, counting from the first day of 1901, rather than from the current year.


def run():
    monthLengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    first_sunday_count = 0
    weekdayOffset = 6  # Meaning: 1901 began with a Tuesday, so days with first_of_month % 7 == 6 are Sundays.

    # We begin the 'day' counter at 1, corresponding to the first day of January 1901.
    # Then we check if this day is a Sunday. Finally, we add the length of the current month
    # to this count, after which its value corresponds to the first day of the next month.
    day = 1

    for year in range(1901, 2000 + 1):
        # Loop through the months, then check if
        # the first of the month is a Sunday.
        for month in range(1, 12 + 1):
            if day % 7 == weekdayOffset:
                first_sunday_count += 1
            
            day += monthLengths[month - 1]
            
            # In leap years, extend February by one day.
            if year % 4 == 0 and month == 2: 
                day += 1

    return first_sunday_count


if __name__ == "__main__":
    print(f"The number of Sundays that fell on the first of a month in the time interval in question is: {run()}")
