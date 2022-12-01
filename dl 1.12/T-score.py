"""T-score"""
def main():
    """T-score"""
    stu = int(input())
    int(input())
    stu_score = []
    for _ in range(stu):
        score = int(input())
        stu_score.append(score)
    x_bar = sum(stu_score)/stu
    stu_power = []
    for i in stu_score:
        stu_power.append(i**2)
    stu_sd_top = (stu*(sum(stu_power)) - (sum(stu_score))**2)
    stu_sd_bottom = stu*(stu-1)
    stu_sd = (stu_sd_top/stu_sd_bottom)**0.5
    stu_z = []
    stu_t = []
    if stu_sd != 0:
        for i in stu_score:
            each_z = (i-x_bar)/stu_sd
            stu_z.append(each_z)
        for j in stu_z:
            each_t = 50 + (10*j)
            stu_t.append(each_t)
    else:
        for i in stu_score:
            each_t = 50
            stu_t.append(each_t)
    for i in stu_t:
        print("%.2f"%i)
main()
