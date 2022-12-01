"""Majority"""
def main():
    """Majority"""
    candi = int(input())
    voter = int(input())
    vote_dict = {}
    candi = candi
    for _ in range(voter):
        num = str(input())
        if num not in vote_dict:
            vote_dict[num] = 1
        else:
            vote_dict[num] += 1
    most = max(vote_dict, key=vote_dict.get)
    if float(vote_dict[most]) > voter/2:
        print(most, vote_dict[most])
    else:
        print(0, vote_dict[most])

main()
