"""MasterMind"""
def main():
    """MasterMind"""
    answer = input()
    guess = input()
    black = 0
    white = 0
    for i in range(4):
        if answer[i] == guess[i]:
            black = black + 1
    for j in set(answer):
        white = white + min(answer.count(j), guess.count(j))
    white = white - black
    blank = 4 - black - white
    print('B'*black+'W'*white+'O'*blank)
main()
