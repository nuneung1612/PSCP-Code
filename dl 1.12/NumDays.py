"""NumDays"""
def main():
    """NumDays"""
    day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day1 = int(input())
    month1 = int(input())
    day2 = int(input())
    month2 = int(input())
    allday1 = 0
    allday2 = 0
    if day_list[month1-1] < day1 or day_list[month2-1] < day2:
        print("Impossible")
    else:
        for i in range(1, month1):
            allday1 += day_list[i-1]
        for j in range(1, month2):
            allday2 += day_list[j-1]
        ans = abs((allday1+day1) - (allday2+day2))
        print(ans)
main()
