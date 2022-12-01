"""iPad Air"""
def main():
    """iPad Air"""
    col = input()
    rom = int(input())
    net = input()
    color_list = ["Space Gray", "Silver", "Green", "Rose Gold", "Sky Blue"]
    rom_list = [64, 256]
    net_list = ["Wi-Fi", "Wi-Fi + Cellular"]
    if (col not in color_list) or (rom not in rom_list) or (net not in net_list):
        print("Not Available")
    elif rom == 64 and net == "Wi-Fi":
        print(19900)
    elif rom == 256 and net == "Wi-Fi":
        print(24900)
    elif rom == 64 and net == "Wi-Fi + Cellular":
        print(24400)
    elif rom == 256 and net == "Wi-Fi + Cellular":
        print(29400)
main()
