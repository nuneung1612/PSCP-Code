"""Hamming"""
def main():
    """Hamming"""
    text1 = input()
    text2 = input()
    val = 0
    for i in range(len(min(text1, text2))): #จริงๆข้อความความยาวเท่ากัน ไม่ได้อ่าน inputspec ดีๆ ก็งี้
        if text2[i] != text1[i]:
            val += 1
    diff = abs(len(text1) - len(text2))
    val -= diff
    print(val)
main()
