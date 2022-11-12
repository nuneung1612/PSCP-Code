"""Coke V2"""
def main(old_price, cap_pro, dis_price, want):
    """Coke V2"""
    if cap_pro == 0:
        return print(old_price*want)

    if want == 0:
        return print(0)

    get = (want - 1)
    count = get // cap_pro
    left = get % cap_pro
    loop = (old_price*(cap_pro-1)) + dis_price

    total = old_price + (count * loop) + (left * old_price)
    print(total)
main(int(input()), int(input()), int(input()), int(input()))
