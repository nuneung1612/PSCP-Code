"""ClockHands"""
def main():
    """ ClockHands """
    hour = int(input())
    sec = int(input())
    hour = ((hour*5) + (sec/12))%60
    if sec <= hour < sec+1:
        print("True")
    else:
        print("False")
main()
