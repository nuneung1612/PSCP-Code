"""3nPlus1"""
def main(num):
    """3nPlus1"""
    res_list = []
    while num != 1:
        if num % 2 != 0:
            num = 3*num + 1
            res_list.append(num)
        else:
            num = num// 2
            res_list.append(num)
    res_list.append(1)
    return len(res_list)

def realmain():
    """this is real main func"""
    len_list = []
    val = int(input())
    while val != 0:
        len_list.append(main(val))
        val = int(input())
    for i in len_list:
        print(i)
realmain()
