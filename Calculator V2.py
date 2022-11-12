"""Calculator V2"""
def main():
    """Calculator V2"""
    num = int(input())
    length = len(str(num))
    count_1 = 1
    count_9 = 9
    total_tap = 0
    if num == 1:
        return print(1)
    for i in range(1, length):
        amount = (count_9 - count_1) + 1
        total_tap += amount*i
        count_1 = int(str(count_1)+"0")
        count_9 = int(str(count_9)+"9")
    plus = (num - count_1 + 1) * length
    print(total_tap + plus + num)
main()
