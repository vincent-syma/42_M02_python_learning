#!/usr/bin/env python3

import sys

# ANSI
RESET = "\033[0m"
BOLD = "\033[1m"

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"

# combinations
BOLD_RED = BOLD + RED
BOLD_GREEN = BOLD + GREEN
BOLD_BLUE = BOLD + BLUE


def parse_arg(arg: str) -> tuple:
    """
    Parses argument into dict name and value. If invalid, raises ValueError.
    """
    i = 0

    while i < len(arg) and arg[i] != ":":
        i += 1

    if i == len(arg):
        raise ValueError("Invalid item syntax.\n"
                         "Correct syntax: 'item_name:amount'")

    name = arg[:i]
    qty_str = arg[i+1:]
    try:
        qty = int(qty_str)
        return (name, qty)
    except ValueError:
        raise ValueError(f"Invalid item quantity for '{name}'.\n"
                         f"'{qty_str}' must be an integer")
        # return None


def main() -> None:
    """
    Entry point of inventory system program.
    """
    print()
    print(f"{BLUE}{BOLD}=== Inventory System Analysis ==={RESET}")
    print()

    argc = len(sys.argv)

    if argc == 1:
        print(f"{BOLD}Empty inventory.{RESET}")
        print(f'{YELLOW}Add something to it:\n{RESET}"python3 '
              'ft_inventory_system.py item_name1:amount1 '
              'item2_name:amount2 ... "')
        print()
        return

    inventory = dict()

    for arg in sys.argv[1:]:
        try:
            name, qty = parse_arg(arg)
            inventory[name] = qty
        except ValueError as e:
            print(f"{RED}Error adding item '{arg}': {e}{RESET}")
            print()

    total = 0
    for qty in inventory.values():
        total += qty
    print(f"Total items in inventory: {total}")
    print(f"Unique item types: {len(inventory)}")

    print()
    print(f"{YELLOW}{BOLD}=== Current Inventory ==={RESET}")
    print()
    for name, qty in inventory.items():
        percentage = qty / total * 100
        print(f"{name}: {qty} units ({percentage:.2f}%)")

    print()
    print(f"{YELLOW}{BOLD}=== Inventory Statistics ==={RESET}")
    print()
    most_name = None
    most_qty = -1
    for name, qty in inventory.items():
        if qty > most_qty:
            most_qty = qty
            most_name = name
    print(f"Most abundant: {most_name} ({most_qty} units)")
    least_name = None
    least_qty = 9999999999
    for name, qty in inventory.items():
        if qty < least_qty:
            least_qty = qty
            least_name = name
    print(f"Least abundant: {least_name} ({least_qty} units)")

    print()
    print(f"{YELLOW}{BOLD}=== Item categories ==={RESET}")
    print()
    categories = {
        "Moderate": {},
        "Scarce": {}
    }
    for name, qty in inventory.items():
        if qty >= 5:
            categories["Moderate"].update({name: qty})
        else:
            categories["Scarce"].update({name: qty})

    for cat_name, items_dict in categories.items():
        print(f"{cat_name}: {items_dict}")

    print()
    print(f"{YELLOW}{BOLD}=== Management Suggestions ==={RESET}")
    print()
    restock_list = list()
    for name, qty in inventory.items():
        if qty <= 1:
            restock_list.append(name)
    if restock_list:
        print("Restock needed:", end=" ")
        for i in range(len(restock_list)):
            print(restock_list[i], end="")
            if i != len(restock_list) - 1:
                print(", ", end="")

    print()
    print()
    print(f"{YELLOW}{BOLD}=== Dictionary Properties Demo ==={RESET}")
    print()
    # print(f"Dictionary keys: {inventory.keys()}")
    print("Dictionary keys:", end=" ")
    keys_list = list(inventory.keys())
    for i in range(len(keys_list)):
        print(keys_list[i], end="")
        if i != len(keys_list) - 1:
            print(", ", end="")
    print()
    # print(f"Dictionary values: {inventory.values()}")
    print("Dictionary values:", end=" ")

    for i in range(len(keys_list)):
        print(inventory[keys_list[i]], end="")
        if i != len(keys_list) - 1:
            print(", ", end="")
    print()
    print()
    print("Sample lookup - 'sword' in inventory: "
          f"{inventory.get('sword') is not None}")
    print()


if __name__ == "__main__":
    main()
