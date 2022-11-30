"""Pro"""
def main():
    """Pro"""
    come = int(input())
    pay = int(input())
    price = int(input())
    group = int(input())
    total = (group//come)*(pay*price)
    total += (group%come)*price
    print(total)
main()
