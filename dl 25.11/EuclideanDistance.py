"""EuclideanDistance"""
def main():
    """EuclideanDistance"""
    ans = 0
    pt_list = []
    count = int(input())
    for _ in range(count):
        txt = input().split()
        numx, numy = int(txt[0]), int(txt[1])
        pt_list.append([numx, numy])
    for i in range(0, count-1):
        dis = ((pt_list[i][0] - pt_list[i+1][0])**2 + (pt_list[i][1] - pt_list[i+1][1])**2)**0.5
        ans += dis
    print("%.2f"%ans)
main()
