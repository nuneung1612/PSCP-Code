"""Coupon"""
def main():
    """Coupon"""
    price = float(input())
    dis1, less1 = input().split()
    dis2, less2 = input().split()
    total1 = price
    total2 = price
    if price >= float(less1) and price >= float(less2):
        total1 = price - float(dis1)
        total2 = price - (price*(float(dis2)/100))
    elif price >= float(less1) and not price >= float(less2):
        total1 = price - float(dis1)
    elif price >= float(less2) and not price >= float(less1):
        total2 = price - (price*(float(dis2)/100))


    if total1 == price == total2:
        print("Nope")
    elif total1 == total2 and float(less1) < float(less2):
        print(("1 %.1f"%total1))
    elif total1 == total2 and float(less2) < float(less1):
        print("2 %.1f"%total2)
    elif total1 <= total2:
        print("1 %.1f"%total1)
    else:
        print("2 %.1f"%total2)

main()
