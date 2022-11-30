"""Area"""
def main():
    """Area"""
    line = int(input())
    shadow = 0
    for _ in range(line):
        text = input()
        for i in text:
            if not i.isspace():
                shadow += 1
    print(shadow)
main()
