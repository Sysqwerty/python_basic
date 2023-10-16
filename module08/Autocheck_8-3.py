from datetime import datetime


def get_str_date(date):
    datetime1 = date.split()[0]
    datetime1_date = datetime1.split('-')
    date1 = datetime(year=int(datetime1_date[0]), month=int(datetime1_date[1]), day=int(datetime1_date[2]))
    date_formatted = date1.strftime('%A %d %B %Y')
    print(date_formatted)

    return date_formatted

get_str_date('2021-05-27 17:08:34.149Z')