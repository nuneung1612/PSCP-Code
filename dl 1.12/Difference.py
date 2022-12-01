"""Difference"""
import json
def main():
    """Difference"""
    list_a = json.loads(input())
    list_b = json.loads(input())
    set_a = set(list_a)
    set_b = set(list_b)
    uni = set_a.union(set_b)
    total = 0
    for i in sorted(uni):
        diff = abs(list_a.count(i)-list_b.count(i))
        if diff > 0:
            print(i, diff)
            total += 1
    if total == 0:
        print("ONAJI DAYO!")
main()
