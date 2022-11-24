"""Phasmophobia"""
def main():
    """Phasmophobia"""
    ghost = {"EMF Level 5" : {'Banshee', 'Jinn', 'Oni', 'Phantom', 'Revenant', 'Shade'}\
            , "Ghost Writing" : {'Demon', 'Oni', 'Revenant', 'Shade', 'Spirit', 'Yurei'}\
            , "Fingerprints" : {'Banshee', 'Poltergeist', 'Revenant', 'Spirit', 'Wraith'}\
            , "Spirit Box" : {'Demon', 'Jinn', 'Mare', 'Oni', 'Poltergeist', 'Spirit', 'Wraith'}\
            , "Freezing Temperatures" : {'Banshee', 'Demon', 'Mare', 'Phantom', 'Wraith', 'Yurei'}\
            , "Ghost Orb" : {'Jinn', 'Mare', 'Phantom', 'Poltergeist', 'Shade', 'Yurei'}\
            , "No evidence" : {'Banshee', 'Jinn', 'Oni', 'Phantom', 'Revenant', 'Shade', 'Demon', \
            'Mare', 'Poltergeist', 'Spirit', 'Wraith', 'Yurei'}}

    set_a = ghost[input()]
    set_b = ghost[input()]
    set_c = ghost[input()]
    ans = list(set_a.intersection(set_b).intersection(set_c))
    ans.sort()
    if len(ans) == 0:
        print("Not yet discovered")
    else:
        print(*ans, sep="\n")
main()
