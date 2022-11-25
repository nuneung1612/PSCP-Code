"""is_prime_LARGER"""
def main():
    """is_prime_LARGER"""
    num = int(input())
    if num == 1:
        return print("False")
    for i in range(2, int(num**0.5)+1, 3):
        if num % i == 0:
            return print("False")
    return print("True")
main()
