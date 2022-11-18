"""Hamming"""
def main():
    """Hamming"""
    text1 = input()
    text2 = input()
    val = 0
    for i in range(len(text1)):
        if text2[i] != text1[i]:
            val += 1
    print(val)
main()
