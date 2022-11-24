"""CoinChangev1"""
def main():
    """CoinChangev1"""
    money = int(input())
    coin_25, left = divmod(money, 25)
    coin_10, left = divmod(left, 10)
    coin_5, coin_1 = divmod(left, 5)
    print(coin_25 + coin_10 + coin_5 + coin_1)
main()
