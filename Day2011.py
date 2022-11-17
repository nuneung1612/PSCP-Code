""" Day2011 """
def main(day, month):
    """Day 2011"""
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dayofyear = sum(days[:month-1]) + day
    daynum = dayofyear%7
    daynames = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
    return print(daynames[daynum])

main(int(input()), int(input()))
