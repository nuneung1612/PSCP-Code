"""ISBN"""
def main():
    """ISBN"""
    isbn = input().replace("-", "")
    test = 0
    koon = 10
    for i in isbn:
        test += int(i) * koon
        koon -= 1
        if koon < 2:
            break
    val = (-test) % 11
    if str(val) == isbn[9]:
        print("Yes")
    elif val == 10 and isbn[9] == "X":
        print("Yes")
    else:
        print("No", end=" ")
        if val < 10:
            print(val)
        else:
            print("X")
main()
