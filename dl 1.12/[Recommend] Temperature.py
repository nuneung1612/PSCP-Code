"""temperature"""
def main():
    '''temperature'''
    temp = float(input())
    have = input().upper()
    want = input().upper()
    if have == "F":
        cel = (temp - 32) * 5/9
    elif have == "K":
        cel = temp - 273.15
    elif have == "R":
        cel = (temp * (5/9))- 273.15
    elif have == "C":
        cel = temp
    print("%.2f"%cal_temp(want, cel))
def cal_temp(want, cel):
    '''cel to fah'''
    if want == "F":
        result = cel * (9/5) +32
    elif want == "K":
        result = cel + 273.15
    elif want == "R":
        result = (cel + 273.15)*(9/5)
    elif want == "C":
        result = cel
    return result
main()
