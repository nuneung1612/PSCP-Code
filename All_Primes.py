"""All_Primes"""
def main():
    """All_Primes"""
    num = int(input())
    val = 0
    for i in range(2, num+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            val += 1
    print(val)
main()
