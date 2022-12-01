"""Resistor"""
def main():
    """Resistor"""
    line_12 = {'Black':0, 'Brown':1, 'Red':2, 'Orange':3, 'Yellow':4, \
'Green':5, 'Blue':6, 'Purple':7, 'Grey':8, 'White':9}
    line_3 = {'Black':1, 'Brown':10, 'Red':100, 'Orange':1000, 'Yellow':10000, \
'Green':100000, 'Blue':1000000, 'Purple':10000000, 'Gold':0.1, 'Silver':0.01}
    line_4 = {'Brown':1, 'Red':2, 'Green':0.5, 'Blue':0.25, 'Purple':0.10, \
'Grey':0.05, 'Gold':5, 'Silver':10}
    col1 = input()
    col2 = input()
    col3 = input()
    col4 = input()
    if (col2 not in line_12) or (col1 not in line_12) or (col3 not in line_3)\
 or (col4 not in line_4):
        print("Error")
    else:
        num = str(line_12[col1]) + str(line_12[col2])
        val = int(num)*line_3[col3]
        max_val = val + (val * (line_4[col4]/100))
        min_val = val - (val * (line_4[col4]/100))
        print("%.4f"%min_val)
        print("%.4f"%max_val)
main()
