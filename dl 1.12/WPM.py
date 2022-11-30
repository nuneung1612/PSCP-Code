"""WPM"""
def main():
    """WPM"""
    gen = input()
    wpm = int(input())
    result = ""
    if gen == "Kids":
        result = kids(wpm)
    else:
        result = adults(wpm)
    print(result)

def kids(word):
    """cal for kids"""
    res = ""
    if word < 11:
        res = "Very Slow"
    elif 11 <= word <= 20:
        res = "Slow"
    elif 21 <= word <= 30:
        res = "Average"
    elif 31 <= word <= 40:
        res = "Fast"
    else:
        res = "Very Fast"
    return res


def adults(word):
    """cal for adults"""
    res = ""
    if word < 26:
        res = "Very Slow"
    elif 26 <= word <= 35:
        res = "Slow/Beginner"
    elif 36 <= word <= 45:
        res = "Intermediate/Average"
    elif 46 <= word <= 65:
        res = "Fast/Advanced"
    elif 66 <= word <= 80:
        res = "Very Fast"
    else:
        res = "Insane"
    return res

main()
