"""[Recommend] Tax"""
def main():
    """[Recommend] Tax"""
    year = int(input())
    ccc = int(input())
    total = 0
    if ccc <= 600:
        total = ccc * 0.5
    elif 600 < ccc <= 1800:
        total = 300 + ((ccc-600)*1.50)
    elif 1800 < ccc:
        total = 300 + 1800 + ((ccc-1800)*4)
    discount = dis(year)
    print("%.2f"%(total - (total*discount)))

def dis(num):
    """discount"""
    ddd = 0
    if num < 6:
        ddd = 0
    elif num == 6:
        ddd = 0.1
    elif num == 7:
        ddd = 0.2
    elif num == 8:
        ddd = 0.3
    elif num == 9:
        ddd = 0.4
    else:
        ddd = 0.5
    return ddd

main()
