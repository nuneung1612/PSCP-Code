"""RunGame"""
def main():
    """RunGame"""
    item = input().split()
    cal = 0
    for i in range(len(item)):
        if i == 0:
            cal += abs(int(item[i]))
        else:
            cal += abs(int(item[i]) - int(item[i-1]))
    print(cal)
main()
