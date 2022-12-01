"""Dart"""
def main():
    """Dart"""
    num = int(input())
    score = 0
    for _ in range(num):
        point = input().split()
        pointx = abs(int(point[0]))
        pointy = abs(int(point[1]))
        rad = (pointx**2 + pointy**2)**0.5
        if rad <= 2:
            score += 5
        elif 2 < rad <= 4:
            score += 4
        elif 4 < rad <= 6:
            score += 3
        elif 6 < rad <= 8:
            score += 2
        elif 8 < rad <= 10:
            score += 1
        else:
            score += 0
    print(score)
main()
