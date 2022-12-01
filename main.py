import time


def read_input():
    return open("data\\input.txt").read().split("\n")


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


def day1():
    inventories_list.sort(reverse=True)
    print(inventories_list[0])
    print(sum(inventories_list[:3]))

    # 72240
    # 210957
    # Execution time (ms): 0.42569986544549465


if __name__ == '__main__':
    start = time.perf_counter()

    input_list = read_input()
    inventories_list = sum_inventory_calories(input_list)

    day1()

    elapsed_time = (time.perf_counter() - start) * 1000
    print("Execution time (ms):", elapsed_time)

