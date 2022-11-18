"""SMS"""
def main():
    """SMS"""
    res3 = {2:["A", "B", "C"], 3:["D", "E", "F"], 4:["G", "H", "I"], 5:["J", "K", "L"], \
6:["M", "N", "O"], 8:["T", "U", "V"]}
    res4 = {7:["P", "Q", "R", "S"], 9:["W", "X", "Y", "Z"]}
    word = []
    turn = int(input())
    for _ in range(turn):
        butt = int(input())
        time = int(input())
        if butt in res3:
            word.append(res3.get(butt)[time%3-1])
        elif butt in res4:
            word.append(res4.get(butt)[time%4-1])
        else:
            del word[-(time):]
    print("".join(word) if len(word) > 0 else "null")
main()
