"""Compound Interest"""
def main():
    """Compound Interest"""
    num_k = int(input())
    num_r = float(input())
    num_t = int(input())
    for _ in range(num_t):
        num_k += num_k * num_r / 100
    print("%.2f" % num_k)
main()
