"""digit v2"""
def main():
    """digit v2"""
    num = input()
    if num.count("thousand") >= 1:
        print(4)
    elif num.count("hundred") >= 1 and num.count("thousand") < 1:
        print(3)
    elif (num.count("ty") >= 1 or num.count("teen") >= 1 or num.count("ten") >= 1 or \
num.count("eleven") or num.count("twelve")) \
and num.count("hundred") < 1 and num.count("thousand") < 1:
        print(2)
    else:
        print(1)
main()
