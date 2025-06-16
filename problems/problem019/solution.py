def is_leap_year(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def count_sundays_on_first(start_year: int = 1901, end_year: int = 2000) -> int:
    month_days = [31, 28, 31, 30, 31, 30,
                  31, 31, 30, 31, 30, 31]

    first_day_of_month = 1  # 0=Monday, 6=Sunday; 1 Jan 1901 was a Tuesday
    sunday_count = 0

    for year in range(start_year, end_year + 1):
        for month in range(12):
            if first_day_of_month == 6:  # Sunday
                sunday_count += 1

            days = month_days[month]
            if month == 1 and is_leap_year(year):
                days += 1

            first_day_of_month = (first_day_of_month + days) % 7

    return sunday_count
