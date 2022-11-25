"""Semi prime"""
def prime(num):
    """check prime"""
    if num == 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def main():
    """Semi prime"""
    num = int(input())
    prime_list = []
    ans = 0
    for i in range(1, num+1):
        if prime(i) == True:
            prime_list.append(i)

    for i in range(len(prime_list)):
        prime1 = prime_list[i]
        for prime2 in prime_list[i:]:
            if prime1*prime2 <= num:
                ans += 1
    print(ans)

main()
