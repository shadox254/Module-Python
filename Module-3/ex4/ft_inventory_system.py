def print_inventory(player: str, inventory: dict) -> None:
    print(f"=== {player.capitalize()}'s Inventory ===")
    inventory_value = 0
    total_quantity = 0
    weapon_count = 0
    consumable_count = 0
    armor_count = 0
    for item in inventory:
        item_stats = inventory[item]
        item_price = int(item_stats['quantity'])*int(item_stats['price'])
        print(f"{item} ({item_stats['type']}, {item_stats['rarity']}): {item_stats['quantity']}x @ {item_stats['price']} gold each = {item_price} gold")
        if item_stats['type'] == "weapon":
            weapon_count += item_stats['quantity']
        if item_stats['type'] == "consumable":
            consumable_count += item_stats['quantity']
        if item_stats['type'] == "armor":
            armor_count += item_stats['quantity']
        inventory_value += item_price
        total_quantity += item_stats['quantity']
    print()
    print(f"Inventory value: {inventory_value} gold")
    print(f"Item count: {total_quantity} items")
    print(f"Categories: weapon({weapon_count}), consumable({consumable_count}), armor({armor_count})")
    print()


def transaction(giver: str, receiver: str, players_inv: dict, item: str, quantity_to_give: int) -> None:
    if quantity_to_give > 1:
        print(f"=== Transaction: {giver.capitalize()} gives {receiver.capitalize()} {quantity_to_give} {item}s ===")
    elif quantity_to_give == 1:
        print(f"=== Transaction: {giver.capitalize()} gives {receiver.capitalize()} a {item} ===")
    else:
        print(f"=== Transaction error! Can't give {quantity_to_give} {item} ===")
        print()
        return None

    if players_inv[giver]['potion']['quantity'] >= quantity_to_give and item in players_inv[giver]:
        print("Transaction successful!")
    elif item not in players_inv[giver]:
        print(f"Transaction canceled! {giver.capitalize()} does not own {item}")
        print()
        return None
    else:
        print(f"Transaction failed! {giver.capitalize()} does not have enough potion.")
        print()
        return None
    print()

    print("=== Updated Inventories ===")
    new_giver_quantity = players_inv[giver][item]['quantity'] - quantity_to_give
    new_giver_inv = players_inv[giver].copy()
    new_giver_inv[item]['quantity'] = new_giver_quantity
    new_receiver_inv = players_inv[receiver].copy()
    if item in players_inv[receiver]:
        new_receiver_quantity = players_inv[receiver][item]['quantity'] + quantity_to_give
    else:
        new_receiver_quantity = quantity_to_give
        new_receiver_inv[item] = players_inv[giver][item]
        new_receiver_inv[item]['quantity'] = new_receiver_quantity
    players_inv[giver].update(new_giver_inv)
    players_inv[receiver].update(new_receiver_inv)
    if quantity_to_give > 1:
        print(f"{giver.capitalize()} {item}s: {players_inv[giver][item]['quantity']}")
        print(f"{receiver.capitalize()} {item}s: {players_inv[receiver][item]['quantity']}")
    else:
        print(f"{giver.capitalize()} {item}: {players_inv[giver][item]['quantity']}")
        print(f"{receiver.capitalize()} {item}: {players_inv[receiver][item]['quantity']}")
    print()
    print()
    print()
    print()
    print()
    print_inventory("alice", players_inv["alice"])
    print_inventory("bob", players_inv["bob"])


def inventory_system(players_inv) -> None:
    print("=== Player Inventory System ===")
    print()
    print_inventory("alice", players_inv["alice"])
    transaction("alice", "bob", players_inv, "potion", 2)
    # print_inventory("alice", players_inv["alice"])


if __name__ == "__main__":
    players_inv = {
        "alice": {
            "sword": {"type": "weapon", "rarity": "rare", "price": 500, "quantity": 1},
            "potion": {"type": "consumable", "rarity": "common", "price": 50, "quantity": 5},
            "shield": {"type": "armor", "rarity": "uncommon", "price": 200, "quantity": 1}
        },
        "bob": {
            "Wizard's staff": {"type": "weapon", "rarity": "uncommon", "price": 300, "quantity": 1},
            "magic_ring": {"type": "weapon", "rarity": "rare", "price": 750, "quantity": 1},
            "cloak": {"type": "armor", "rarity": "common", "price": 150, "quantity": 1},
            "mana potion": {"type": "potion", "rarity": "uncommon", "price": 50, "quantity": 7}
        }
    }
    inventory_system(players_inv)