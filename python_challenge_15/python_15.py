import calendar
from datetime import datetime

all_possible_years = range(1006,1996,10)
list_of_all_statisfact = []

for possible_year in all_possible_years:
    that_day = datetime(possible_year,1,26)
    if calendar.isleap(possible_year)\
         and datetime.isoweekday(that_day) == 1:
        list_of_all_statisfact.append(possible_year)

need_to_buy_flower = datetime(list_of_all_statisfact[-2],1,27)

print(need_to_buy_flower)

#mozart

