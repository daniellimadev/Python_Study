# Creating dates with datetime module
# datetime(year, month, day)
# datetime(year, month, day, hours, minutes, seconds)
# datetime.strptime('DATE', 'FORMAT')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# For timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Installing pytz
# pip install pytz types-pytz
from datetime import datetime

data_str_data = '2024/01/20 07:49:23'
data_str_data = '01/20/2024'
data_str_fmt = '%d/%m/%Y'

# date = datetime(2022, 4, 20, 7, 49, 23)
data = datetime.strptime(data_str_data, data_str_fmt)
print(date)