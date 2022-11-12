"""Filter"""
import json
def main():
    """Filter"""
    text = json.loads(input())
    score = float(input())
    pass_list = []
    stu_sorted = sorted(text.keys())
    for i in stu_sorted:
        if text[i] >= score:
            pass_list.append("%s\t%.2f"%(i, text[i]))
    if len(pass_list) > 0:
        for i in pass_list:
            print(i)
    else:
        print("Nope")
main()
