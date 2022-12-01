"""OTP"""
def main():
    """OTP"""
    check_list = []
    while True:
        num = input()
        num_count = []
        if num == '0':
            break
        else:
            for i in range(10):
                num_count.append(num.count(str(i)))
            if len(num) == 4 and num_count.count(2) == 1:
                check_list.append("Valid")
            elif len(num) == 6 and (num_count.count(2) == 2 or num_count.count(3) == 1):
                check_list.append("Valid")
            elif len(num) == 8 and (num_count.count(2) == 3 or num_count.count(3) == 2):
                check_list.append("Valid")
            else:
                check_list.append("Invalid")
    for i in check_list:
        print(i)
main()
