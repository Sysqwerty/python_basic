from calendar import monthrange


def get_days_in_month(month:int, year:int):
    days_in_month = monthrange(year, month)[1]
    print(days_in_month)

    return days_in_month

get_days_in_month(2, 2021)