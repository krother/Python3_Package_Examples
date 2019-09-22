
import datetime

# format dates:
date = datetime.date(2015, 12, 24)
print(date.strftime("%d.%m.%Y"))

# convert dates to integer numbers:

date = datetime.date(2015, 12, 24)
print(date.toordinal())

# and back:
datetime.date.fromordinal(7)
