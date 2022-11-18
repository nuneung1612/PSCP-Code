"""Roman"""
def main(val):
    """convert roman to integer"""
    roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 'IV':4, 'IX':9, 'XL':40, \
'XC':90, 'CD':400, 'CM':900}
    ans = 0
    idx = 0
    while idx < (len(val)):
        if idx+1 < len(val) and val[idx:idx+2] in roman:
            ans += roman[val[idx:idx+2]]
            idx += 2
        else:
            ans += roman[val[idx]]
            idx += 1
    print(ans)
main(input())
