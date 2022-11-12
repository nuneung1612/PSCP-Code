"""CoPrime V1"""
def main(num_1, num_2):
    """CoPrime V1"""
    prime = 0
    for i in range(1, min(num_1, num_2) + 1):
        if num_1 % i == 0 and num_2 % i == 0:
            prime = i
    if prime == 1:
        print("YES"+"\n"+str(prime))
    else:
        print("NO"+"\n"+str(prime))
main(int(input()), int(input()))
