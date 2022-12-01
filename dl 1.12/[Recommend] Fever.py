"""Fever"""
def main():
    """Fever"""
    temp = float(input())
    if 36 <= temp < 38:
        print("No Fever")
    elif 38 <= temp < 39:
        print("Mild Fever")
    elif 39 <= temp < 40:
        print("High Fever")
    elif 40 <= temp:
        print("Very High Fever")
main()
