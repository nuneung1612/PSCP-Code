"""BreakPassword"""
import hashlib
def main():
    """BreakPassword"""
    txt = input()
    for i in range(0, 100000):
        value = str("%05d"%i)
        hashing = hashlib.sha512(value.encode())
        if str(hashing.hexdigest()).upper() == txt:
            print("%05d"%i)
main()
