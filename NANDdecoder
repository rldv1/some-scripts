def decodenand(identifier):
    brands = {
        0x01: "Spansion",
        0x04: "Fujitsu",
        0x07: "Renesas",
        0x20: "STMicro",
        0x2C: "Micron",
        0x45: "SanDisk",
        0x4A: "SMIC",
        0x51: "Qimonda",
        0x89: "Intel",
        0x92: "ESMT Powerchip",
        0x98: "Toshiba",
        0x9B: "Custom",
        0x9D: "Hynix",
        0xB3: "Spectek",
        0xC2: "Macronix",
        0xC8: "ESMT Mira PSC",
        0xEC: "Samsung",
        0xEF: "Winbond"
    }

    nandgen = {
        0: "SLC",
        1: "MLC",
        2: "TLC",
        3: "QLC"
    }

    brand = brands.get(identifier[0], "Unknown NAND Brand")
    memory_type = nandgen.get((identifier[2] >> 2) & 3, "Unknown NAND Type")

    # --------------------------------
    # отреверсил хуёво, адекватно не определяет ничего кроме брендов: 0x2C, 0x45, 0x98
    # --------------------------------
    capacity_info = ""
    if identifier[0] in [0x45, 0x98, 0xB3]:
        capacity_info = f" {1 << ((identifier[4] >> 2) & 3)}Gb/die"
    elif identifier[0] == 0x9B and (identifier[3] & 0xE0) < 0x60:
        capacity_info = f" {1 << ((identifier[3] >> 5) & 3)}Gb/die"

    plane_info = ""
    if identifier[0] in [0x45, 0x98]:
        plane_info = f" {1 << (((identifier[4] >> 2) & 3) - (identifier[2] & 3))}Plane/die"
    elif identifier[0] == 0x9B and (identifier[3] & 0xE0) < 0x60:
        plane_info = f" {1 << ((identifier[3] >> 5) & 3)}Plane/die"

    layer_count = ""
    if identifier[0] in [0x2C, 0x45, 0x98]:
        layer_count = f" {((identifier[2] >> 3) & 3) + 1}L"
    # --------------------------------

    #todo
    return brand, memory_type


identifier = [0x89, 0xd3, 0xac, 0x32, 0xc6, 0]
print("in: ", identifier)
brand, memory_type = decodenand(identifier)
print(brand, memory_type)
