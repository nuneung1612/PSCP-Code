"""Gram_v1"""
def main():
    """Gram_v1"""
    text = input()
    txt_list = []
    word = ""
    num = 0
    for i in range(len(text)-1):
        txt_list.append(text[i]+text[i+1])
    #print(txt_list)
    for i in txt_list:
        if txt_list.count(i) > num:
            word = i
            num = txt_list.count(i)
    print(word+"\n"+str(num))
main()
