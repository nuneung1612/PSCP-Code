"""LetterFrequency"""
def main():
    """LetterFrequency"""
    text = input().lower()
    letter_dict = {}
    for i in text:
        if i.isalpha() and i in letter_dict:
            letter_dict[i] += 1
        elif i.isalpha() and i not in letter_dict:
            letter_dict[i] = 1
    print(max(letter_dict, key=letter_dict.get))
main()
