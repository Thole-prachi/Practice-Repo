def is_leap (year):
    if year % 4 == 0:
        print ("This is leap year")
    elif year % 100 != 0:
        print ("This is not leap year")
    elif year % 400 == 0:
        print ("This is leap year")
    else:
        print("not sure which year it is?")

is_leap(1989)