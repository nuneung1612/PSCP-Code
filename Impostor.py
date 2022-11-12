"""Impostor"""
import json
def main():
    """Impostor"""
    role = {}
    dead = {}
    alive = {}
    impostor = 0
    while True:
        txt = input()
        if txt == "Start":
            continue
        if txt == "End":
            break
        if txt[0] == "{":
            role.update(json.loads(txt))
        else:
            dead.update({txt:role[txt]})
    for i in role:
        if i not in dead:
            alive.update({i:role[i]})
    for i in alive:
        if role[i] == "Impostor":
            impostor += 1
    print(str(impostor)+" Impostor Remains", "***Alive***", sep="\n")
    for i in sorted(alive.items(), key=lambda item: item[0]):
        print(*i, sep=" : ")
    print("***Dead***")
    for i in sorted(dead.items(), key=lambda item: item[0]):
        print(*i, sep=" : ")
main()
