'''
Date Created: 12/18/2024 (MM/DD/YYYY)

Calendar program
SOURCE: CODEFINITY (AD)

'''

import calendar

def month_calendar():
    year = int(input("Enter a year: "))
    month = int(input("Enter a month (1-12): "))

    cal = calendar.TextCalendar(calendar.SUNDAY)
    month_cal = cal.formatmonth(year, month)

    print(f"\n\n{month_cal}")


month_calendar()
