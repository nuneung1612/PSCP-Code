"""Milk v2"""
def main():
    """Milk v2"""
    price = float(input())
    pro_cov = int(input())
    cov_exchange = int(input())
    pro_bot = int(input())
    bot_exchange = int(input())
    money = float(input())
    buy = money // price
    total = cov = bot = buy
    while cov >= pro_cov or bot >= pro_bot:
        from_cov = (cov//pro_cov)*cov_exchange
        from_bot = (bot//pro_bot)*bot_exchange
        new = from_bot + from_cov
        cov = new + cov%pro_cov
        bot = new + bot%pro_bot
        total += new
    print(int(total))
main()
