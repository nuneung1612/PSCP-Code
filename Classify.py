"""Classify"""
def main():
    """Classify"""
    text = input()
    stu_id = []
    senior = 0
    while text != "END":
        stu_id.append(text[:4])
        text = input()
    stu_set = sorted(set(stu_id))
    for i in stu_set:
        year = int(i[:2])
        if year != senior:
            print(year, int(i[2:4]), stu_id.count(i))
        else:
            print("--", int(i[2:4]), stu_id.count(i))
        senior = year
main()
