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

    if item in players_inv[giver] and players_inv[giver][item]['quantity'] >= quantity_to_give:
        print("Transaction successful!")
    elif item not in players_inv[giver]:
        print(f"Transaction canceled! {giver.capitalize()} does not own {item}")
        print()
        return None
    else:
        print(f"Transaction failed! {giver.capitalize()} does not have enough {item}.")
        print()
        return None
    print()

    print("=== Updated Inventories ===")
    players_inv[giver][item]['quantity'] -= quantity_to_give
    
    if item in players_inv[receiver]:
        players_inv[receiver][item]['quantity'] += quantity_to_give
    else:
        players_inv[receiver][item] = players_inv[giver][item].copy()
        players_inv[receiver][item]['quantity'] = quantity_to_give

    if quantity_to_give > 1:
        print(f"{giver.capitalize()} {item}s: {players_inv[giver][item]['quantity']}")
        print(f"{receiver.capitalize()} {item}s: {players_inv[receiver][item]['quantity']}")
    else:
        print(f"{giver.capitalize()} {item}: {players_inv[giver][item]['quantity']}")
        print(f"{receiver.capitalize()} {item}: {players_inv[receiver][item]['quantity']}")
    print()


def inventory_analytics(players_inv):
    print("=== Inventory Analytics ===")
    highest_value = 0
    for player, inventory in players_inv.items():
        current_player_value = 0
        for item in inventory.values():
            current_player_value += item['price'] * item['quantity']
        if current_player_value > highest_value:
            highest_value = current_player_value
            mvp = player
    print(f"Most valuable player: {mvp.capitalize()} ({highest_value} gold)")

    max_quantity = 0
    for player, inventory in players_inv.items():
        current_quantity = sum(item['quantity'] for item in inventory.values())
        if current_quantity > max_quantity:
            max_quantity = current_quantity
            most_items_player = player
    print(f"Most items: {most_items_player.capitalize()} ({max_quantity} items)")

    rarest_items = []
    for inventory in players_inv.values():
        for item, item_stats in inventory.items():
            if item_stats['rarity'] == "rare":
                rarest_items.append(item)
    print(f"Rarest items: {', '.join(rarest_items)}")


def inventory_system(players_inv) -> None:
    print("=== Player Inventory System ===")
    print()
    print_inventory("alice", players_inv["alice"])
    transaction("alice", "bob", players_inv, "potion", 2)
    inventory_analytics(players_inv)
    print_inventory("alice", players_inv["alice"])
    print_inventory("bob", players_inv["bob"])
    


if __name__ == "__main__":
    players_inv = {
        "alice": {
            "sword": {"type": "weapon", "rarity": "rare", "price": 500, "quantity": 1},
            "potion": {"type": "consumable", "rarity": "common", "price": 50, "quantity": 5},
            "shield": {"type": "armor", "rarity": "uncommon", "price": 200, "quantity": 1}
        },
        "bob": {
            "Wizard's staff": {"type": "weapon", "rarity": "uncommon", "price": 150, "quantity": 1},
            "magic_ring": {"type": "weapon", "rarity": "rare", "price": 300, "quantity": 1},
            "cloak": {"type": "armor", "rarity": "common", "price": 100, "quantity": 1},
        }
    }
    inventory_system(players_inv)