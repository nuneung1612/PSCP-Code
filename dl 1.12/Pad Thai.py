"""Pad Thai"""
def main():
    """Pad Thai"""
    ingre = ["Pad Thai Sauce", "Tofu", "Pickle Turnip", "Shrimp", "Bean Sprouts", \
"Noodle", "Chives", "Lime", "Egg", "Oil", "Peanuts"]
    taste = ["Sweet", "Salty", "Sour"]
    have = set()
    fla = set()
    false_ingre = []
    bad_taste = []
    txt = input()
    while txt != "Cook":
        if txt in ingre:
            have.add(txt)
        else:
            false_ingre.append(ingre)
        txt = input()
    taste_txt = input()
    while taste_txt != "End":
        if taste_txt in taste:
            fla.add(taste_txt)
        else:
            bad_taste.append(taste_txt)
        taste_txt = input()
    if len(false_ingre) > 0:
        print("This is not Pad Thai!!!")
    elif len(have) == 11 and len(fla) == 3 and len(bad_taste) == 0:
        print("Delicious!")
    elif len(have) < 11:
        print("This is bad!")
    elif len(have) == 11 and (len(bad_taste) > 0 or len(fla) < 3):
        print("Not Bad...")
main()
