"""Colors"""
def main():
    """Colors"""
    prime = ['Red', 'Yellow', 'Blue']
    col1 = input()
    col2 = input()
    if (col1 in prime) and (col2 in prime):
        if (col1 == 'Red' or col2 == 'Red') and (col1 == 'Yellow' or col2 == 'Yellow'):
            print('Orange')
        elif (col1 == 'Red' or col2 == 'Red') and (col1 == 'Blue' or col2 == 'Blue'):
            print('Violet')
        elif (col1 == 'Blue' or col2 == 'Blue') and (col1 == 'Yellow' or col2 == 'Yellow'):
            print('Green')
        elif col1 == col2:
            print(col1)
    else:
        print('Error')
main()
