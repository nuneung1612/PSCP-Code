"""HorizontalHistogram"""
def main():
    """HorizontalHistogram"""
    text = input()
    letter = {}
    for i in text:
        if i in letter:
            letter[i] += 1
        else:
            letter[i] = 1
    sorted_letter = sorted(letter.keys(), key=str.swapcase)
    for i in sorted_letter:
        freq = ""
        print(i, ": ", end="")
        for j in range(1, letter[i]+1):
            if j % 5 == 0:
                freq += "-|"
            else:
                freq += "-"
        print(freq.rstrip("|"))
main()
