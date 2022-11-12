"""BreachTheDoor"""
def main():
    """BreachTheDoor"""
    text = input()
    cut_text = text.split()
    new_cut = []
    #word = ""
    #print(cut_text)
    for i in cut_text:
        word = ""
        for j in i:
            if j.isalpha():
                word += j
        new_cut.append(word)
    #print(new_cut)
    for i in new_cut:
        if len(i) > 6:
            print(i, end=" ")

main()
