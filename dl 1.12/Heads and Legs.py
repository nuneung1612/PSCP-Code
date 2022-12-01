"""Heads and Legs"""
def main():
    """Heads and Legs"""
    head = int(input())
    leg = int(input())
    rabbit = (leg - 2*head) // 2
    left = (leg - 2*head) % 2
    bird = head - rabbit
    if rabbit >= 0 and bird >= 0 and left == 0:
        print(rabbit, bird)
    else:
        print("Impossible")
main()
