"""Sort"""
def main():
    """Sort"""
    num_list = []
    num = input()
    while num != "END":
        num_list.append(int(num))
        num = input()
    swap = True
    while swap:
        swap = False
        for i in range(len(num_list)-1):
            if num_list[i] > num_list[i+1]:
                num_list[i], num_list[i+1] = num_list[i+1], num_list[i]
                swap = True
    for i in num_list:
        print(i)
main()
