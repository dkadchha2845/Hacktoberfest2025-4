import calendar
print()
year = int(input("Enter Year (e.g = 2023): "))
month = int(input("Enter Month (1 to 12): "))
calender  = calendar.month(year, month)
print(f"Calendar For {calendar.month_name[month]} {year}:\n")
print(calender)
print()
