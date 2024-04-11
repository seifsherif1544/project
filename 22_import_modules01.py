# import datetime
# currentYear = datetime.date.today().year
from datetime import date
currentYear = date.today().year

from m_reading import readInteger
birthYear = readInteger("Please, enter your birth year: ", 2000, currentYear)

age = currentYear - birthYear
print(age)
