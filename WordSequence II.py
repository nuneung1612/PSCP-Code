"""WordSequence II"""
def main(txt, new_txt):
    """WordSequence II"""
    max_val = max(len(txt), len(new_txt))
    for i in range(max_val+1):
        print(new_txt[:i]+txt[i:])
main(input(), input())
