def sum_inventory_calories(sum_inventory_input):
    individual_inventory = []

    elf_no = 0
    individual_inventory.append(0)
    for x in sum_inventory_input:
        if x != '':
            individual_inventory[elf_no] = individual_inventory[elf_no] + int(x)
        else:
            elf_no += 1
            individual_inventory.append(0)

    return individual_inventory


def solve():
    input_list = open("data\\day1.txt").read().split("\n")
    inventories_list = sum_inventory_calories(input_list)
    inventories_list.sort(reverse=True)
    print(inventories_list[0])
    print(sum(inventories_list[:3]))
