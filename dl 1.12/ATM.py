"""ATM"""
def main():
    """ATM"""
    money = int(input())
    while True:
        pro = input()
        if pro == "END":
            break
        tup = pro.split()
        if tup[0] == "D":
            money += int(tup[1])
        else:
            money -= int(tup[1])
            if money < 0:
                money = 0
    print(money)
main()
