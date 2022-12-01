"""Discount"""
def main():
    """Discount"""
    book = []
    while True:
        price = input()
        if price == "ENTER":
            break
        else:
            book.append(int(price))
    book.sort()
    if len(book) <= 5:
        print(sum(book))
    elif 6 <= len(book) < 12:
        print(sum(book[1:]))
    elif 12 <= len(book) < 20:
        print(sum(book[2:]))
    elif 20 == len(book):
        print(sum(book[4:]))
    elif len(book) > 20:
        free = (len(book)-20)//5
        print(sum(book[4+free:]))
main()
