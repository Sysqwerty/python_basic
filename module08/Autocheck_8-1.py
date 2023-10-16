from datetime import datetime


def get_days_from_today(date):
    date_parts = date.split('-')
    date_now = datetime.now()
    date_data = datetime(year=int(date_parts[0]), month=int(date_parts[1]), day=int(date_parts[2]))
    difference:datetime = date_now - date_data
    print('date:', date)
    print('date_now:', date_now)
    print('difference:', difference.days)

    return difference.days

get_days_from_today('2020-10-09')